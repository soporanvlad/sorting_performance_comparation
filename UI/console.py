import time


class UI:
    def __init__(self, service):
        self.cars_service = service

    def print_meniu(self):
        print("\n MENIU \n")
        print("1. Crearea listei ")
        print("2. Afisarea listei ")
        print("3. Cautarea dupa token ")
        print("4. Sortarea rapida a listei ")
        print("5. Sortarea prin selectie a listei ")
        print("6. Iesire din meniu ")

    def print_submeniu(self):
        print("\n SUBMENIU \n")
        print("1. Sortare dupa Token ")
        print("2. Sortare dupa Marca si Model ")
        print("3. Sortare dupa Marca, Model si Token ")
        print("4. Sortare dupa profit ")
        print("5. Iesire ")

    def run_meniu(self):
        while True:
            self.print_meniu()
            option = int(input("Alegeti optiunea : "))
            if option == 1:
                nr = int(input("Introduceti numarul de elemente ale listei: "))
                self.cars_service.create_cars(nr)
            elif option == 2:
                x = self.cars_service.print_cars()
                if len(x) == 0:
                    print("Nu exista masini!")
                    return
                for i in x:
                    print(i)
            elif option == 3:
                pass
                tokencar = input("Introduceti tokenul: ")
                self.search_car(tokencar)
            elif option == 4:
                cmd = input("Option(token, brand/model, brand/model/token, profit): ")
                self.quick_sort_car(cmd)
            elif option == 5:
                cmd = input("Option(token, brand/model, brand/model/token, profit): ")
                self.selection_sort_car(cmd)
            elif option == 6:
                print("Programul s-a incheiat !")
                break
            else:
                print("Alegeti alta optiune !")

    def search_car(self, tokencar):
        criteriu_cautare = "token"
        unsorted_list = self.cars_service.print_cars()
        sorted_list = self.cars_service.quick_sort(unsorted_list, "token")
        x = tokencar
        start_time: float = time.time()
        position = self.cars_service.binary_search(sorted_list, criteriu_cautare, x)
        if position > 0:
            print(f"Car is at the {position} position in sorted car list.")
            print(sorted_list[position], '\n')
        else:
            print(f"Car not in list!\n")
        end_time: float = time.time()
        execution_time = end_time - start_time
        print("Execution time: ")
        print(execution_time)

    def quick_sort_car(self, cmd):
        unsorted_list = self.cars_service.print_cars()
        start_time: float = time.time()
        # sorted_list = self.__car_service.sort_alg_nn(unsorted_list, cmd)
        sorted_list = self.cars_service.quick_sort(unsorted_list, cmd)
        end_time: float = time.time()
        execution_time = end_time - start_time
        for car in sorted_list:
            print(car)
        print("Execution time: ")
        print(execution_time)

    def selection_sort_car(self, cmd):
        unsorted_list = self.cars_service.print_cars()
        start_time: float = time.time()
        # sorted_list = self.__car_service.sort_alg_nn(unsorted_list, cmd)
        sorted_list = self.cars_service.selection_sort(unsorted_list, cmd)
        end_time: float = time.time()
        execution_time = end_time - start_time
        for car in sorted_list:
            print(car)
        print("Execution time: ")
        print(execution_time)