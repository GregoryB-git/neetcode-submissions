class TimeMap:

    def __init__(self):
        self.store = defaultdict(list) #key=str, value=[val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" #this is the expected return if nothing is found
        values = self.store.get(key, [])

        #bisearch
        l, r = 0, len(values) -1
        while l <= r:
            m = (l+r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            
            elif values[m][1] == timestamp:
                return res

            else:
                r = m - 1

        return res

        
