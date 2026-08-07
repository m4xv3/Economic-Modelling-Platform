class Household:
    def __init__(self, population, savings_rate):
        self.population = population
        self.income = 0
        self.savings_rate = savings_rate
        self.consumption = 0
        self.savings = 0

    def receive_income(self, income):
        self.income = income

    def calculate_consumption(self):

        self.savings = self.income * self.savings_rate
        self.consumption = self.income - self.savings
        
        return self.consumption


class LowIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.05
            )

class MiddleIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 30_000_000,
            savings_rate = 0.1
        )

class HighIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.2
        )