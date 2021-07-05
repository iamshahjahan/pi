from model.parking import SmallSizeParkingSpot, MediumSizeParkingSpot, LargeSizeParkingSpot, ParkingLot, ParkingSpotType


def start():
    carparkingspot1 = MediumSizeParkingSpot(1, 1)
    carparkingspot2 = MediumSizeParkingSpot(2, 1)
    carparkingspot3 = MediumSizeParkingSpot(3, 1)
    carparkingspot4 = MediumSizeParkingSpot(4, 1)

    bikeParkingspot1 = SmallSizeParkingSpot(11, 1)
    bikeParkingspot2 = SmallSizeParkingSpot(12, 1)
    bikeParkingspot3 = SmallSizeParkingSpot(13, 1)
    bikeParkingspot4 = SmallSizeParkingSpot(14, 1)

    truckParkingspot1 = LargeSizeParkingSpot(111, 1)
    truckParkingspot2 = LargeSizeParkingSpot(112, 1)
    truckParkingspot3 = LargeSizeParkingSpot(113, 1)
    truckParkingspot4 = LargeSizeParkingSpot(114, 1)

    parking_lot = ParkingLot()

    parking_lot.add_a_spot(ParkingSpotType.MEDIUM_SIZE, carparkingspot1)
    parking_lot.add_a_spot(ParkingSpotType.MEDIUM_SIZE, carparkingspot2)
    parking_lot.add_a_spot(ParkingSpotType.MEDIUM_SIZE, carparkingspot3)
    parking_lot.add_a_spot(ParkingSpotType.MEDIUM_SIZE, carparkingspot4)

    parking_lot.add_a_spot(ParkingSpotType.SMALL_SIZE, bikeParkingspot1)
    parking_lot.add_a_spot(ParkingSpotType.SMALL_SIZE, bikeParkingspot2)
    parking_lot.add_a_spot(ParkingSpotType.SMALL_SIZE, bikeParkingspot3)
    parking_lot.add_a_spot(ParkingSpotType.SMALL_SIZE, bikeParkingspot4)
    #
    parking_lot.add_a_spot(ParkingSpotType.LARGE_SIZE, truckParkingspot1)
    parking_lot.add_a_spot(ParkingSpotType.LARGE_SIZE, truckParkingspot2)
    parking_lot.add_a_spot(ParkingSpotType.LARGE_SIZE, truckParkingspot3)
    parking_lot.add_a_spot(ParkingSpotType.LARGE_SIZE, truckParkingspot4)

    parking_spot = parking_lot.search_a_spot(ParkingSpotType.LARGE_SIZE)

    print(parking_spot)

    print(parking_lot.book_a_spot(parking_spot))
    print(parking_lot.release_a_spot(parking_spot))
    print(parking_lot.release_a_spot(parking_spot))




if __name__ == "__main__":
    start()
