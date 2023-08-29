class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []

    def drive(self):
        return "Brum brum"

    def passenger_count(self):
        return len(self.passengers)
    
    
        



# print(increase_passengers)

    def pick_up(self, input_passenger):
        self.passengers.append(input_passenger)
    
    def drop_off(self, input_passenger):
        self.passengers.remove(input_passenger)
    
    def empty_bus(self):
        self.passengers.clear()
    

    
