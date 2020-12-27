"""
Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.

Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.

https://leetcode.com/problems/logger-rate-limiter/
"""

class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.getNextPrintingTimeFor = {}
        
    def cleanUpMap(self,currentTime:int):
        secondCopy = dict(self.getNextPrintingTimeFor)
        self.getNextPrintingTimeFor = {}
        for k,v in secondCopy.items():
            if v > currentTime:
                self.getNextPrintingTimeFor[k] = v
                

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        """
        
        windowSize = 10
        
        if message not in self.getNextPrintingTimeFor:
            self.getNextPrintingTimeFor[message] = timestamp + windowSize
            self.cleanUpMap(timestamp)
            return True
        
        if self.getNextPrintingTimeFor[message] > timestamp:
            self.cleanUpMap(timestamp)
            return False
        
        self.getNextPrintingTimeFor[message] = timestamp + windowSize
        self.cleanUpMap(timestamp)
        return True
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)