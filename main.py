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

class FirmSector:
    def __init__(self):
        self.labour_force = 25_000_000
        self.employed_workers = 23_750_000
        self.capital_stock = 5_000_000_000_000
        self.productivity = 1
        self.labour_weight = 0.7
        self.capital_weight = 0.3

    def produce(self, demand):
        #recieve demand
        #calculate potential output
        # determine actual output

        
    def employment_rate(self):
        employment_rate = self.employed_workers/self.labour_force