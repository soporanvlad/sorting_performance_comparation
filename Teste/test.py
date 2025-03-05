from Domain.entity import Car
from Service.service import Service


class TestService:
    def __init__(self):
        self.car_service = Service([])

    def test_selection_sort(self):
        car_list = [
            Car("Hyundai", "Seria_3", "B1OPEI", 22602, 7312),
            Car("Honda", "A-Class", "AOXK7X", 20740, 7720),
            Car("Honda", "Civic", "DA6L4I", 25345, 11274),
            Car("Ford", "A-Class", "CBCF64", 17955, 5264),
            Car("Audi", "Civic", "I9Q8SA", 20394, 8982),
            Car("Honda", "A-Class", "HFAASB", 20343, 4081),
            Car("Tesla", "Civic", "EGXTNJ", 29617, 10976),
            Car("Audi", "Golf", "J3KV2N", 22951, 3333),
            Car("Honda", "Focus", "FHA9B4", 16096, 5471),
            Car("Audi", "Civic", "GSWYYV", 17077, 8297)
        ]

        expected_sorted_cars = [
            Car("Honda", "A-Class", "AOXK7X", 20740, 7720),
            Car("Hyundai", "Seria_3", "B1OPEI", 22602, 7312),
            Car("Ford", "A-Class", "CBCF64", 17955, 5264),
            Car("Honda", "Civic", "DA6L4I", 25345, 11274),
            Car("Tesla", "Civic", "EGXTNJ", 29617, 10976),
            Car("Honda", "Focus", "FHA9B4", 16096, 5471),
            Car("Audi", "Civic", "GSWYYV", 17077, 8297),
            Car("Honda", "A-Class", "HFAASB", 20343, 4081),
            Car("Audi", "Civic", "I9Q8SA", 20394, 8982),
            Car("Audi", "Golf", "J3KV2N", 22951, 3333),
        ]

        sorted_cars = (self.car_service.selection_sort(car_list, "token"))
        assert sorted_cars == expected_sorted_cars

    def test_quick_sort(self):
        car_list = [
            Car("Mercedes", "Rio", "JZYNCT", 28663, 9795),
            Car("Tesla", "Rio", "RGP9SJ", 29753, 4825),
            Car("Mercedes", "A-Class", "M2DD7P", 17650, 6890),
            Car("BMW", "Focus", "477G7T", 24295, 8064)
        ]

        expected_sorted_cars = [
            Car("Mercedes", "A-Class", "M2DD7P", 17650, 6890),
            Car("Mercedes", "Rio", "JZYNCT", 28663, 9795),
            Car("BMW", "Focus", "477G7T", 24295, 8064),
            Car("Tesla", "Rio", "RGP9SJ", 29753, 4825)
        ]

        sorted_cars = self.car_service.quick_sort(car_list, "brand/model")
        assert sorted_cars == expected_sorted_cars

    def run_all_tests(self):
        self.test_selection_sort()
        self.test_quick_sort()
        print("All tests passed!")



