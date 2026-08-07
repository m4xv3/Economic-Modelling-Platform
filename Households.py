class Household:
    def __init__(self, population, income, savings_rate):
        self.population = population
        self.income = income
        self.savings_rate = savings_rate

class LowIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.05,
            income_share = 0.15
        )

class MiddleIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 30_000_000,
            savings_rate = 0.1,
            income_share = 0.5
            )

class HighIncomeHouseholds(Household):
    def __init__(self):
        super().__init__(
            population = 10_000_000,
            savings_rate = 0.2,
            income_share = 0.35
        )
