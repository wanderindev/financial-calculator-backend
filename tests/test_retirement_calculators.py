import json
import unittest
from tests.base_test import BaseTest
from tests.retirement_constants import (
    DURACION_DE_FONDO_JSON_0,
    DURACION_DE_FONDO_JSON_1,
    DURACION_DE_FONDO_RESULT_0,
    DURACION_DE_FONDO_RESULT_1,
    FONDO_PARA_RETIRO_JSON_0,
    FONDO_PARA_RETIRO_JSON_1,
    FONDO_PARA_RETIRO_RESULT_0,
    FONDO_PARA_RETIRO_RESULT_1,
    RETIRO_PARA_FONDO_JSON_0,
    RETIRO_PARA_FONDO_JSON_1,
    RETIRO_PARA_FONDO_RESULT_0,
    RETIRO_PARA_FONDO_RESULT_1,
)


class TestRetirementCalculator(BaseTest):
    """Test all endpoints for the retirement calculator"""

    def setUp(self):
        super(TestRetirementCalculator, self).setUp()
        with self.app_context:
            pass

    def test_fund_duration_end(self):
        """
        Test the endpoint for the fund duration calculator when withdrawals
        are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/duracion-de-fondos",
                data=json.dumps(DURACION_DE_FONDO_JSON_0),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, DURACION_DE_FONDO_RESULT_0)

    def test_fund_duration_start(self):
        """
        Test the endpoint for the fund duration calculator when withdrawals
        are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/duracion-de-fondos",
                data=json.dumps(DURACION_DE_FONDO_JSON_1),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, DURACION_DE_FONDO_RESULT_1)

    def test_total_fund_end(self):
        """
        Test the endpoint for the total fund calculator when withdrawals
        are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/fondo-para-retiros",
                data=json.dumps(FONDO_PARA_RETIRO_JSON_0),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, FONDO_PARA_RETIRO_RESULT_0)

    def test_total_fund_start(self):
        """
        Test the endpoint for the total fund calculator when withdrawals
        are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/fondo-para-retiros",
                data=json.dumps(FONDO_PARA_RETIRO_JSON_1),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, FONDO_PARA_RETIRO_RESULT_1)

    def test_fund_withdrawal_end(self):
        """
        Test the endpoint for the fund withdrawal calculator when withdrawals
        are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/retiros-para-agotar-fondos",
                data=json.dumps(RETIRO_PARA_FONDO_JSON_0),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, RETIRO_PARA_FONDO_RESULT_0)

    def test_fund_withdrawal_start(self):
        """
        Test the endpoint for the fund withdrawal calculator when withdrawals
        are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/retiros-para-agotar-fondos",
                data=json.dumps(RETIRO_PARA_FONDO_JSON_1),
                headers=TestRetirementCalculator.request_headers,
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, RETIRO_PARA_FONDO_RESULT_1)


if __name__ == "__main__":
    unittest.main()
