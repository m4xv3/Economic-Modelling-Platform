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

