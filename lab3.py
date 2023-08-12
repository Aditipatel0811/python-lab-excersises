#1
import re
def splitAndDictionary(mainString):
    tempList = re.split("_+", mainString)

    finalDict = {"Name": tempList[0], "Domain": tempList[1], "Registration No.": tempList[2]}
    print(f"\n{finalDict}")

stringMain = "Aditi___Airline management___2347204"
splitAndDictionary(stringMain)


#2
class Airline:
    def __init__(self, flightname, passenger_class):
        self.flightname = flightname
        self.passenger_class = passenger_class

    def display_info(self):
        return f"flightname: {self.flightname}, passenger_class: {self.passenger_class}"

# Subclass 1: Flight (inherits from Airline)
class flight(Airline):
    def __init__(self, flightname, passenger_class, flight_type ):
        super().__init__(flightname, passenger_class)
        self.fight_type = flight_type

    def display_info(self):
        return f"flight - {super().display_info()}, Fight Type: {self.fight_type}"

# Subclass 2: pilot (inherits from Airline)
class pilot(Airline):
    def __init__(self, flightname, passenger_class, pilot_type):
        super().__init__(flightname, passenger_class)
        self.pilot_type = pilot_type

    def display_info(self):
        return f"pilot - {super().display_info()}, Frame Type: {self.pilot_type}"

# Subclass 3: Airline_services (inherits from Airline )
class Airline_services(Airline):
    def __init__(self, flightname, passenger_class, Airline_package):
        super().__init__(flightname, passenger_class)
        self.Airline_package = Airline_package

    def display_info(self):
        return f"Motorcycle - {super().display_info()}, Engine Type: {self.Airline_package}"

if __name__ == "__main__":
    flight = flight("Air One", "Economy", "Connecting")
    pilot = pilot("India One", "Business", "private Pilot")
    Airline_services = Airline_services("Vasant", "Premium Economy Class", "Charter Airline")

    print( flight.display_info())
    print(pilot.display_info())
    print(Airline_services.display_info())

    
    