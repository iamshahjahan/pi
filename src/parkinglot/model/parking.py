from abc import ABC
from enum import Enum
from typing import List


class User(ABC):
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Admin(User):
    def __init__(self, name, address, privilege):
        super().__init__(name, address)
        self.privilege = privilege


class ParkingAttendant(User):
    def __init__(self, name, address, privilege):
        super().__init__(name, address)
        self.privilege = privilege


class VehicleType(Enum):
    CAR, BIKE, TRUCK = 0, 1, 2


class ParkingSpotType(Enum):
    MEDIUM_SIZE, SMALL_SIZE, LARGE_SIZE = 0, 1, 2


class Vehicle(ABC):
    def __init__(self, vin):
        self.vin = vin


class Car(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)


class Truck(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)


class Bike(Vehicle):
    def __init__(self, vin):
        super().__init__(vin)


class ParkingSpot(ABC):
    def __init__(self, number, floor):
        self.number = number
        self.floor = floor
        self.occupied = False

    def __repr__(self):
        return f"{self.number}:{self.floor}:{self.occupied}"


class SmallSizeParkingSpot(ParkingSpot):
    def __init__(self, number, floor):
        super().__init__(number, floor)


class MediumSizeParkingSpot(ParkingSpot):
    def __init__(self, number, floor):
        super().__init__(number, floor)


class LargeSizeParkingSpot(ParkingSpot):
    def __init__(self, number, floor):
        super().__init__(number, floor)

# mark this singleton
class ParkingLot:
    def __init__(self):
        self.parking_lot = {
            ParkingSpotType.SMALL_SIZE: [],
            ParkingSpotType.MEDIUM_SIZE: [],
            ParkingSpotType.LARGE_SIZE: [],
        }

    def __repr__(self):
        return f"{self.parking_lot}"

    def add_a_spot_by_spot_type(self, parking_spot_list, parking_spot):
        parking_spot_list.append(parking_spot)

    def remove_a_spot_by_spot_type(self, parking_spot_list, parking_spot):
        parking_spot_list.remove(parking_spot)

    def add_a_spot(self, parking_spot_type, parking_spot):
        {
            ParkingSpotType.SMALL_SIZE: self.add_a_spot_by_spot_type,
            ParkingSpotType.MEDIUM_SIZE: self.add_a_spot_by_spot_type,
            ParkingSpotType.LARGE_SIZE: self.add_a_spot_by_spot_type
        }.get(parking_spot_type, "Invalid spot type")(self.parking_lot.get(parking_spot_type),parking_spot)

    def remove_a_spot(self, parking_spot_type, parking_spot):
        switch_case = {
            ParkingSpotType.SMALL_SIZE: self.remove_a_spot_by_spot_type,
            ParkingSpotType.MEDIUM_SIZE: self.remove_a_spot_by_spot_type,
            ParkingSpotType.LARGE_SIZE: self.remove_a_spot_by_spot_type,
        }

        return switch_case.get(parking_spot_type, "Invalid spot type")(self.parking_lot.get(parking_spot_type),parking_spot)

    def return_free_spot(self, parking_lot_by_spot_type: List[ParkingSpot]):
        for parking_spot in parking_lot_by_spot_type:
            if not parking_spot.occupied:
                return parking_spot
        return None

    def search_a_spot(self, parking_spot_type):
        switch_case = {
            ParkingSpotType.SMALL_SIZE: self.return_free_spot(self.parking_lot.get(ParkingSpotType.SMALL_SIZE)),
            ParkingSpotType.MEDIUM_SIZE: self.return_free_spot(self.parking_lot.get(ParkingSpotType.MEDIUM_SIZE)),
            ParkingSpotType.LARGE_SIZE: self.return_free_spot(self.parking_lot.get(ParkingSpotType.LARGE_SIZE)),
        }

        return switch_case.get(parking_spot_type, "Invalid spot type")

    def book_a_spot(self, parking_spot):
        if parking_spot.occupied:
            raise Exception("Already occupied.")
        parking_spot.occupied = True
        return True

    def release_a_spot(self, parking_spot):
        if not parking_spot.occupied:
            raise Exception("Spot is not occupied.")
        parking_spot.occupied = False
        return True
