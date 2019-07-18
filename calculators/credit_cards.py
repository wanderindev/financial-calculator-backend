from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators
from config import HEADERS
from .utils import aggregate, format_tables


@calculators.route('/tarjeta-pago-fijo', methods=['POST'])
@calculators.route('/tarjeta-pago-minimo', methods=['POST'])
def tarjeta_de_credito():
    calculator = Calculator(**request.get_json())

    time_scale = calculator.time_scale
    first_p = calculator.get_payment_cc()
    periods = calculator.periods
    nper = periods[-1]
    num_of_years = nper / 12
    payments = calculator.payments
    a_payments = aggregate(payments, periods)
    interests = calculator.interests
    a_interests = aggregate(interests, periods)
    balances = calculator.balances
    table = format_tables(calculator, 1, 'cc')
    table_m = format_tables(calculator, calculator.freq / 12, 'cc')
    table_a = format_tables(calculator, calculator.freq / 1, 'cc')

    return jsonify({
        'time_scale': time_scale,
        'first_p': first_p,
        'total_pmt': sum(payments),
        'total_int': sum(interests),
        'total_prin': calculator.cc_debt,
        'nper': nper,
        'num_of_years': num_of_years,
        'periods': periods,
        'a_payments': a_payments,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS


@calculators.route('/tasa-de-interes-real-tc', methods=['POST'])
def tasa_de_interes_real_tc():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_rate_cc()

    return jsonify({
        'rate': rate
    }), 200, HEADERS
