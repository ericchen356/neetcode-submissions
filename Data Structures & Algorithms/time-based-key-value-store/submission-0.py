class TimeMap:

    def __init__(self):
        # maps { key : [[value, timestamp], [value, ts]]}

        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.dict: 
            self.dict[key].append([value, timestamp])
        else: 
            self.dict[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:

        pairs = self.dict.get(key, [])
        res = ""

        l = 0
        r = len(pairs) - 1

        while l <= r: 
            mid = (l + r) // 2 
            
            if pairs[mid][1] <= timestamp: 
                res = pairs[mid][0]
                l = mid + 1
            else: 
                r = mid - 1
        
        return res