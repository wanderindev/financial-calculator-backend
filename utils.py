from math import ceil


def get_balances(periods, deposits, ini_dep, rate, freq,
                 dep_when):
    balance = 0 if not dep_when else ini_dep
    balances = []

    interests = []
    agg_interest = 0
    agg_interests = []

    agg_deposit = 0
    agg_deposits = []

    for x in periods:
        if dep_when:
            interest = round(balance * rate / (100 * freq), 2)
        else:
            interest = round((balance + deposits[x - 1]) * rate / (100 * freq),
                             2)

        agg_interest += interest
        agg_deposit += deposits[x - 1]
        interests.append(interest)
        agg_interests.append(agg_interest)
        agg_deposits.append(agg_deposit)
        balance = sum(deposits[:x]) + sum(interests[:x])
        balances.append(balance)

    return interests, agg_interests, agg_deposits, balances


def get_deposits(ini_dep, reg_dep, extra_dep, extra_dep_start, extra_dep_f,
                 periods):
    # Build a list of regular deposits.
    reg_deps = [reg_dep for _ in periods]
    reg_deps[0] = reg_deps[0] + ini_dep

    # Build a list of extraordinary deposits.
    extra_dep_p = []
    if extra_dep:
        extra_dep_p.append(extra_dep_start)
        if extra_dep_f:
            for x in periods[extra_dep_start + 1:]:
                if not (x - extra_dep_start) % (12 / extra_dep_f):
                    extra_dep_p.append(x)

    extra_deps = [extra_dep if x in extra_dep_p else 0 for x in periods]

    # Return consolidated deposit list
    return [round(reg_deps[x - 1] + extra_deps[x - 1], 2) for x in
            periods], reg_deps, extra_deps


def get_periods(freq, num_of_years):
    return [x + 1 for x in range(ceil(freq * num_of_years))], \
           [x + 1 for x in range(ceil(12 * num_of_years))], \
           [x + 1 for x in range(ceil(1 * num_of_years))]


def get_table_m(periods_m, deposits, interests, balances, freq):
    if freq >= 12:
        return [dict(p='{:0,.0f}'.format(periods_m[x - 1]),
                     d='{:0,.2f}'.format(sum(deposits[
                                             int((x - 1) * freq / 12):int(
                                                 x * freq / 12)])),
                     i='{:0,.2f}'.format(sum(interests[
                                             int((x - 1) * freq / 12):int(
                                                 x * freq / 12)])),
                     b='{:0,.2f}'.format(balances[int(x * freq / 12) - 1])) for
                x in periods_m]
    return None


def get_table_a(periods_a, deposits, interests, balances, freq):
    return [dict(p='{:0,.0f}'.format(periods_a[x - 1]),
                 d='{:0,.2f}'.format(sum(deposits[(x - 1) * freq:x * freq])),
                 i='{:0,.2f}'.format(sum(interests[(x - 1) * freq:x * freq])),
                 b='{:0,.2f}'.format(balances[x * freq - 1])) for x in
            periods_a]


def get_time_scale(freq):
    freq_items = [(u'Año', 1, 10), ('Semestre', 2, 10),
                  ('Cuatrimestre', 3, 12), ('Bimestre', 6, 12),
                  ('Mes', 12, 12), ('Quincena', 24, 12), ('Bi-semana', 26, 13),
                  ('Semana', 52, 13),
                  (u'Día', 364, 15)]

    for item in freq_items:
        if item[1] == freq:
            return item[0], item[2]


def parse_args(kwargs):
    for k, v in kwargs.items():
        if not v:
            v = 0

        if k in ['freq', 'extra_dep_f', 'dep_when']:
            kwargs[k] = int(v)
        elif k in ['extra_dep_start']:
            kwargs[k] = int(str(v).replace(',', ''))
        elif k in ['ini_dep', 'reg_dep', 'num_of_years', 'rate', 'extra_dep']:
            kwargs[k] = float(str(v).replace(',', ''))

    kwargs['time_scale'] = get_time_scale(kwargs['freq'])

    return kwargs
