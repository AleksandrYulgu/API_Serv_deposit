try:
    import unittest
    from views import deposit_calculation, format_for_datetime, list_date, dict_data_base
    from Serv_deposit import app
    from flask.testing import FlaskClient
except Exception as e:
    print("Some Modules are Missing {}".format(e))


class TestViews(unittest.TestCase):

    def test_depos_calc_period(self):
        period = 3
        amount = 10000
        rate = 6
        self.assertEqual(deposit_calculation(period, amount, rate), [10050.0, 10100.25, 10150.75])

    def test_depos_calc_period_type(self):
        period = 3
        amount = 10000
        rate = 6
        self.assertRaises(TypeError, deposit_calculation, period, amount, 'rate')
        self.assertRaises(TypeError, deposit_calculation, 'period', amount, rate)
        self.assertRaises(TypeError, deposit_calculation, period, "amount", rate)

    def test_type_format_date(self):
        date = '31.01.2021'
        self.assertEqual(format_for_datetime(date), (2021, 1, 31))

    def test_actual_date_list_date(self):
        date = (2021, 1, 31)
        per = 3
        self.assertEqual(list_date(date, per), ['31.01.2021', '28.02.2021', '31.03.2021'])

    def test_dict_date_base(self):
        date = '31.01.2022'
        period = 3
        amount = 100000
        rate = 6
        self.assertEqual(dict_data_base(date, period, amount, rate), {'31.01.2022': 100500.0, '28.02.2022': 101002.5, '31.03.2022': 101507.51})
        #self.assertRaises(TypeError, dict_data_base, date, period, amount, rate)

"""
class TestApp(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/deposits")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get("/deposits")
        statuscode = response.status_code
        self.assertEqual(response.content_type, "application/json")
"""

if __name__ == "__main__":
    unittest.main()
