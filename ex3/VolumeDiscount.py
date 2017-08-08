import re

class VolumeDiscount():

    def bestDeal(self, priceList, quantity):
        d = {}
        for price in priceList:
            match = re.match("(\w+)\s+(\w+)", price)
            d[int(match.group(1))] = int(match.group(2))
        if quantity <  min(d.keys()):
            result = min(d.values())
        else:
            unit_price = []
            for price in d.keys():
                unit_price.append(d[price] / float(price))
            min_unit_price = min(unit_price)
            index_min = unit_price.index(min_unit_price)     
            integer = quantity / d.keys()[index_min]
            remain = quantity % d.keys()[index_min]            
            result = integer * d[d.keys()[index_min]]            
            del d[d.keys()[index_min]]
            newPriceList = []
            for key in d.keys():
                newPriceList.append(str(key) + " "+ str(d[key]))
            if remain != 0:
                result = result + self.bestDeal(newPriceList, remain)              
        return result