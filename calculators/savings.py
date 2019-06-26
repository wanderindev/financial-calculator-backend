from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators

HEADERS = {'Content-Type': 'application/json'}


@calculators.route('/calculadora-de-ahorros', methods=['POST'])
def calculadora_de_ahorros():
    data = request.get_json()
    calculator = Calculator(**data)

    time_scale = calculator.time_scale
    periods, _, _ = calculator.get_periods()
    deposits, a_deposits = calculator.get_deposits()
    interests, a_interests, balances = calculator.get_savings_ints_and_bals()
    table, table_m, table_a = calculator.get_savings_tables()

    return jsonify({
        'time_scale': time_scale,
        'total_dep': sum(deposits),
        'total_int': sum(interests),
        'fin_bal': balances[-1],
        'periods': periods,
        'agg_deposits': a_deposits,
        'agg_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS
