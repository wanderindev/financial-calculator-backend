from math import ceil
from typing import List, Tuple


# noinspection PyTypeChecker
# tag::calculator_class[]
class Calculator:
    freq_items = [
        (u"Año", 1, 10),
        ("Semestre", 2, 10),
        ("Cuatrimestre", 3, 12),
        ("Bimestre", 6, 12),
        ("Mes", 12, 12),
        ("Quincena", 24, 12),
        ("Bi-semana", 26, 13),
        ("Semana", 52, 13),
        (u"Día", 365, 15),
    ]

    def __init__(self, **kwargs):
        self.freq = self.get_int(kwargs.get("freq", 12))
        self.num_of_years = self.get_float(kwargs.get("num_of_years", 0))
        self.rate = self.get_float(kwargs.get("rate", 0))
        self.time_scale, rows_per_page = self.get_time_scale(self.freq)
        self.periods = self.get_periods() # end::calculator_class[]
        self.periods_a = self.get_periods_a()
        self.periods_m = self.get_periods_m()
        self.num_of_years_t = self.num_of_years
        self.nper_t = 0
        self.interests = []
        self.balances = []


    @staticmethod
    def get_float(val: str) -> float:
        return float(str(val).replace(",", ""))

    @staticmethod
    def get_int(val: str) -> int:
        return int(str(val).replace(",", ""))

    def get_periods(self) -> List[int]:
        return [x + 1 for x in range(ceil(self.freq * self.num_of_years))]

    def get_periods_a(self) -> List[int]:
        return [x + 1 for x in range(ceil(1 * self.num_of_years))]

    def get_periods_m(self) -> List[int]:
        return [x + 1 for x in range(ceil(12 * self.num_of_years))]

    def get_time_scale(self, freq: int) -> Tuple[str, int]:
        f = freq if freq else 12
        for item in self.freq_items:
            if item[1] == f:
                return item[0], item[2]
