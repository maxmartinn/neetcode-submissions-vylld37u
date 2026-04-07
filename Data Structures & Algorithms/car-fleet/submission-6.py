class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        given postion and speed

        car1 ---- car2
        10mph       1mph
        car1 cannot pass car2 it can only match the speed

        a car fleet is a set of cars drving at the same positio nand same speed

        a single car is also a fleet


        
        naive solution would be to sort position and speed array by position

        Input: target = 10, position = [1,4], speed = [3,2]

        Output: 1

        position = [1,4], speed = [3,2]

        vectors = [(1, 3), (4, 2)]

        target = 10

        repersent each vectors as when it will reach the target by subtracting target by position and then dividing by speed
        stk[i] repersents time crossed
        time_crossed[i] = (target - position[i]) / speed

        stk = [6 2]

        a car fleet is formed whenever a previous car will reach the target at a faster pace then a car in front of it

        so calculate in order and create a monotomic decreasing stack. the number of car fleets will be the length of the stk array

        """

        vectors = sorted(zip(position, speed)) # (position, speed)
        stk = []

        for p, s in vectors:
            time_crossed = 0
            if speed == 0 and target != 0:
                stk = []
            else:
                time_crossed = (target - p) / s
            while stk and stk[-1] <= time_crossed:
                stk.pop()
            stk.append(time_crossed)

        return len(stk)

        """
        target=10
    position=[8,3,7,4,6,5]
    speed=[4,4,4,4,4,4]
        """