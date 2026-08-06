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