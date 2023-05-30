# Aby uzyskać lepsze wyczucie wzorca stanu i maszyny stanu, zdecydowanie zalecane jest
# wdrożenie własnego przykładu. Może to być cokolwiek: prosta gra wideo (do obsługi stanów
# głównego bohatera i wrogów można użyć automatów stanu), winda, parser lub dowolny inny
# system, który można modelować za pomocą automatów stanów.
# wybrałem winde

from state_machine import (State, Event, acts_as_state_machine,
                           after, before, InvalidStateTransition)


@acts_as_state_machine
class Elevator:
    STATIONARY = State(initial=True)
    MOVING_UP = State()
    MOVING_DOWN = State()

    up_button_pressed = Event(from_states=(STATIONARY,), to_state=MOVING_UP)
    down_button_pressed = Event(from_states=(STATIONARY,), to_state=MOVING_DOWN)
    stop = Event(from_states=(MOVING_UP, MOVING_DOWN), to_state=STATIONARY)

    current_floor = 0
    floors_count = 10

    def __init__(self):
        self.is_initialized = False

    def up(self, to_floor):
        if self.current_floor >= to_floor:
            raise InvalidStateTransition
        else:
            self.current_floor = to_floor
            print(f"Moved up to floor {to_floor}")

    def down(self, to_floor):
        if self.current_floor <= to_floor:
            raise InvalidStateTransition
        else:
            self.current_floor = to_floor
            print(f"Moved down to floor {to_floor}")

    @after('up_button_pressed')
    def go_up(self):
        if self.current_floor == 0:
            self.up(1)
        elif self.current_floor < self.floors_count - 1:
            self.up(self.current_floor + 1)

    @after('down_button_pressed')
    def go_down(self):
        if self.current_floor == 9:
            self.down(self.current_floor - 1)
        elif self.current_floor > 0:
            self.down(self.current_floor - 1)

    def move(self):
        try:
            if self.state == Elevator.MOVING_UP:
                self.up(self.current_floor + 1)
            elif self.state == Elevator.MOVING_DOWN:
                self.down(self.current_floor - 1)
        except InvalidStateTransition:
            self.stop()

    @before('stop')
    def stop_elevator(self):
        print(f"Stopped on floor {self.current_floor}")

    @property
    def state(self):
        return self.current_state

    @staticmethod
    def main():
        elevator = Elevator()
        elevator.up_button_pressed()
        for i in range(9):
            elevator.move()
        elevator.stop()
        elevator.down_button_pressed()
        for i in range(9):
            elevator.move()
        elevator.stop()

        # The simulation is complete
        print("Simulation complete.")

if __name__ == '__main__':
        Elevator.main()
