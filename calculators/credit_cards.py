from flask import jsonify, request

from .calculator import Calculator
from .calculators import calculators
from config import HEADERS
from .utils import aggregate, format_tables

@calculators.route('/tasa-de-interes-real-tc', methods=['POST'])
def tasa_de_interes_real_tc():
    calculator = Calculator(**request.get_json())

    rate = calculator.get_rate_cc()

    return jsonify({
        'rate': rate
    }), 200, HEADERS