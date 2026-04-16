class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list) # (key : [(value, time)])

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap[key]

        l = 0
        r = len(arr) - 1
        time_pair = ("", -1) # (value, time)
        while l <= r:
            m = (l + r) // 2
            if arr[m][1] <= timestamp:
                time_pair = arr[m]
                l = m + 1
            else:
                r = m - 1
        return time_pair[0]



        """


        Input:
        ["TimeMap", "set", ["alice", "happy", 1], "get", ["alice", 1], "get", ["alice", 2], "set", ["alice", "sad", 3], "get", ["alice", 3]]

        Output:
        [null, null, "happy", "happy", null, "sad"]

        {alice : [(happy, 1),(sad, 3)]}




        """