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
    dice = Dice(nums)
    q = int(input())
    for _ in range(q):
        top, front = map(int, input().split())
        while(True):
            dice.rotate_random()
            if dice.top == top and dice.front == front :
                print(dice.right)
                break

   

if __name__ == "__main__":
    main()