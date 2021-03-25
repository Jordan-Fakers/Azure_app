import unittest
from bdd import connection_db, select_from_db
from mailsender import go_mail, table_data
import os

class TestCodes(unittest.TestCase):

    def test_connectionbdd(self):
        self.assertTrue(connection_db())

    def test_selectbdd(self):
        self.assertEqual(type(select_from_db()), list)
    
    def test_sendmail(self):
        email = "overlordtest97.1@gmail.com"
        data = select_from_db()
        msg = data
        self.assertEqual(type(go_mail(email, data)),str)

if __name__ == '__main__':
    unittest.main(verbosity=2)