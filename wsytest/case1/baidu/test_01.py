#coding:utf-8
import  unittest
class IntegerArithmeticTestCase(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def testAdd(self):  ## test method names begin 'test*'
        self.assertEqual((1 + 2), 3)
        self.assertEqual(0 + 1, 1)
    def testMultiply(self):
        self.assertEqual((0 * 10), 0)
        self.assertEqual((5 * 8), 40)
    def test_00(self):
        u'''测加法减法是否正确'''
        print "执行成功"

if __name__ == '__main__':
    unittest.main()