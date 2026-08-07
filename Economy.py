from CentralBank import CentralBank
from Sectors import (
    ManufacturingSector,
    ServiceSector,
    AgricultureSector,
    TechnologySector
)
class Economy:
    def __init__(self):
        self.gdp = 0

        self.centralBank = CentralBank()

        self.manufacturing = ManufacturingSector()
        self.services = ServiceSector()
        self.agriculture = AgricultureSector()
        self.technology = TechnologySector()

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