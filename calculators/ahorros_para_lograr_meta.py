from flask import jsonify, request

from .calculators import calculators
from utils import fut_val, get_balances, get_deposits, \
    get_periods, get_table, get_table_a, get_table_m, \
    HEADERS, parse_data, payment, pres_val


@calculators.route('/ahorros-para-lograr-meta', methods=['POST'])
def ahorros_para_lograr_meta():
    data = parse_data(request.get_json())

    ini_dep = data.get('ini_dep')
    fin_bal = data.get('fin_bal')
    freq = data.get('freq')
    num_of_years = data.get('num_of_years')
    rate = data.get('rate')
    dep_when = data.get('dep_when')
    time_scale, rows_per_page = data.get('time_scale')

    periods, periods_m, periods_a = get_periods(freq, num_of_years)

    fv = fut_val(rate / (100 * freq), freq * num_of_years, ini_dep)

    reg_dep = -1 * payment(rate / (100 * freq),
                           freq * num_of_years,
                           0,
                           fin_bal + fv,
                           dep_when)

    deposits, reg_deps, extra_deps = get_deposits(ini_dep,
                                                  reg_dep,
                                                  0,
                                                  0,
                                                  0,
                                                  periods)

    interests, agg_interests, agg_deposits, balances = get_balances(
        periods, deposits, ini_dep, rate, freq, dep_when)

    return jsonify({
        'reg_dep': reg_dep,
        'time_scale': time_scale,
        'total_dep': sum(deposits),
        'total_int': sum(interests),
        'fin_bal': balances[-1],
        'periods': periods,
        'agg_deposits': agg_deposits,
        'agg_interests': agg_interests,
        'balances': balances,
        'table': get_table(periods, deposits, interests, balances),
        'table_m': get_table_m(periods_m, deposits, interests, balances,
                               freq),
        'table_a': get_table_a(periods_a, deposits, interests, balances,
                               freq)
    }), 200, HEADERS
