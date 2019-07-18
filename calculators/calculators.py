from flask import Blueprint

calculators = Blueprint('calculators', __name__)


from .savings import ahorros_para_lograr_meta
from .savings import calculadora_de_ahorros
from .savings import tasa_de_interes_requerida
from .savings import tiempo_para_lograr_meta
from .savings import valor_actual
from .loans import calculadora_de_prestamos
from .loans import tasa_de_interes_real_p
from .retirements import fondo_para_retiros
from .retirements import duracion_de_fondos
from .retirements import retiros_para_agotar_fondos
from .credit_cards import tasa_de_interes_real_tc
from .credit_cards import tarjeta_de_credito
