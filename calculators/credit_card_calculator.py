from .calculator import Calculator


# noinspection PyTypeChecker
class CreditCardCalculator(Calculator):
    def __init__(self, **kwargs):
        super(CreditCardCalculator, self).__init__(**kwargs)

        self.cc_debt = self.get_float(kwargs.get("cc_debt", 0))
        self.add_c = self.get_float(kwargs.get("add_c", 0))
        self.min_p_perc = self.get_float(kwargs.get("min_p_perc", 0))
        self.min_p = self.get_float(kwargs.get("min_p", 0))
        self.fix_p = self.get_float(kwargs.get("fix_p", 0))
        self.payments = []
        self.payments_p = []

    def get_payment_cc(self) -> float:
        _rate = self.rate / (100 * self.freq)
        _min_p_perc = self.min_p_perc / 100
        _min_p = self.min_p
        _fix_p = self.fix_p
        b = self.cc_debt
        per = 0

        while b > 0:
            i = b * _rate
            p = max(b * _min_p_perc, _min_p, _fix_p)

            if b + i < p:
                p = b + i

            b += i - p
            per += 1

            self.periods.append(per)
            self.payments.append(p)
            self.payments_p.append(p - i)
            self.interests.append(i)
            self.balances.append(b)

        return self.payments[0]

    def get_rate_cc(self) -> float:
        return self.rate + self.add_c * 1200 / self.cc_debt
