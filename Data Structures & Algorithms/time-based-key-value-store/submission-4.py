class TimeMap:

    def __init__(self):
        self.db = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # {key : [[value, time]]}}
        # 
        # make the db at key append the value and time
        if key not in self.db:
            self.db[key] = []
        self.db[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        values = self.db.get(key, [])
        l = 0
        r = len(values) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            # check if middle values is <= prev_timestamp
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res



