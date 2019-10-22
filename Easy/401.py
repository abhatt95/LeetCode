"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
"""
from itertools import combinations 

class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:
        
        options = ["8h","4h","2h","1h","32","16","8","4","2","1"]
        
        comb = combinations(options,num)
        
        output = []
        
        for x in list(comb):
            current_hour = 0
            current_min = 0
            for time in x:
                if "h" in time:
                    current_hour+= int(time.replace("h",""))
                else:
                    current_min+= int(time)
            if current_hour < 12 and current_min < 60:
                op = str(current_hour)+":"+"{:02d}".format(current_min)
                output.append(op)
        return sorted(output)
        