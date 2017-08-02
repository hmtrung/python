'''
Created on Jul 27, 2017

@author: hminhtrung
'''

import re

class ParameterSubstitution():
    
    def processParams(self, code, params):
        numbers = self.find_number(code) # find all numbers follow by $ and save them to an array
#         print "numbers = ", numbers 
        filtered_numbers = self.number_filter(numbers, len(params)) # filter numbers meet the requirement: number must less than or equal length of params, and not start with 0
#         print "filtered_numbers = ", filtered_numbers
        splitted_code = self.split(self.dollar_append(filtered_numbers), code) # split code into array, delimit by ($ + number)
#         print "splitted_code = ", splitted_code
        result = "".join(self.replace(filtered_numbers, splitted_code, params)) # replace ($ + number) by params[number - 1]
#         print "result = ", result
        return result
    
    # find array of number follow by $
    # code = "$3+$1*$2-$7=$10"
    # return: match =  ['3', '1', '2', '7', '10']
    def find_number(self, code):
        numbers = re.findall("\$(\d+)", code)
        return numbers
    
    # filter number <= size and not leading by 0
    def number_filter(self, numbers, size):
        filtered_numbers = []
        for item in numbers:
            while int(item) > size and int(item) >= 10:
                item = item[:-1]
            if int(item) <= size and re.match("^0", item) == None:
                filtered_numbers.append(item)
        return filtered_numbers
    
    
    def dollar_append(self, array):
        dollar_appended_numbers = []
        for item in array:
            dollar_appended_numbers.append("$" + item)
        return dollar_appended_numbers
    
    # split by $ + number
    # array = ['$3', '$1', '$2', '$1']
    # code = $3+$1*$2-$7=$10
    # return: ['$3', '+', '$1', '*', '$2', '-$7=', '$1', '0']
    def split(self, array, code):
        words = []
        for item in array:
            index = code.index(item)
            words.append(code[0 : index])
            words.append(item)
            code = code[index + len(item):]
        words.append(code)
        return words
    
    # numbers = ['3', '1', '2', '1']
    # code = ['', '$3', '+', '$1', '*', '$2', '-$7=', '$1', '0']
    # params = ["myvar", "490jri", "e09jd9", "dlkjfoiej"]
    # return: ['', 'e09jd9', '+', 'myvar', '*', '490jri', '-$7=', 'myvar', '0']
    
    def replace(self, numbers, code, params):
        tmp = [None] * len(code)
        if numbers == []:
            tmp = code
        else:
            for i in range(len(code)):
                for j in range(len(numbers)):
                    if code[i] == str("$" + numbers[j]):
                        tmp[i] = params[int(numbers[j]) - 1]
                        break
                    else:
                        tmp[i] = code[i]
        return tmp
