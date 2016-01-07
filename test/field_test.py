import unittest

from ..src.field import Field

class TestField(unittest.TestCase):

    def test_create_field(self):
        Field()

    def test_moving_south_possible(self):
        field = Field()
        self.assertTrue(field.is_move_south_possible())

    def test_moving_south_blocked(self):
        field = Field(south=False)
        self.assertFalse(field.is_move_south_possible())

    def test_moving_north_possible(self):
        field = Field()
        self.assertTrue(field.is_move_north_possible())

    def test_moving_north_blocked(self):
        field = Field(north=False)
        self.assertFalse(field.is_move_north_possible())

    def test_str(self):
        self.assertEqual(str(Field(west = False, east = False)),"<Field north,south>")
