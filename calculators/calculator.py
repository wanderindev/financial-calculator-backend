from math import ceil
from numpy import fv, nper, pmt, pv, rate


# noinspection PyTypeChecker
class Calculator:
    freq_items = [
        (u'Año', 1, 10),
        ('Semestre', 2, 10),
        ('Cuatrimestre', 3, 12),
        ('Bimestre', 6, 12),
        ('Mes', 12, 12),
        ('Quincena', 24, 12),
        ('Bi-semana', 26, 13),
        ('Semana', 52, 13),
        (u'Día', 364, 15)
    ]

    def __init__(self, **kwargs):
        self.ini_dep = self.get_float(kwargs.get('ini_dep', 0))
        self.reg_dep = self.get_float(kwargs.get('reg_dep', 0))
        self.freq = self.get_int(kwargs.get('freq', 0))
        self.num_of_years = self.get_float(kwargs.get('num_of_years', 0))
        self.rate = self.get_float(kwargs.get('rate', 0))
        self.extra_dep = self.get_float(kwargs.get('extra_dep', 0))
        self.extra_dep_start = self.get_int(kwargs.get('extra_dep_start', 0))
        self.extra_dep_f = self.get_int(kwargs.get('extra_dep_f', 0))
        self.dep_when = self.get_int(kwargs.get('dep_when', 0))
        self.time_scale, rows_per_page = self.get_time_scale(self.freq)
        self.fin_bal = self.get_float(kwargs.get('fin_bal', 0))
        self.periods = self.get_periods()
        self.periods_a = self.get_periods_a()
        self.periods_m = self.get_periods_m()
        self.deposits = []
        self.interests = []
        self.balances = []

    def get_balances_savings(self):
        balances = []

        for x in self.periods:
            balances.append(sum(self.deposits[:x]) + sum(self.interests[:x]))

        self.balances = balances

        return self.balances

    def get_deposits(self):
        reg_deps = self.get_deposits_r()
        extra_deps = self.get_deposits_e()

        self.deposits = [round(reg_deps[x-1] + extra_deps[x-1], 2)
                         for x in self.periods]

        return self.deposits

    def get_deposits_e(self):
        extra_dep_p = []

        if self.extra_dep:
            extra_dep_p.append(self.extra_dep_start)
            if self.extra_dep_f:
                for x in self.periods[self.extra_dep_start + 1:]:
                    if not (x - self.extra_dep_start) \
                           % (12 / self.extra_dep_f):
                        extra_dep_p.append(x)

        return [self.extra_dep if x in extra_dep_p else 0
                for x in self.periods]

    def get_deposits_r(self):
        reg_deps = [self.reg_dep for _ in self.periods]
        reg_deps[0] += self.ini_dep

        return reg_deps

    @staticmethod
    def get_float(val):
        return float(str(val).replace(',', ''))

    @staticmethod
    def get_int(val):
        return int(str(val).replace(',', ''))

    def get_interests_savings(self):
        _rate = self.rate / (100 * self.freq)
        interests = [round(self.deposits[0] * _rate
                           if self.dep_when else self.ini_dep * _rate, 2)]

        for x in self.periods[1:]:
            if self.dep_when:
                interest = round((sum(self.deposits[:x]) + sum(interests[:x]))
                                 * _rate, 2)
            else:
                interest = round((sum(self.deposits[:x-1]) +
                                  sum(interests[:x-1])) * _rate, 2)

            interests.append(interest)

        self.interests = interests

        return self.interests

    def get_nper_savings(self):
        _nper = ceil(nper(self.rate / (100 * self.freq),
                          -self.reg_dep,
                          -self.ini_dep,
                          self.fin_bal,
                          self.dep_when))

        self.num_of_years = round(_nper / self.freq, 2)
        self.periods = self.get_periods()
        self.periods_a = self.get_periods_a()
        self.periods_m = self.get_periods_m()

        return _nper

    def get_periods(self):
        return [x + 1 for x in range(ceil(self.freq * self.num_of_years))]

    def get_periods_a(self):
        return [x + 1 for x in range(ceil(1 * self.num_of_years))]

    def get_periods_m(self):
        return [x + 1 for x in range(ceil(12 * self.num_of_years))]

    def get_pres_val(self):
        return pv(self.rate / (100 * self.freq),
                  self.freq * self.num_of_years,
                  0,
                  self.fin_bal,
                  self.dep_when)

    def get_reg_dep_savings(self):
        _fv = fv(self.rate / (100 * self.freq),
                 self.freq * self.num_of_years,
                 0,
                 self.ini_dep,
                 self.dep_when) + self.fin_bal

        self.reg_dep = -pmt(self.rate / (100 * self.freq),
                            self.freq * self.num_of_years,
                            0,
                            _fv,
                            self.dep_when)

        return self.reg_dep

    def get_rate_savings(self):
        return rate(self.freq * self.num_of_years,
                    -self.reg_dep,
                    -self.ini_dep,
                    self.fin_bal,
                    self.dep_when) * self.freq * 100

    def get_time_scale(self, freq):
        for item in self.freq_items:
            if item[1] == freq:
                return item[0], item[2]
