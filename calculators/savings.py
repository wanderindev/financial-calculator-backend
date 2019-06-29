from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators

HEADERS = {'Content-Type': 'application/json'}


@calculators.route('/ahorros-para-lograr-meta', methods=['POST'])
def ahorros_para_lograr_meta():
    calculator = Calculator(**request.get_json())

    reg_dep = calculator.get_reg_dep()
    time_scale = calculator.time_scale
    periods, _, _ = calculator.get_periods()
    deposits, a_deposits = calculator.get_deposits()
    interests, a_interests, balances = calculator.get_savings_ints_and_bals()
    table, table_m, table_a = calculator.get_savings_tables()

    return jsonify({
        'reg_dep': reg_dep,
        'time_scale': time_scale,
        'total_dep': sum(deposits),
        'total_int': sum(interests),
        'fin_bal': balances[-1],
        'periods': periods,
        'a_deposits': a_deposits,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS


@calculators.route('/calculadora-de-ahorros', methods=['POST'])
def calculadora_de_ahorros():
    calculator = Calculator(**request.get_json())

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
        'a_deposits': a_deposits,
        'a_interests': a_interests,
        'balances': balances,
        'table': table,
        'table_m': table_m,
        'table_a': table_a
    }), 200, HEADERS


@calculators.route('/tasa-de-interes-requerida', methods=['POST'])
def tasa_de_interes_requerida():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_savings_rate()

    return jsonify({
        'rate': rate
    }), 200, HEADERS


@calculators.route('/tiempo-para-lograr-meta', methods=['POST'])
def tiempo_para_lograr_meta():
    calculator = Calculator(**request.get_json())

    nper = calculator.get_nper()
    time_scale = calculator.time_scale
    periods, _, _ = calculator.get_periods()
    deposits, a_deposits = calculator.get_deposits()
    interests, a_interests, balances = calculator.get_savings_ints_and_bals()
    table, table_m, table_a = calculator.get_savings_tables()

    return jsonify({
        'nper': nper,
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


@calculators.route('/valor-actual', methods=['POST'])
def valor_actual():
    calculator = Calculator(**request.get_json())

    pv = -calculator.get_pres_val()

    return jsonify({
        'pv': pv
    }), 200, HEADERS
