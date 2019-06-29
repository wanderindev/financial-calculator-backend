from flask import Blueprint

calculators = Blueprint('calculators', __name__)


from .savings import ahorros_para_lograr_meta
from .savings import calculadora_de_ahorros
from .savings import tasa_de_interes_requerida
from .savings import tiempo_para_lograr_meta
from .savings import valor_actual
