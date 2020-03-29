from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators
from config import HEADERS
from .utils import aggregate, format_tables


@calculators.route("/calculadora-de-prestamos", methods=["POST"])
def calculadora_de_prestamos():
    calculator = Calculator(**request.get_json())

    time_scale = calculator.time_scale
    reg_pmt = calculator.get_reg_pmt()
    calculator.get_payments()
    periods = calculator.periods
    interests = calculator.interests
    a_interests = aggregate(interests, periods)
    balances = calculator.balances
    payments = calculator.payments
    payments_e = calculator.payments_e
    payments_r = calculator.payments_r
    a_payments = aggregate(payments, periods)
    num_of_years = calculator.num_of_years
    num_of_years_t = calculator.num_of_years_t
    nper = num_of_years * calculator.freq
    nper_t = calculator.nper_t
    total_pmt = nper * reg_pmt
    total_int = total_pmt - calculator.loan
    table = format_tables(calculator, 1, "loans")
    table_m = format_tables(calculator, calculator.freq / 12, "loans")
    table_a = format_tables(calculator, calculator.freq / 1, "loans")

    return (
        jsonify(
            {
                "time_scale": time_scale,
                "total_pmt": total_pmt,
                "total_int": total_int,
                "num_of_years": num_of_years,
                "num_of_years_t": num_of_years_t,
                "years_saved": num_of_years - num_of_years_t,
                "cash_saved": total_pmt - sum(payments),
                "nper": nper,
                "nper_t": nper_t,
                "total_pmt_t": sum(payments),
                "total_int_t": sum(interests),
                "total_prin": calculator.loan,
                "total_prin_t": calculator.loan,
                "reg_pmt": reg_pmt,
                "periods": periods,
                "a_payments": a_payments,
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


@calculators.route("/tasa-de-interes-real-de-prestamo", methods=["POST"])
def tasa_de_interes_real_p():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_rate_loans()

    return jsonify({"rate": rate}), 200, HEADERS


@calculators.route("/tiempo-para-cancelar-prestamo", methods=["POST"])
def tiempo_para_pagar():
    calculator = Calculator(**request.get_json())

    nper = calculator.get_nper_loans()
    num_of_years = calculator.num_of_years
    time_scale = calculator.time_scale
    periods = calculator.get_periods()
    payments, payments_r, payments_e = calculator.get_payments()
    a_payments = aggregate(payments, periods)
    interests = calculator.interests
    a_interests = aggregate(interests, periods)
    balances = calculator.balances
    table = format_tables(calculator, 1, "loans")
    table_m = format_tables(calculator, calculator.freq / 12, "loans")
    table_a = format_tables(calculator, calculator.freq / 1, "loans")

    return (
        jsonify(
            {
                "nper": nper,
                "num_of_years": num_of_years,
                "time_scale": time_scale,
                "total_pmt": sum(payments),
                "total_int": sum(interests),
                "total_prin": calculator.loan,
                "periods": periods,
                "a_payments": a_payments,
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
