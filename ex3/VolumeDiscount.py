import re

class VolumeDiscount(object):
    def best_deal(self, price_list, quantity):
        dictionary = {}
        for price in price_list:
            match = re.match(r"(\w+)\s+(\w+)", price)
            dictionary[int(match.group(1))] = int(match.group(2))
        if quantity < min(dictionary.keys()):
            result = min(dictionary.values())
        else:
            unit_price = []
            for price in dictionary:
                unit_price.append(dictionary[price] / float(price))
            min_unit_price = min(unit_price)
            index_min = unit_price.index(min_unit_price)
            integer = quantity / dictionary.keys()[index_min]
            remain = quantity % dictionary.keys()[index_min]
            result = integer * dictionary[dictionary.keys()[index_min]]
            del dictionary[dictionary.keys()[index_min]]
            new_price_list = []
            for key in dictionary:
                new_price_list.append(str(key) + " " + str(dictionary[key]))
            if remain != 0:
                result = result + self.best_deal(new_price_list, remain)
        return result
