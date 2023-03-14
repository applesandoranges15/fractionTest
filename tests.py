from fraction import Fraction
import unittest
import unittest 
from src import calc
class TestInit(unittest.TestCase):
  #several of these will need to check to see if an exception is raised
  def test_divZero(self):
    with self.assertRaises(ZeroDivisionError,msg="Denominator of zero fails to raise DivByZero"):
      a = Fraction(1,0)
  def test_default(self):
      a = Fraction()
      self.assertEquals(0, a.numerator)
      self.assertEquals(1, a.denominator)
  def test_oneArg(self):
      a = Fraction(5)
      self.assertEquals(5, a.numerator)
      self.assertEquals(1, a.denominator)
  def test_twoArg(self):
    a = Fraction(2, 5)
    self.assertEquals(2, a.numerator)
    self.assertEquals(5, a.denominator)
  def test_invalidArg(self):
    with self.assertRaises(ValueError, msg="Cannot non-numeric data as arguments")
      a = Fraction("o", 5)
  def test_reduced(self):
    a = Fraction(4, 2)
    self.assertEquals(2, a.numerator)
    self.assertEquals(1, a.denominator)
    b = Fraction(3, 9)
    self.assertEquals(1, b.numerator)
    self.assertEquals(3, b.denominator)
    #if the inputs share a factor, is the fraction reduced? i.e. 2/4 = 1/2

class TestStr(unittest.TestCase):
  def test_displayfraction(self):
    a = Fraction(1,2)
    self.assertEqual("1/2",a.__str__())
  def test_displayInt(self):
    a = Fraction(5,1)
    self.assertEqual("5", a.__str__())
  def test_displayNeg(self):
    a = Fraction(2, -7)
    self.assertEqual("-2/7", a.__str__())
    b = Fraction(-5, 9)
    self.assertEqual("-5/9", b.__str__())
    c = Fraction(-3, -2)
    self.assertEqual("3/2", c.__str__())

class TestFlt(unittest.TestCase):
  def testPositive(self):
    a=Fraction(3, 4)
    self.assertEqual(0.75, a.__float__())
  def testNegative(self):
    a=Fraction(-3,4)
    self.assertEqual(-0.75, a.__float__())
  def test_invalidArg(self):
    with self.assertRaises(ValueError, msg="Cannot non-numeric data as arguments")
      a = "apple"
      a.__float__()


class TestAdd(unittest.TestCase):
  def setUp(self):
    self.first=Fraction(2, 3)
    self.second=Fraction(1,3)
    self.third=Fraction(-1,3)
    self.fourth=Fraction()
  def add_positive(self):
    assertEqual("1", self.first.__add__(self.second).__str__())
  def add_negative(self):
    assertEqual("1/3", first.__add__(self.third).__str__())
  def add_zero(self):
    assertEqual("2/3", self.first.__add__(self.fourth).__str__())


  
class TestSub(unittest.TestCase):
  def setUp(self):
    self.first=Fraction(2, 3)
    self.second=Fraction(1,3)
    self.third=Fraction(-1,3)
    self.fourth=Fraction()
  def sub_positive(self):
    assertEqual("1/3", self.first.__sub__(self.second).__str__())
  def sub_negative(self):
    assertEqual("-1/3", self.second.__sub__(self.first).__str__())
  def sub_zero(self):
    assertEqual("2/3", self.first.__sub__(self.fourth).__str__())
  def add_doubleNeg(self):
    assertEqual("0", self.third.__sub__(self.third).__str__())


class TestMult(unittest.TestCase):
  def mult_post(self):
    a=Fraction(2,3)
    b=Fraction(1,2)
    assertEqual("1/3", a.__mult__(b).__str())
  def mult_neg(self):
    a=Fraction(2,3)
    b=Fraction(-1,3)
    assertEqual("-2/9", a.__mult__(b).__str())
  def mult_doubleNeg(self):
    a=Fraction(-1,3)
    assertEqual("1/9", a.__mult__(a).__str())
  def mult_zero(self):
    a=Fraction(-1,3)
    b=Fraction()
    assertEqual("0", a.__mult__(b).__str())
  def test_invalidArg(self):
    with self.assertRaises(ValueError, msg="Cannot non-numeric data as arguments")
      a = "apple"
      a.__mult__(a)
  
class TestTrueDiv(unittest.TestCase):
  def div_pos(self):
    a=Fraction(2,3)
    b=Fraction(1,2)
    assertEqual("4/3", a.__div__(b).__str())
  def div_neg(self):
    a=Fraction(2,3)
    b=Fraction(-1,3)
    assertEqual("-2", a.__div__(b).__str())
  def div_doubleNeg(self):
    a=Fraction(-1,3)
    assertEqual("3", a.__div__(a).__str())
  def test_invalidArg(self):
    with self.assertRaises(ValueError, msg="Cannot non-numeric data as arguments")
      a = "apple"
      a.__div__(a)
  def div_zero(self):
    with self.assertRaises(ZeroDivisionError, msg="Cannot divide by zero")
      a = Fraction(1,2)
      b=Fraction()
      a.__div__(b)
  
    
