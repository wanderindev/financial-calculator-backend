from math import ceil


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

    def get_deposits(self):
        periods, _, _ = self.get_periods()
        reg_deps = self.get_reg_deps(periods)
        extra_deps = self.get_extra_deps(periods)

        deposits = [round(reg_deps[x - 1] + extra_deps[x - 1], 2)
                    for x in periods]
        a_deposits = [round(sum(deposits[:x]), 2) for x in periods]

        return deposits, a_deposits

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

    def get_savings_ints_and_bals(self):
        periods, _, _ = self.get_periods()
        deposits, _ = self.get_deposits()
        balances = []
        interests = []
        rate = self.rate / (100 * self.freq)

        balance = 0 if self.dep_when else self.ini_dep

        for x in periods:
            if self.dep_when:
                interest = round((balance + deposits[x - 1]) * rate, 2)
            else:
                interest = round(balance * rate, 2)

            interests.append(interest)
            balance = sum(deposits[:x]) + sum(interests[:x])
            balances.append(balance)

        a_interests = [round(sum(interests[:x]), 2) for x in periods]

        return interests, a_interests, balances

    def get_periods(self):
        return [x + 1 for x in range(ceil(self.freq * self.num_of_years))], \
               [x + 1 for x in range(ceil(12 * self.num_of_years))], \
               [x + 1 for x in range(ceil(1 * self.num_of_years))]

    def get_reg_deps(self, periods):
        reg_deps = [self.reg_dep for _ in periods]
        reg_deps[0] = reg_deps[0] + self.ini_dep

        return reg_deps

    def get_savings_tables(self):
        periods, periods_m, periods_a = self.get_periods()
        deposits, _ = self.get_deposits()
        interests, _, balances = self.get_savings_ints_and_bals()
        table_m = None

        table = [dict(p='{:0,.0f}'.format(periods[x - 1]),
                      d='{:0,.2f}'.format(deposits[x - 1]),
                      i='{:0,.2f}'.format(interests[x - 1]),
                      b='{:0,.2f}'.format(balances[x - 1]))
                 for x in periods]

        table_a = [dict(p='{:0,.0f}'.format(periods_a[x - 1]),
                        d='{:0,.2f}'.format(
                            sum(deposits[(x - 1)*self.freq:x*self.freq])),
                        i='{:0,.2f}'.format(
                            sum(interests[(x - 1)*self.freq:x*self.freq])),
                        b='{:0,.2f}'.format(balances[x*self.freq-1]))
                   for x in periods_a]

        if self.freq >= 12:
            table_m = [dict(p='{:0,.0f}'.format(periods_m[x - 1]),
                            d='{:0,.2f}'.format(
                                sum(deposits[int((x-1)*self.freq/12):
                                             int(x*self.freq/12)])),
                            i='{:0,.2f}'.format(
                                sum(interests[int((x-1)*self.freq/12):
                                              int(x*self.freq/12)])),
                            b='{:0,.2f}'.format(
                                balances[int(x*self.freq/12)-1]))
                       for x in periods_m]

        return table, table_m, table_a

    def get_time_scale(self, freq):
        for item in self.freq_items:
            if item[1] == freq:
                return item[0], item[2]
