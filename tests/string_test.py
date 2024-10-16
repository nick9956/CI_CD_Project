import unittest
import xmlrunner
import io


class TestStringMethods(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    out = io.BytesIO()
    unittest.main(
        testRunner=xmlrunner.XMLTestRunner(output='../test-reports'),
        failfast=False,
        buffer=False,
        catchbreak=False,
        exit=False)
