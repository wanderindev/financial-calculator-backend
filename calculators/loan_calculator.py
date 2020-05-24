from math import ceil
from numpy_financial import nper, pmt, rate
from typing import List, Tuple

from .calculator import Calculator


# noinspection PyTypeChecker
class LoanCalculator(Calculator):
    def __init__(self, **kwargs):
        super(LoanCalculator, self).__init__(**kwargs)

        self.loan = self.get_float(kwargs.get("loan", 0))
        self.reg_pmt = self.get_float(kwargs.get("reg_pmt", 0))
        self.extra_pmt = self.get_float(kwargs.get("extra_pmt", 0))
        self.extra_pmt_start = self.get_int(kwargs.get("extra_pmt_start", 0))
        self.extra_pmt_f = self.get_int(kwargs.get("extra_pmt_f", 0))
        self.pmt_when = self.get_int(kwargs.get("pmt_when", 0))
        self.payments = []
        self.payments_e = []
        self.payments_r = []
        self.payments_p = []

    def get_balances_loans(self) -> List[float]:
        balances = []

        for x in self.periods:
            bal = self.loan - sum(self.payments[:x]) + sum(self.interests[:x])
            if bal < 0:
                if self.reg_pmt + bal >= 0:
                    self.payments_r[x - 1] = self.reg_pmt + bal
                    self.payments[x - 1] = (
                        self.payments_r[x - 1] + self.payments_e[x - 1]
                    )
                    balances.append(0)
                    self.trunc_periods(x)
                else:
                    self.payments_r[x - 1] = 0
                    self.payments_e[x - 1] = (
                        bal + self.payments_e[x - 1] + self.reg_pmt
                    )
                    self.payments[x - 1] = self.payments_e[x - 1]
                    balances.append(0)
                    self.trunc_periods(x)

                return balances
            else:
                balances.append(
                    self.loan
                    - sum(self.payments[:x])
                    + sum(self.interests[:x])
                )

        return balances

    def get_interests_loans(self) -> List[float]:
        _rate = self.rate / (100 * self.freq)
        interests = [
            round(
                (self.loan - self.payments[0]) * _rate
                if self.pmt_when
                else self.loan * _rate,
                4,
            )
        ]

        for x in self.periods[1:]:
            if self.pmt_when:
                interest = round(
                    (self.loan - sum(self.payments[:x]) + sum(interests[:x]))
                    * _rate,
                    4,
                )
            else:
                interest = round(
                    (
                        self.loan
                        - sum(self.payments[: x - 1])
                        + sum(interests[:x])
                    )
                    * _rate,
                    4,
                )

            if interest < 0:
                interests.append(0)
            else:
                interests.append(interest)

        return interests

    def get_nper_loans(self) -> int:
        _nper = ceil(
            nper(
                self.rate / (100 * self.freq),
                -self.reg_pmt,
                self.loan,
                when=self.pmt_when,
            )
        )

        self.num_of_years = round(_nper / self.freq, 2)
        self.periods = self.get_periods()
        self.periods_a = self.get_periods_a()
        self.periods_m = self.get_periods_m()

        return _nper

    def get_payments(self) -> Tuple[List[float]]:
        self.payments_r = self.get_payments_r()
        self.payments_e = self.get_payments_e()

        self.payments = [
            round(self.payments_r[x - 1] + self.payments_e[x - 1], 4)
            for x in self.periods
        ]

        self.interests = self.get_interests_loans()
        self.balances = self.get_balances_loans()

        return self.payments, self.payments_e, self.payments_r

    def get_payments_e(self) -> List[float]:
        extra_pmt_p = []

        if self.extra_pmt:
            extra_pmt_p.append(self.extra_pmt_start)
            if self.extra_pmt_f:
                for x in self.periods[self.extra_pmt_start :]:
                    if not (x - self.extra_pmt_start) % (
                        12 / self.extra_pmt_f
                    ):
                        extra_pmt_p.append(x)

        return [
            self.extra_pmt if x in extra_pmt_p else 0 for x in self.periods
        ]

    def get_payments_r(self) -> List[float]:
        return [self.reg_pmt for _ in self.periods]

    def get_rate_loans(self):
        return (
            rate(
                self.freq * self.num_of_years,
                -self.reg_pmt,
                self.loan,
                0,
                self.pmt_when,
            )
            * self.freq
            * 100
        )

    def get_reg_pmt(self) -> float:
        self.reg_pmt = round(
            -pmt(
                self.rate / (100 * self.freq),
                self.freq * self.num_of_years,
                self.loan,
                when=self.pmt_when,
            ),
            4,
        )

        return self.reg_pmt

    def trunc_periods(self, p: int) -> None:
        self.periods = self.periods[:p]
        self.payments_r = self.payments_r[:p]
        self.payments_e = self.payments_e[:p]
        self.payments = self.payments[:p]
        self.interests = self.interests[:p]
        self.nper_t = p
        self.num_of_years_t = p / self.freq
