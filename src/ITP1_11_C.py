import random

class Dice:
    __top = __front = __right = __left = __back = __bottom = 0
    
    def __init__(self, nums):
        self.__top, self.__front, self.__right, self.__left, self.__back, self.__bottom = nums

    @property
    def top(self):
        return self.__top
    @property
    def front(self):
        return self.__front
    @property
    def right(self):
        return self.__right
    @property
    def left(self):
        return self.__left
    @property
    def back(self):
        return self.__back
    @property
    def bottom(self):
        return self.__bottom
    

    def rotate(self, dir):
        if dir == "E":
            self.__top, self.__left, self.__bottom, self.__right = self.__left, self.__bottom, self.__right, self.__top
        elif dir == "N":
            self.__top, self.__front, self.__bottom, self.__back = self.__front, self.__bottom, self.__back, self.__top
        elif dir == "S":
            self.__top, self.__back, self.__bottom, self.__front = self.__back, self.__bottom, self.__front, self.__top
        elif dir == "W":
            self.__top, self.__right, self.__bottom, self.__left = self.__right, self.__bottom, self.__left, self.__top

    def rotate_random(self):
        r = random.randrange(4)
        if r == 0:
            self.rotate("E")
        elif r == 1:
            self.rotate("N")
        elif r == 2:
            self.rotate("S")
        elif r == 3:
            self.rotate("W")
        
    

def main():
    nums = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))
    dice = Dice(nums)
    dice2 = Dice(nums2)
    for _ in range(1000):
        dice.rotate_random()
        if dice.top == dice2.top \
        and dice.front == dice2.front \
        and dice.right == dice2.right \
        and dice.left == dice2.left \
        and dice.back == dice2.back \
        and dice.bottom == dice2.bottom:
            print("Yes")
            return
    print("No")
    

   

if __name__ == "__main__":
    main()