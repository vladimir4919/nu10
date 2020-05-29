import random
import unittest
import pytest
from prepare_loto import Person,Dropout,Ticket, Computer,Gamer, Bag


class TestTicket(unittest.TestCase):

    def setUp(self):
        self.ticket = Ticket()

    def tearDown(self):
        pass

    def test_init(self):
        self.assertEqual(len(self.ticket.numbers), 15)
        self.assertEqual(len(self.ticket.strings), 3)


    def test_show_ticket(self):
        self.assertEqual(len(self.ticket.strings), 3)




class TestGamer(unittest.TestCase):

    def setUp(self):
        self.card = Ticket()

    def test_is_victory(self):
        self.assertEqual(len(self.card.strings), 3)
        self.assertTrue(self.card.strings, '-')


class TestComputer(unittest.TestCase):

    def setUp(self):
        self.card = Ticket()

    def test_cross_out(self):
        self.assertTrue(self.card.strings, '-')


class TestPerson(unittest.TestCase):

    def setUp(self):
        self.card = Ticket()

    def test_act(self):
        answer = ['yes', 'no']
        self.assertEqual(answer, ['yes', 'no'])
        num = random.randint(0, 90)
        while answer == 'yes':
            self.assertIn(num, self.card.nums)
        while answer == 'no':
            self.assertNotIn(num, self.card.nums)


class TestBag(unittest.TestCase):

    def setUp(self):
        self.card = Ticket()

    def test_init(self):
        self.assertTrue(self.card.numbers, [1, 91])

    def test_select_sample(self):
        self.assertEqual(len(self.card.numbers), 15)





