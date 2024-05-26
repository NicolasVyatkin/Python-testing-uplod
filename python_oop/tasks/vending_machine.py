from collections import defaultdict


class VendingMachineCore:
    def __init__(self, manager_key):
        self.__manager_key = manager_key
        self._products = defaultdict(lambda: 0)

    def _load_products(self, products, manager_key):
        if manager_key != self.__manager_key:
            return "Restricted"
        for product_name, product_count in products.items():
            self._products[product_name] += product_count
        return 'Products loaded OK'

    def _get_product(self, product_name):
        if product_name in self._products:
            current_stock = self._products.get(product_name)
            if not current_stock:
                return 0
            self._products[product_name] -= 1
            return product_name
        return 0

    @property
    def products(self):
        return dict(self._products)


class CocaColaVenndingMachine(VendingMachineCore):
    def _load_coke(self, coke_type, number, manager_key):
        return self._load_products({coke_type: number}, manager_key)


class ServiceManagerInterface:
    def __init__(self):
        print('Plese create manager key: ')
        key = input()
        self._machine = CocaColaVenndingMachine(manager_key=key)

    def load_coke(self, coke_type, number):
        print('Please enter manager key: ')
        manager_key = input()
        return self._machine._load_coke(coke_type, number, manager_key)

    def get_inventory(self):
        if self._machine.products:
            return self._machine.products
        return 'No products'

    def update_public_machine(self):
        return self._machine


class CustomerInterface:
    def __init__(self):
        self._taken_products = defaultdict(lambda: 0)

    def take_product(self, machine, name):
        product = machine._get_product(name)
        if not product:
            return 'No sutch product'
        self._taken_products[name] += 1
        return name

    @property
    def taken_products(self):
        if not self._taken_products:
            return 'No produkts taken'
        return dict(self._taken_products)


class Simulation:
    def __init__(self):
        self.service_manager = ServiceManagerInterface()
        self.customer = CustomerInterface()
        self.machine = None

    @staticmethod
    def get_manual():
        print('Roles: S (service), C (customer)')
        print('S comands: ')
        print('\t INV - get inventory, ')
        print('\t LOAD - load goods inside, ')
        print('C comands: ')
        print('\t GET - get product, ')
        print('\t MY - get curent customer products')

    def run(self):
        while True:
            print('='*40)
            self.get_manual()
            print('='*40)
            print('Input role')
            role = input()
            print('Input comand')
            command = input()
            if role == 'S':
                if command == 'INV':
                    print(self.service_manager.get_inventory())
                elif command == 'LOAD':
                    print('Enter product')
                    product = input()
                    print('Enter count')
                    count = int(input())
                    if count < 1:
                        print('Count should be > 0')
                    else:
                        status = self.service_manager.load_coke(product, count)
                        self.machine = self.service_manager.update_public_machine()
                        print(status)
            elif role == 'C':
                if command == 'GET':
                    if self.machine is None:
                        print('No machine(((')
                    else:
                        print('Enter product: ')
                        product = str(input())
                        print(self.customer.take_product(
                            self.machine, product))
                elif command == 'MY':
                    if self.customer is not None:
                        print(self.customer.taken_products)
                    else:
                        print('No customer :(')
                else:
                    print('Exit')
                    break


if __name__ == '__main__':
    simulator = Simulation()
    simulator.run()
