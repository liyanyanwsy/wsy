#coding:utf-8
import unittest
class Test(unittest.TestCase):
    def test05(self):
        '''判断 a == b '''
        a = 1
        b = 1
        self.assertEqual(a, b)
    def test06(self):
        '''判断 a in b '''
        a = "hello"
        b = "hello world!"
        self.assertIn(a, b)
    def test07(self):
        '''判断 a is True '''
        a = True
        self.assertTrue(a)
    def test08(self):
        '''失败案例'''
        a = "上海-悠悠"
        b = "yoyo"
        self.assertEqual(a,b,msg="失败原因:%s !=%s"%(a,b))

if __name__=='__main__':
    unittest.main()