import json
import unittest
from tests.base_test import BaseTest
from tests.saving_constants import (
    AHORROS_JSON_0,
    AHORROS_JSON_1,
    AHORROS_PARA_META_JSON_0,
    AHORROS_PARA_META_JSON_1,
    AHORROS_PARA_META_RESULT_0,
    AHORROS_PARA_META_RESULT_1,
    AHORROS_RESULT_0,
    AHORROS_RESULT_1,
    INTERES_REQUERIDO_JSON_0,
    INTERES_REQUERIDO_JSON_1,
    INTERES_REQUERIDO_RESULT_0,
    INTERES_REQUERIDO_RESULT_1,
    TIEMPO_PARA_META_JSON_0,
    TIEMPO_PARA_META_JSON_1,
    TIEMPO_PARA_META_RESULT_0,
    TIEMPO_PARA_META_RESULT_1,
    VALOR_ACTUAL_JSON_0,
    VALOR_ACTUAL_JSON_1,
    VALOR_ACTUAL_RESULT_0,
    VALOR_ACTUAL_RESULT_1,
)


class TestSavingCalculator(BaseTest):
    """Test all endpoints for the savings calculator"""

    def setUp(self):
        super(TestSavingCalculator, self).setUp()
        with self.app_context:
            pass

    def test_saving_for_goal_end(self):
        """
        Test the endpoint for the savings to reach goal calculator
        when deposit are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/ahorros-para-lograr-meta",
                data=json.dumps(AHORROS_PARA_META_JSON_0),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, AHORROS_PARA_META_RESULT_0)

    def test_saving_for_goal_start(self):
        """
        Test the endpoint for the savings to reach goal calculator
        when deposit are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/ahorros-para-lograr-meta",
                data=json.dumps(AHORROS_PARA_META_JSON_1),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, AHORROS_PARA_META_RESULT_1)

    def test_saving_end(self):
        """
        Test the endpoint for the savings calculator when deposit are
        made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/calculadora-de-ahorros",
                data=json.dumps(AHORROS_JSON_0),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, AHORROS_RESULT_0)

    def test_saving_start(self):
        """
        Test the endpoint for the savings calculator when deposit are
        made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/calculadora-de-ahorros",
                data=json.dumps(AHORROS_JSON_1),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, AHORROS_RESULT_1)

    def test_required_rate_end(self):
        """
        Test the endpoint for the required interest rate calculator
        when deposit are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tasa-de-interes-requerida",
                data=json.dumps(INTERES_REQUERIDO_JSON_0),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertLess(
                abs(data["rate"] - INTERES_REQUERIDO_RESULT_0["rate"]), 0.001
            )

    def test_required_rate_start(self):
        """
        Test the endpoint for the required interest rate calculator
        when deposit are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tasa-de-interes-requerida",
                data=json.dumps(INTERES_REQUERIDO_JSON_1),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertLess(
                abs(data["rate"] - INTERES_REQUERIDO_RESULT_1["rate"]), 0.001
            )

    def test_time_to_goal_end(self):
        """
        Test the endpoint for the time to reach goal calculator
        when deposit are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tiempo-para-lograr-meta",
                data=json.dumps(TIEMPO_PARA_META_JSON_0),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, TIEMPO_PARA_META_RESULT_0)

    def test_time_to_goal_start(self):
        """
        Test the endpoint for the time to reach goal calculator
        when deposit are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/tiempo-para-lograr-meta",
                data=json.dumps(TIEMPO_PARA_META_JSON_1),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, TIEMPO_PARA_META_RESULT_1)

    def test_present_value_end(self):
        """
        Test the endpoint for the present value calculator when deposit
        are made at the end of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/valor-actual",
                data=json.dumps(VALOR_ACTUAL_JSON_0),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, VALOR_ACTUAL_RESULT_0)

    def test_present_value_start(self):
        """
        Test the endpoint for the present value calculator when deposit
        are made at the start of the compounding period
        """
        with self.client as c:
            results = c.post(
                "/valor-actual",
                data=json.dumps(VALOR_ACTUAL_JSON_1),
                headers=TestSavingCalculator.request_headers
            )
            data = json.loads(results.data)

            self.assertDictEqual(data, VALOR_ACTUAL_RESULT_1)


if __name__ == "__main__":
    unittest.main()
