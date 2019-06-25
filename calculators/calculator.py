from math import ceil


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

    # noinspection PyTypeChecker
    def get_deposits(self):
        periods = self.get_periods()
        reg_deps = self.get_reg_deps(periods)
        extra_deps = self.get_extra_deps(periods)

        return [round(reg_deps[x - 1] + extra_deps[x - 1], 2) for x in periods]

    def get_extra_deps(self, periods):
        extra_dep_p = []

        if self.extra_dep:
            extra_dep_p.append(self.extra_dep_start)
            if self.extra_dep_f:
                for x in periods[self.extra_dep_start + 1:]:
                    if not (x - self.extra_dep_start) \
                           % (12 / self.extra_dep_f):
                        extra_dep_p.append(x)

        return [self.extra_dep if x in extra_dep_p else 0 for x in periods]

    @staticmethod
    def get_int(val):
        return int(str(val).replace(',', ''))

    @staticmethod
    def get_float(val):
        return float(str(val).replace(',', ''))

    def get_periods(self):
        return [x + 1 for x in range(ceil(self.freq * self.num_of_years))], \
               [x + 1 for x in range(ceil(12 * self.num_of_years))], \
               [x + 1 for x in range(ceil(1 * self.num_of_years))]

    def get_reg_deps(self, periods):
        reg_deps = [self.reg_dep for _ in periods]
        reg_deps[0] = reg_deps[0] + self.ini_dep

        return reg_deps

    # noinspection PyTypeChecker
    def get_saving_balances(self):
        periods = self.get_periods()
        deposits = self.get_deposits()

        balance = 0 if self.dep_when else self.ini_dep
        balances = []

        interests = []
        agg_interest = 0
        agg_interests = []

        agg_deposit = 0
        agg_deposits = []

        for x in periods:
            if self.dep_when:
                interest = round(
                    (balance + deposits[x - 1]) * self.rate
                    / (100 * self.freq), 2)
            else:
                interest = round(balance * self.rate / (100 * self.freq), 2)

            agg_interest += interest
            agg_deposit += deposits[x - 1]
            interests.append(interest)
            agg_interests.append(agg_interest)
            agg_deposits.append(agg_deposit)
            balance = sum(deposits[:x]) + sum(interests[:x])
            balances.append(balance)

        return interests, agg_interests, agg_deposits, balances

    def get_time_scale(self, freq):
        for item in self.freq_items:
            if item[1] == freq:
                return item[0], item[2]
