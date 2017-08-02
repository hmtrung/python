'''
Created on Jul 27, 2017

@author: hminhtrung
'''
import unittest
from ParameterSubstitution import ParameterSubstitution


class SimpleTest(unittest.TestCase):
    
    def test1(self):
        ps = ParameterSubstitution()
        code = "if ($1 == $2) $3;"
        params = ["12", "12", "doWhatIWant()"]
        result = "if (12 == 12) doWhatIWant();"
        self.assertEquals(ps.processParams(code, params), result)
          
    def test2(self):
        ps = ParameterSubstitution()
        code = "$3+$1*$2-$7=$10"
        params = ["myvar", "490jri", "e09jd9", "dlkjfoiej"]
        result = "e09jd9+myvar*490jri-$7=myvar0"
        self.assertEquals(ps.processParams(code, params), result)
           
    def test3(self):
        ps = ParameterSubstitution()
        code = "12342123$13231232$2123211242$a$dlkj$"
        params = ["$2", "$1"]
        result = "12342123$23231232$1123211242$a$dlkj$"
        self.assertEquals(ps.processParams(code, params), result)
      
    def test4(self):
        ps = ParameterSubstitution()
        code = "{[(+.*-,/\\:;<=>?@)]}_`~|$$1"
        params = ["1{[(+.*-,/\\:;<=>?@)]}_`~|"]
        result = "{[(+.*-,/\\:;<=>?@)]}_`~|$1{[(+.*-,/\\:;<=>?@)]}_`~|"
        self.assertEquals(ps.processParams(code, params), result)
         
    def test5(self):
        ps = ParameterSubstitution()
        code = "$01"
        params = ["abc"]
        result = "$01"
        self.assertEquals(ps.processParams(code, params), result)
            
if __name__ == '__main__':
    unittest.main()
