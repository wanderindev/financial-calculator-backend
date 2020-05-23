from math import ceil
from numpy_financial import nper, pmt, pv

from .calculator import Calculator


# noinspection PyTypeChecker
class RetirementCalculator(Calculator):
    def __init__(self, **kwargs):
        super(RetirementCalculator, self).__init__(**kwargs)

        self.ret_fund = self.get_float(kwargs.get("ret_fund", 0))
        self.reg_wdr = self.get_float(kwargs.get("reg_wdr", 0))
        self.wdr_when = self.get_int(kwargs.get("wdr_when", 0))
        self.withdrawals = []

    def get_balances_retirements(self):
        balances = []

        for x in self.periods:
            bal = (
                self.ret_fund
                - sum(self.withdrawals[:x])
                + sum(self.interests[:x])
            )

            if bal < 0:
                balances.append(0)
            else:
                balances.append(
                    self.ret_fund
                    - sum(self.withdrawals[:x])
                    + sum(self.interests[:x])
                )
        self.balances = balances

        return balances

    def get_interests_retirements(self):
        _rate = self.rate / (100 * self.freq)
        interests = [
            round(
                (self.ret_fund - self.withdrawals[0]) * _rate
                if self.wdr_when
                else self.ret_fund * _rate,
                2,
            )
        ]

        for x in self.periods[1:]:
            if self.wdr_when:
                cur_bal = round(
                    (
                        self.ret_fund
                        - sum(self.withdrawals[:x])
                        + sum(interests[:x])
                    ),
                    2,
                )

                if cur_bal < 0:
                    interest = 0
                    self.withdrawals[x - 1] = self.withdrawals[x - 1] + cur_bal
                else:
                    interest = round(cur_bal * _rate, 2)
            else:
                cur_bal = (
                    self.ret_fund
                    - sum(self.withdrawals[: x - 1])
                    + sum(interests[:x])
                )
                interest = round(cur_bal * _rate, 2)

                if cur_bal + interest < self.withdrawals[x - 1]:
                    self.withdrawals[x - 1] = cur_bal + interest

            interests.append(interest)

        self.interests = interests

        return interests

    def get_nper_retirements(self):
        _nper = ceil(
            nper(
                self.rate / (100 * self.freq),
                -self.reg_wdr,
                self.ret_fund,
                when=self.wdr_when,
            )
        )

        self.num_of_years = round(_nper / self.freq, 2)
        self.periods = self.get_periods()
        self.periods_a = self.get_periods_a()
        self.periods_m = self.get_periods_m()

        return _nper

    def get_reg_wdr(self):
        self.reg_wdr = round(
            -pmt(
                self.rate / (100 * self.freq),
                self.freq * self.num_of_years,
                self.ret_fund,
                when=self.wdr_when,
            ),
            2,
        )

        return self.reg_wdr

    def get_ret_fund(self):
        self.ret_fund = -round(
            pv(
                self.rate / (100 * self.freq),
                self.freq * self.num_of_years,
                self.reg_wdr,
                when=self.wdr_when,
            ),
            2,
        )

        return self.ret_fund

    def get_withdrawals(self):
        self.withdrawals = [self.reg_wdr for _ in self.periods]

        return self.withdrawals
