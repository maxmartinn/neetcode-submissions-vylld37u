class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # if theres a car in front thats going to get there slower 
        cars = []
        stk = []
        for i in range(len(position)):
            cars.append((position[i], speed[i]))
        cars.sort()
        cars = cars[::-1]
        for car in cars:
            pos = car[0]
            speed = car[1]
            eta = float((target - pos) / speed)
            print(eta)
            if not stk or stk[-1] < eta:
                stk.append(eta)
        return len(stk)
