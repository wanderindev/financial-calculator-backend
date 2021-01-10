import json
import unittest
from tests.test_base import BaseTest
from tests.credit_card_constants import (
    T_INTERES_REAL_JSON,
    T_INTERES_REAL_RESULT,
    T_PAGO_FIJO_JSON,
    T_PAGO_FIJO_RESULT,
    T_PAGO_MINIMO_JSON,
    T_PAGO_MINIMO_RESULT,
)


class TestCreditCardCalculator(BaseTest):
    """Test all endpoints for the credit card calculator"""

    def setUp(self):
        super(TestCreditCardCalculator, self).setUp()
        with self.app_context:
            pass

    def test_credit_card_fixed_p(self):
        """Test the endpoint for the credit card fixed payment calculator"""
        with self.client as c:
            results = c.post(
                "/tarjeta-pago-fijo",
                data=json.dumps(T_PAGO_FIJO_JSON),
                headers=TestCreditCardCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, T_PAGO_FIJO_RESULT)

    def test_credit_card_min_p(self):
        """Test the endpoint for the credit card minimum payment calculator"""
        with self.client as c:
            results = c.post(
                "/tarjeta-pago-minimo",
                data=json.dumps(T_PAGO_MINIMO_JSON),
                headers=TestCreditCardCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, T_PAGO_MINIMO_RESULT)

    def test_credit_card_rate(self):
        """Test the endpoint for the credit card rate calculator"""
        with self.client as c:
            results = c.post(
                "/tasa-de-interes-real-de-tarjeta",
                data=json.dumps(T_INTERES_REAL_JSON),
                headers=TestCreditCardCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, T_INTERES_REAL_RESULT)


if __name__ == "__main__":
    unittest.main()
