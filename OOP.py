class Customer:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value


class Bike:
    def __init__(self, name, price):
        self._name = name
        self._price = price

    # Getters and Setters
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value


class ElectricBike(Bike):
    def __init__(self, name, price, maxspeed):
        super().__init__(name, price)
        self._maxspeed = maxspeed

    # Getter and Setter for maxspeed
    @property
    def maxspeed(self):
        return self._maxspeed

    @maxspeed.setter
    def maxspeed(self, value):
        self._maxspeed = value


class NormalBike(Bike):
    def __init__(self, name, price, maxspeed):
        super().__init__(name, price)
        self._maxspeed = maxspeed

    # Getter and Setter for maxspeed
    @property
    def maxspeed(self):
        return self._maxspeed

    @maxspeed.setter
    def maxspeed(self, value):
        self._maxspeed = value


class MainBikeRental:
    def __init__(self):
        self._bikes = []
        self._rentals = []

    # Getters and Setters
    @property
    def bikes(self):
        return self._bikes

    @bikes.setter
    def bikes(self, value):
        self._bikes = value

    @property
    def rentals(self):
        return self._rentals

    @rentals.setter
    def rentals(self, value):
        self._rentals = value

    # Method to request bikes
    def requestBike(self, customer, num_of_bikes):
        if customer.age <= 6:
            print("Customer must be older than 6 years.")
            return False

        available_bikes = len(self._bikes)
        if num_of_bikes <= available_bikes:
            self._bikes = self._bikes[num_of_bikes:]  # Deduct bikes
            self._rentals.append({"customer": customer, "num_of_bikes": num_of_bikes})
            print(f"{num_of_bikes} bikes rented successfully.")
            return True
        else:
            print("Requested bikes not available. Please wait 10 minutes.")
            return False

    # Method to return bikes
    def returnBike(self, rental_time, num_of_bikes):
        total_cost = rental_time * 40 * num_of_bikes
        print(f"Total bill: ${total_cost}")
        for _ in range(num_of_bikes):
            self._bikes.append(Bike("Generic Bike", 100))  # Returning generic bikes
        print(f"{num_of_bikes} bikes returned successfully.")
        return total_cost

    # Method to add bikes
    def addBike(self, bike):
        self._bikes.append(bike)
        print(f"Bike '{bike.name}' added to inventory.")

    # Method to calculate total cost of all bikes
    def totalCost(self):
        return sum(bike.price for bike in self._bikes)


# Example Usage
if __name__ == "__main__":
    rental_system = MainBikeRental()
    customer = Customer("Alice", 25)

    # Add some bikes
    rental_system.addBike(ElectricBike("E-Bike1", 500, 30))
    rental_system.addBike(NormalBike("N-Bike1", 300, 20))
    rental_system.addBike(NormalBike("N-Bike2", 300, 25))

    # Request and return a bike
    rental_system.requestBike(customer, 2)
    rental_system.returnBike(rental_time=3, num_of_bikes=2)

    # Check total cost of all bikes
    print(f"Total value of bikes in stock: ${rental_system.totalCost()}")
