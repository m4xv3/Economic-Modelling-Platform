from central_bank import CentralBank

from sectors import (
    ManufacturingSector,
    ServiceSector,
    AgricultureSector,
    TechnologySector
)

from households import (
    LowIncomeHouseholds,
    MiddleIncomeHouseholds,
    HighIncomeHouseholds
)

class Economy:
    def __init__(self):
        self.gdp = 0

        self.central_bank = CentralBank()

        self.manufacturing = ManufacturingSector()
        self.services = ServiceSector()
        self.agriculture = AgricultureSector()
        self.technology = TechnologySector()

        self.low_income_households = LowIncomeHouseholds()
        self.middle_income_households = MiddleIncomeHouseholds()
        self.high_income_households = HighIncomeHouseholds()

    def calculate_gdp(self):
        manufacturing_output = self.manufacturing.produce(300_000_000_000)
        services_output = self.services.produce(800_000_000_000)
        agriculture_output = self.agriculture.produce(50_000_000_000)
        technology_output = self.technology.produce(200_000_000_000)

        self.gdp = (
            manufacturing_output
            + services_output
            + agriculture_output
            + technology_output
        )
        return self.gdp
        #GDP = consumption + investment + government spending + (ex - im)

    def distribute_income(self):
        total_income = self.calculate_total_income()

        self.low_income_households.receive_income(
            total_income * 0.2
            )  

        self.middle_income_households.receive_income(
            total_income * 0.5
            )

        self.high_income_households.receive_income(
            total_income * 0.3
            )
        
    def calculate_employment(self):
        total_labour_force = (
            self.manufacturing.labour_force
            + self.services.labour_force
            + self.agriculture.labour_force
            + self.technology.labour_force
        )

        total_employed = (
            self.manufacturing.employed_workers
            + self.services.employed_workers
            + self.agriculture.employed_workers
            + self.technology.employed_workers
        )

        return total_employed / total_labour_force

    def calculate_consumption(self):
        total_consumption = (
            self.low_income_households.calculate_consumption()
            + self.middle_income_households.calculate_consumption()
            + self.high_income_households.calculate_consumption()
        )
        return total_consumption

    def calculate_total_income(self):

        total_income = (
            self.manufacturing.calculate_wage_bill()
            + self.services.calculate_wage_bill()
            + self.agriculture.calculate_wage_bill()
            + self.technology.calculate_wage_bill()
            )

        return total_income