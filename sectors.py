class EconomicSector:
    def __init__(
            self,
            labour_force,
            employed_workers,
            capital_stock,
            productivity,
            labour_weight,
            capital_weight,
            average_wage
            ):  
         
        self.labour_force = labour_force
        self.employed_workers = employed_workers
        self.capital_stock = capital_stock
        self.productivity = productivity
        self.labour_weight = labour_weight
        self.capital_weight = capital_weight
        self.average_wage = average_wage

    def produce(self, demand):
        potential_output = (
            self.productivity * (self.employed_workers ** self.labour_weight) * (self.capital_stock ** self.capital_weight)
            )
        actual_output = min(potential_output, demand)
        return actual_output
        
    def employment_rate(self):
        return self.employed_workers/self.labour_force

    def calculate_wage_bill(self):
        return self.employed_workers * self.average_wage


class ManufacturingSector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force=5_000_000,
            employed_workers=4_800_000,
            capital_stock=2_000_000_000_000,
            productivity=25,
            labour_weight = 0.4,
            capital_weight = 0.6,
            average_wage = 50_000
        )

class ServiceSector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force = 15_000_000,
            employed_workers = 14_400_000,
            capital_stock = 3_000_000_000_000,
            productivity = 30,
            labour_weight = 0.8,
            capital_weight = 0.2,
            average_wage = 45_000
        )

class AgricultureSector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force = 1_000_000,
            employed_workers = 900_000,
            capital_stock = 2_500_000_000_000,
            productivity = 20,
            labour_weight = 0.6,
            capital_weight = 0.4,
            average_wage=30_000
        )

class TechnologySector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force = 3_000_000,
            employed_workers = 2_500_000,
            capital_stock=1_500_000_000_000,
            productivity=60,
            labour_weight = 0.6,
            capital_weight = 0.4,
            average_wage = 80_000
        )
