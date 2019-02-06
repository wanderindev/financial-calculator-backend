from flask import Flask

from config import config
from utils import get_balances, get_deposits, get_periods, get_table_a, \
    get_table_m, parse_args


def create_app(config_name):
    """
    App factory for the creation of a Flask app.
    :param config_name: The key for the config setting to use
    :type config_name: str
    :return: A Flask app instance
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    @app.route('/calc1')
    def calc1(kwargs):
        data = parse_args(kwargs)

        ini_dep = data.get('ini_dep')
        reg_dep = data.get('reg_dep')
        freq = data.get('freq')
        num_of_years = data.get('num_of_years')
        rate = data.get('rate')
        extra_dep = data.get('extra_dep')
        extra_dep_start = data.get('extra_dep_start')
        extra_dep_f = data.get('extra_dep_f')
        dep_when = data.get('dep_when')
        time_scale, rows_per_page = data.get('time_scale')

        periods, periods_m, periods_a = get_periods(freq, num_of_years)
        deposits, reg_deps, extra_deps = get_deposits(ini_dep, reg_dep,
                                                      extra_dep,
                                                      extra_dep_start,
                                                      extra_dep_f, periods)
        interests, agg_interests, agg_deposits, balances = get_balances(
            periods, deposits, ini_dep, rate, freq, dep_when)

        return {
            'time_scale': time_scale,
            'other_rb': dict(visible=freq > 1,
                             label=time_scale if freq > 1 else '',
                             r=rows_per_page),
            'm_rb': dict(visible=freq > 12, label='Mes' if freq > 12 else '',
                         r=12),
            'total_dep': sum(deposits),
            'total_int': sum(interests),
            'fin_bal': balances[-1],
            'periods': periods,
            'agg_deposits': agg_deposits,
            'agg_interests': agg_interests,
            'balances': balances,
            'table': [dict(p='{:0,.0f}'.format(periods[x - 1]),
                           d='{:0,.2f}'.format(deposits[x - 1]),
                           i='{:0,.2f}'.format(interests[x - 1]),
                           b='{:0,.2f}'.format(balances[x - 1])) for x in
                      periods],
            'table_m': get_table_m(periods_m, deposits, interests, balances,
                                   freq),
            'table_a': get_table_a(periods_a, deposits, interests, balances,
                                   freq)
        }

    return app
