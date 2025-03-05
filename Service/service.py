from Domain.entity import Car


class Service:
    def __init__(self, car_repo):
        self.cars_repository = car_repo

    def get_all(self):
        return self.cars_repository

    def print_cars(self):
        return list(self.cars_repository.print_all_cars())

    def create_cars(self, nr_cars):
        self.cars_repository.generate_cars(nr_cars)

    def search_by_token(self, car, token):
        if car.get_token() == token:
            return 0
        elif car.get_token() < token:
            return -1
        else:
            return 1

    def secvential_search(self, lista, criteriu_cautare, elem):
        rezultat = []
        for car in lista:
            if self.search_by_token(car, elem) == 0:
                rezultat.append(car)
        return rezultat

    def binary_search(self, car_list, criteriu_cautare, x):
        low = 0
        high = len(car_list)-1
        if criteriu_cautare == "token":
            while low <= high:
                mid = (low + high) // 2
                if x == car_list[mid].get_token():
                    return mid
                elif x > car_list[mid].get_token():
                    low = mid + 1
                else:
                    high = mid - 1
            return -1

    def comparator(self, val1, val2, cmd):
        if cmd == "token":
            cmp = Car.comparator_token(val1, val2)
            return cmp
        elif cmd == "brand/model":
            cmp = Car.comparator_brand_model(val1, val2)
            return cmp
        elif cmd == "brand/model/token":
            cmp = Car.comparator_brand_model_token(val1, val2)
            return cmp
        elif cmd == "profit":
            cmp = Car.comparator_profit(val1, val2)
            return cmp
        else:
            print("Comanda invalida!")

    def swap_elements(self, list2, val1, val2, comparator):
        if comparator == -1:
            aux: int = list2[val1]
            list2[val1] = list2[val2]
            list2[val2] = aux
        else:
            pass

    def selection_sort(self, unsorted_list, cmd):
        for z in range(0, len(unsorted_list) - 1):
            min_index = z
            for m in range(z + 1, len(unsorted_list)):
                if self.comparator(unsorted_list[m], unsorted_list[min_index],
                                   cmd) == 1:  # Compare with 1 for ascending order
                    min_index = m
            if min_index != z:
                self.swap_elements(unsorted_list, z, min_index, -1)
        return unsorted_list

    def quick_sort_1(self, unsorted_list, cmd):
        if len(unsorted_list) <= 1:
            return unsorted_list
        else:
            pivot = unsorted_list[0]
            left = [x for x in unsorted_list[1:] if self.comparator(x, pivot, cmd) != -1]
            right = [x for x in unsorted_list[1:] if self.comparator(x, pivot, cmd) == -1]
            return self.quick_sort(left, cmd) + [pivot] + self.quick_sort(right, cmd)

    def quick_sort(self, unsorted_list, cmd):
        if len(unsorted_list) <= 1:
            return unsorted_list
        else:
            pivot_index = len(unsorted_list) // 2
            pivot = unsorted_list[pivot_index]

            # Partition the list around the pivot
            left = [x for i, x in enumerate(unsorted_list) if i != pivot_index and self.comparator(x, pivot, cmd) >= 0]
            right = [x for i, x in enumerate(unsorted_list) if i != pivot_index and self.comparator(x, pivot, cmd) < 0]

            # Recursively sort the partitions
            return self.quick_sort(left, cmd) + [pivot] + self.quick_sort(right, cmd)

