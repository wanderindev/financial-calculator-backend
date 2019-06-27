from flask import Blueprint

calculators = Blueprint('calculators', __name__)

from .savings import calculadora_de_ahorros
from .savings import ahorros_para_lograr_meta