from flask import jsonify, request

from calculators.retirement_calculator import RetirementCalculator
from config import HEADERS
from resources.calculators import calculators
from resources.utils import aggregate, format_tables


@calculators.route("/duracion-de-fondos", methods=["POST"])
def duracion_de_fondos():
    calculator = RetirementCalculator(**request.get_json())

    nper = calculator.get_nper_retirements()
    num_of_years = calculator.num_of_years
    ret_fund = calculator.ret_fund
    time_scale = calculator.time_scale
    periods = calculator.get_periods()
    calculator.get_withdrawals()
    interests = calculator.get_interests_retirements()
    withdrawals = calculator.withdrawals
    a_withdrawals = aggregate(withdrawals, periods)
    a_interests = aggregate(interests, periods)
    balances = calculator.get_balances_retirements()
    table = format_tables(calculator, 1, "retirements")
    table_m = format_tables(calculator, calculator.freq / 12, "retirements")
    table_a = format_tables(calculator, calculator.freq / 1, "retirements")

    return (
        jsonify(
            {
                "nper": nper,
                "num_of_years": num_of_years,
                "time_scale": time_scale,
                "total_wdr": sum(withdrawals),
                "total_int": sum(interests),
                "ret_fund": ret_fund,
                "periods": periods,
                "a_withdrawals": a_withdrawals,
                "a_interests": a_interests,
                "balances": balances,
                "table": table,
                "table_m": table_m,
                "table_a": table_a,
            }
        ),
        200,
        HEADERS,
    )


@calculators.route("/fondo-para-retiros", methods=["POST"])
def fondo_para_retiros():
    calculator = RetirementCalculator(**request.get_json())

    time_scale = calculator.time_scale
    ret_fund = calculator.get_ret_fund()
    periods = calculator.periods
    calculator.get_withdrawals()
    interests = calculator.get_interests_retirements()
    withdrawals = calculator.withdrawals
    a_withdrawals = aggregate(withdrawals, periods)
    a_interests = aggregate(interests, periods)
    balances = calculator.get_balances_retirements()
    table = format_tables(calculator, 1, "retirements")
    table_m = format_tables(calculator, calculator.freq / 12, "retirements")
    table_a = format_tables(calculator, calculator.freq / 1, "retirements")

    return (
        jsonify(
            {
                "time_scale": time_scale,
                "total_wdr": sum(withdrawals),
                "total_int": sum(interests),
                "ret_fund": ret_fund,
                "periods": periods,
                "a_withdrawals": a_withdrawals,
                "a_interests": a_interests,
                "balances": balances,
                "table": table,
                "table_m": table_m,
                "table_a": table_a,
            }
        ),
        200,
        HEADERS,
    )


@calculators.route("/retiros-para-agotar-fondos", methods=["POST"])
def retiros_para_agotar_fondos():
    calculator = RetirementCalculator(**request.get_json())

    time_scale = calculator.time_scale
    reg_wdr = calculator.get_reg_wdr()
    ret_fund = calculator.ret_fund
    periods = calculator.periods
    calculator.get_withdrawals()
    interests = calculator.get_interests_retirements()
    withdrawals = calculator.withdrawals
    a_withdrawals = aggregate(withdrawals, periods)
    a_interests = aggregate(interests, periods)
    balances = calculator.get_balances_retirements()
    table = format_tables(calculator, 1, "retirements")
    table_m = format_tables(calculator, calculator.freq / 12, "retirements")
    table_a = format_tables(calculator, calculator.freq / 1, "retirements")

    return (
        jsonify(
            {
                "time_scale": time_scale,
                "total_wdr": sum(withdrawals),
                "total_int": sum(interests),
                "ret_fund": ret_fund,
                "reg_wdr": reg_wdr,
                "periods": periods,
                "a_withdrawals": a_withdrawals,
                "a_interests": a_interests,
                "balances": balances,
                "table": table,
                "table_m": table_m,
                "table_a": table_a,
            }
        ),
        200,
        HEADERS,
    )
