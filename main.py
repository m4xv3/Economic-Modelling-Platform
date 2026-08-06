class Economy:
    def __init__(self):
        pass

class CentralBank:
    def __init__(self):
        self.inflation_target = 0.02
        self.policy_interest_rate = 0.03
        self.policy_response_strength = 0.5
        self.inflation_tolerance = 0.005
        self.independence = 0.5
        self.policy_stance = "neutral"

    def adjust_policy(self, current_inflation):
        inflation_gap = current_inflation - self.inflation_target
        interest_rate_change = inflation_gap * self.policy_response_strength
        if inflation_gap > self.inflation_tolerance:
            self.policy_interest_rate += interest_rate_change
            self.policy_stance = "tightening"
        elif inflation_gap < -self.inflation_tolerance:
            self.policy_interest_rate += interest_rate_change
            self.policy_stance = "easing"
        else:
            self.policy_stance = "neutral"

class EconomicSector:
    def __init__(self, labour_force, employed_workers, capital_stock, productivity, labour_weight, capital_weight):
        self.labour_force = labour_force
        self.employed_workers = employed_workers
        self.capital_stock = capital_stock
        self.productivity = productivity
        self.labour_weight = labour_weight
        self.capital_weight = capital_weight

    def produce(self, demand):
        potential_output = (
            self.productivity * (self.employed_workers ** self.labour_weight) * (self.capital_stock ** self.capital_weight)
            )
        actual_output = min(potential_output, demand)
        return actual_output
        
    def employment_rate(self):
        return self.employed_workers/self.labour_force

class ManufacturingSector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force=5_000_000,
            employed_workers=4_800_000,
            capital_stock=2_000_000_000_000,
            productivity=25,
            labour_weight = 0.4,
            capital_weight = 0.6
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
        )

class AgricultureSector(EconomicSector):
    def __init__(self):
        super().__init__(
            labour_force = 10_000_000,
            employed_workers = 9_000_000,
            capital_stock = 2_500_000_000_000,
            productivity = 20,
            labour_weight = 0.6,
            capital_weight = 0.4,
        )