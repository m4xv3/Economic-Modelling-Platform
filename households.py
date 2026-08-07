class Household:
    def __init__(self, population, income, savings_rate):
        self.population = population
        self.income = income
        self.savings_rate = savings_rate
        self.consumption = 0
        self.savings = 0

    def calculate_consumption(self):
        total_income = self.population * self.income

        self.savings = total_income * self.savings_rate
        self.consumption = total_income - self.savings

        return self.consumption


class LowIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.05,
            income = 20_000
        )

class MiddleIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 30_000_000,
            savings_rate = 0.1,
            income = 50_000
        )

class HighIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.2,
            income = 100_000
        )