class Rider:
    def __init__(self, trained_status, experience):
        self.__trained_status = trained_status  # Boolean
        self.__experience = experience          # Integer

    def performs_tricks(self):
        print("Performs stunts and tricks!")

    def rides_vehicle(self):
        print("Rides a vehicle.")

class BikerRider(Rider):
    def __init__(self, trained_status, experience, race_license):
        super().__init__(trained_status, experience)
        self.__race_license = race_license  # Boolean

    def rides_in_dome(self):
        print("Rides the bike in the dome.")

class CycleRider(Rider):
    def __init__(self, trained_status, experience):
        super().__init__(trained_status, experience)

    def rides_blindfolded(self):
        print("Rides the cycle blindfolded.")

# === Example usage ===
print("Bike Rider:")
bike_rider = BikerRider(trained_status=True, experience=5, race_license=True)
bike_rider.rides_vehicle()
bike_rider.rides_in_dome()
bike_rider.performs_tricks()

print("\nCycle Rider:")
cycle_rider = CycleRider(trained_status=True, experience=3)
cycle_rider.rides_vehicle()
cycle_rider.rides_blindfolded()
cycle_rider.performs_tricks()
