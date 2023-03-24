MINI14 = '1.4GHz Mac mini'
IPAD = 'iPad Pro'
IPAD2 = 'IPAD PRO MAX MAX 2025'


class AppleFactory:
    class MacMini14:
        def __init__(self):
            self.memory = 4  # in gigabytes
            self.hdd = 500  # in gigabytes
            self.gpu = 'Intel HD Graphics 5000'

        def __str__(self):
            info = (f'Model: {MINI14}',
                    f'Memory: {self.memory}GB',
                    f'Hard Disk: {self.hdd}GB',
                    f'Graphics Card: {self.gpu}')
            return '\n'.join(info)

    class IpadPro:
        def __init__(self):
            self.memory = 8  # in gigabytes
            self.storage = 256  # in gigabytes
            self.gpu = 'Apple GPU 7-core graphics'
            self.processor = 'Apple A15Z Bionic'

        def __str__(self):
            info = (f'Model: {IPAD}',
                    f'Memory: {self.memory}GB',
                    f'Storage: {self.storage}GB',
                    f'Graphics Card: {self.gpu}'
                    f'Processor: {self.processor}')
            return '\n'.join(info)

    def build_computer(self, model):
        if model == MINI14:
            return self.MacMini14()
        elif model == IPAD:
            return self.IpadPro()
        else:
            msg = f"I don't know how to build {model}"
            print(msg)


class Computer:
    def __init__(self, serial_number):
        self.serial = serial_number
        self.memory = None  # in gigabytes
        self.hdd = None     # in gigabytes
        self.gpu = None

    def __str__(self):
        info = (f'Memory: {self.memory}GB',
                f'Hard Disk: {self.hdd}GB',
                f'Graphics Card: {self.gpu}',
                f'Serial Number: {self.serial}')
        return '\n'.join(info)


class ComputerBuilder:
    def __init__(self, serial_number):
        self.computer = Computer(serial_number)
        self.serial = serial_number

    def configure_memory(self, amount):
        self.computer.memory = amount

    def configure_hdd(self, amount):
        self.computer.hdd = amount

    def configure_gpu(self, gpu_model):
        self.computer.gpu = gpu_model


class HardwareEngineer:
    def __init__(self):
        self.builder = None

    def construct_computer(self, memory, hdd, gpu, serial_number):
        self.builder = ComputerBuilder(serial_number)
        self.builder.configure_memory(memory)
        self.builder.configure_hdd(hdd)
        self.builder.configure_gpu(gpu)

    @property
    def computer(self):
        return self.builder.computer


def main():
    engineer = HardwareEngineer()
    engineer.construct_computer(hdd=500, memory=8, gpu='GeForce GTX 650 Ti', serial_number='132839')
    computer = engineer.computer
    print(computer)
    print("\n")
    factory = AppleFactory()
    ipad_pro = factory.build_computer(IPAD)
    print(ipad_pro)
    print("\n")
    factory = AppleFactory()
    ipad_pro = factory.build_computer(IPAD2)
    print(ipad_pro)


if __name__ == '__main__':
    main()
