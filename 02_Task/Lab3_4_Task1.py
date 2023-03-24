import json
import xml.etree.ElementTree as etree
import sqlite3

from django import forms


class PersonForm(forms.Form):
    name = forms.CharField(max_length=100)
    birth_date = forms.DateField(required=False)


class Data:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class DataExtractor:
    def __init__(self, filepath):
        self.filepath = filepath


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree.getroot()


class SQLiteDataExtractor(DataExtractor):
    def __init__(self, filepath):
        super().__init__(filepath)
        self.conn = sqlite3.connect(filepath)

    def execute_query(self, query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        data = cursor.fetchall()
        return data

    @property
    def parsed_data(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        return data


def dataextraction_factory(filepath):
    if filepath.endswith('json'):
        extractor = JSONDataExtractor
    elif filepath.endswith('xml'):
        extractor = XMLDataExtractor
    elif filepath.endswith('db'):
        extractor = SQLiteDataExtractor
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))
    return extractor(filepath)


def extract_data_from(filepath):
    if filepath.endswith('.db'):
        return SQLiteDataExtractor(filepath)
    else:
        raise ValueError('Cannot extract data from {}'.format(filepath))


data_factory = extract_data_from('data.db')

conn = sqlite3.connect('data.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS data
                  (name text, age integer)''')

data = [Data('John', 25), Data('Jimy', 19), Data('Patty', 20)]

for d in data:
    cursor.execute("INSERT INTO data VALUES (?, ?)", (d.name, d.age))

conn.commit()
conn.close()

result = data_factory.execute_query('SELECT * FROM data')
print(result)

sqlite_factory = extract_data_from('data.db')
sqlite_data = sqlite_factory.parsed_data
print(f'Found: {len(sqlite_data)} records')
for record in sqlite_data:
    print(f"Name: {record[0]}, Age: {record[1]}")


def main():
    json_factory = dataextraction_factory('data/movies.json')
    json_data = json_factory.parsed_data
    print(f'Found: {len(json_data)} movies')
    for movie in json_data:
        print(f"Title: {movie.get('title')}")
        year = movie.get('year')
        if year:
            print(f"Year: {year}")
        director = movie.get('director')
        if director:
            print(f"Director: {director}")
        genre = movie.get('genre')
        if genre:
            print(f"Genre: {genre}")
        print()

    xml_factory = dataextraction_factory('data/person.xml')
    xml_data = xml_factory.parsed_data
    liars = xml_data.findall(".//person[lastName='Liar']")
    print(f'found: {len(liars)} persons')
    for liar in liars:
        firstname = liar.find('firstName').text
        print(f'first name: {firstname}')
        lastname = liar.find('lastName').text
        print(f'last name: {lastname}')
        for p in liar.find('phoneNumbers'):
            print(f"phone number ({p.attrib['type']}): {p.text}")
        print()

# sql lite

    sqlite_factory = extract_data_from('data.db')
    sqlite_data = sqlite_factory.parsed_data
    print(f'Found: {len(sqlite_data)} records')
    for record in sqlite_data:
        print(f"Name: {record[0]}, Age: {record[1]}")


if __name__ == '__main__':
    main()