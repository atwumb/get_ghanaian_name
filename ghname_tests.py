import unittest
import date_week_born
import ghname

class GetDayTestCase(unittest.TestCase):
    def test_get_day(self):
        self.assertEqual(date_week_born.get_day('08/04/1981'), "Tuesday")
    def test_get_name(self):
        self.assertEqual(ghname.get_ghname(), "Abena")
    def test_get_name_meaning(self):
        self.assertEqual(ghname.get_name_meaning('Tuesday'),"Full of fire and determination, inspirer, risk-taker, will go through a period of uncertainty that will lead to change" )




if __name__ == '__main__':
    unittest.main()