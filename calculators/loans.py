from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators
from config import HEADERS
from .utils import aggregate, format_tables


@calculators.route('/calculadora-de-prestamos', methods=['POST'])
def calculadora_de_prestamos():
    calculator = Calculator(**request.get_json())

    time_scale = calculator.time_scale
    reg_pmt = calculator.get_reg_pmt()
    periods = calculator.periods
    payments, payments_r, payments_e = calculator.get_payments()
    a_payments = aggregate(payments, periods)
    interests = calculator.get_interests_loans()
    a_interests = aggregate(interests, periods)
    balances = calculator.get_balances_loans()
    table = format_tables(calculator, 1, 'loans')
    table_m = format_tables(calculator, calculator.freq / 12, 'loans')
    table_a = format_tables(calculator, calculator.freq / 1, 'loans')

    return jsonify({
        'time_scale': time_scale,
        'total_pmt': sum(payments),
        'total_int': sum(interests),
        'total_prin': calculator.loan,
        'reg_pmt': reg_pmt,
        'periods': periods,
        'a_payments': a_payments,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS
