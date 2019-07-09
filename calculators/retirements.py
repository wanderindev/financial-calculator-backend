from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators
from config import HEADERS
from .utils import aggregate, format_tables


@calculators.route('/duracion-de-fondos', methods=['POST'])
def duracion_de_fondos():
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


@calculators.route('/fondo-para-retiros', methods=['POST'])
def fondo_para_retiros():
    calculator = Calculator(**request.get_json())

    time_scale = calculator.time_scale
    ret_fund = calculator.get_ret_fund()
    periods = calculator.periods
    withdrawals = calculator.get_withdrawals()
    a_withdrawals = aggregate(withdrawals, periods)
    interests = calculator.get_interests_retirements()
    a_interests = aggregate(interests, periods)
    balances = calculator.get_balances_retirements()
    table = format_tables(calculator, 1, 'retirements')
    table_m = format_tables(calculator, calculator.freq / 12, 'retirements')
    table_a = format_tables(calculator, calculator.freq / 1, 'retirements')

    return jsonify({
        'time_scale': time_scale,
        'total_wdr': sum(withdrawals),
        'total_int': sum(interests),
        'ret_fund': ret_fund,
        'periods': periods,
        'a_withdrawals': a_withdrawals,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS


@calculators.route('/retiros-para-agotar-fondos', methods=['POST'])
def retiros_para_agotar_fondos():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_rate_loans()

    return jsonify({
        'rate': rate
    }), 200, HEADERS
