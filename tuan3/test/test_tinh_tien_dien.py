import unittest
import tuan3.tinh_tien_dien as tinh_tien_dien


class TestTinhTienDien(unittest.TestCase):
    def test_tinh_tien_dien(self):
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(-1), -1)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(25), 45150)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(75), 136950)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(150), 291950)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(250), 536750)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(350), 825700)
        self.assertEqual(tinh_tien_dien.tinh_tien_dien(450), 1135750)