import unittest
from VolumeDiscount import VolumeDiscount


class SimpleTest(unittest.TestCase):
    
    def test1(self):
        vd = VolumeDiscount()
        priceList = ["1 10", "5 45"]
        quantity = 10
        result = 90
        self.assertEquals(vd.bestDeal(priceList, quantity), result)
      
    def test2(self):
        vd = VolumeDiscount()
        priceList = ["1 8", "5 45"]
        quantity = 10
        result = 80
        self.assertEquals(vd.bestDeal(priceList, quantity), result)
         
    def test3(self):
        vd = VolumeDiscount()
        priceList = ["99 913", "97 173", "50 464", "80 565"]
        quantity = 18
        result = 173
        self.assertEquals(vd.bestDeal(priceList, quantity), result)
        
    def test4(self):
        vd = VolumeDiscount()
        priceList = ["2 272","1 166","10 993"]
        quantity = 81
        result = 8110
        self.assertEquals(vd.bestDeal(priceList, quantity), result) 
            
if __name__ == '__main__':
    unittest.main()
