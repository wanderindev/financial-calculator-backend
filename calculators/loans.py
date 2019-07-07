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
    interests = calculator.interests
    a_interests = aggregate(interests, periods)
    balances = calculator.balances
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


@calculators.route('/tasa-de-interes-real', methods=['POST'])
def tasa_de_interes_real():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_rate_loans()

    return jsonify({
        'rate': rate
    }), 200, HEADERS


@calculators.route('/tiempo-para-pagar', methods=['POST'])
def tiempo_para_pagar():
    calculator = Calculator(**request.get_json())

    nper = calculator.get_nper_loans()
    time_scale = calculator.time_scale
    periods = calculator.get_periods()
    payments, payments_r, payments_e = calculator.get_payments()
    a_payments = aggregate(payments, periods)
    interests = calculator.interests
    a_interests = aggregate(interests, periods)
    balances = calculator.balances
    table = format_tables(calculator, 1, 'loans')
    table_m = format_tables(calculator, calculator.freq / 12, 'loans')
    table_a = format_tables(calculator, calculator.freq / 1, 'loans')

    return jsonify({
        'nper': nper,
        'time_scale': time_scale,
        'total_pmt': sum(payments),
        'total_int': sum(interests),
        'total_prin': calculator.loan,
        'periods': periods,
        'a_payments': a_payments,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS
