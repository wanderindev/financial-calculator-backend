from flask import Blueprint

calculators = Blueprint('calculators', __name__)

from .calculadora_de_ahorros import calculadora_de_ahorros
from .ahorros_para_lograr_meta import ahorros_para_lograr_meta