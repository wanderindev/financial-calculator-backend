from flask import Blueprint

calculators = Blueprint('calculators', __name__)

from .calculadora_de_ahorros import calculadora_de_ahorros
