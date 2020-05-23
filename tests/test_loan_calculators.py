import json
import unittest
from tests.base_test import BaseTest
from tests.loan_constants import (
    INTERES_JSON_0,
    INTERES_JSON_1,
    INTERES_RESULT_0,
    INTERES_RESULT_1,
    PRESTAMOS_JSON_0,
    PRESTAMOS_JSON_1,
    PRESTAMOS_RESULT_0,
    PRESTAMOS_RESULT_1,
    TIEMPO_PAGAR_JSON_0,
    TIEMPO_PAGAR_JSON_1,
    TIEMPO_PAGAR_RESULT_0,
    TIEMPO_PAGAR_RESULT_1,
)


class TestLoanCalculator(BaseTest):
    """Test all endpoints for the loan calculator"""

    def setUp(self):
        super(TestLoanCalculator, self).setUp()
        with self.app_context:
            pass

    def test_loan_end(self):
        """
        Test the endpoint for the loans calculator when payments are made
        at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/calculadora-de-prestamos",
                data=json.dumps(PRESTAMOS_JSON_0),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, PRESTAMOS_RESULT_0)

    def test_loan_start(self):
        """
        Test the endpoint for the loans calculator when payments are made
        at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/calculadora-de-prestamos",
                data=json.dumps(PRESTAMOS_JSON_1),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, PRESTAMOS_RESULT_1)

    def test_interest_end(self):
        """
        Test the endpoint for the loan interest calculator when payments
        are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tasa-de-interes-real-de-prestamo",
                data=json.dumps(INTERES_JSON_0),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertLess(
                abs(data["rate"] - INTERES_RESULT_0["rate"]), 0.001
            )

    def test_interest_start(self):
        """
        Test the endpoint for the loan interest calculator when payments
        are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tasa-de-interes-real-de-prestamo",
                data=json.dumps(INTERES_JSON_1),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertLess(
                abs(data["rate"] - INTERES_RESULT_1["rate"]), 0.001
            )

    def test_loan_time_to_pay_end(self):
        """
        Test the endpoint for the time to pay loan when payments are made
        at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tiempo-para-cancelar-prestamo",
                data=json.dumps(TIEMPO_PAGAR_JSON_0),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, TIEMPO_PAGAR_RESULT_0)

    def test_loan_time_to_pay_start(self):
        """
        Test the endpoint for the time to pay loan when payments are made
        at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tiempo-para-cancelar-prestamo",
                data=json.dumps(TIEMPO_PAGAR_JSON_1),
                headers=TestLoanCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, TIEMPO_PAGAR_RESULT_1)


if __name__ == "__main__":
    unittest.main()
