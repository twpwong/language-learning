import unittest
import japanese_conjugation as jc


class TestJapaneseConjugation(unittest.TestCase):
    def test_classify_godan_ru_exception(self):
        self.assertEqual(jc.classify_verb("切る"), "godan")

    def test_conjugate_godan_ru_exception_masu(self):
        self.assertEqual(jc.conjugate("切る", "masu"), "切ります")


if __name__ == "__main__":
    unittest.main()
