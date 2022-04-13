import math
from dataclasses import asdict, dataclass
from decimal import Decimal


@dataclass
class ZipAirplane:
    pk: int
    passengers_count: int

    @property
    def fuel_tank(self) -> int:
        return self.pk * 200

    @property
    def consumption_per_minute(self) -> Decimal:
        return Decimal(math.log(self.pk) * 0.8) + Decimal(0.002 * self.passengers_count)

    def total_fly_minutes(self) -> Decimal:
        return Decimal(self.fuel_tank / self.consumption_per_minute)

    @classmethod
    def from_list(cls, airplane_data: list[dict]) -> list[dict]:
        return [cls(**data).asdict() for data in airplane_data]

    def asdict(self) -> dict:
        values_dict = {
            "fuel_consumption": self.consumption_per_minute,
            "total_fly_minutes": self.total_fly_minutes(),
        }
        return values_dict
