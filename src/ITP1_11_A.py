
class Dice:
    __top = __front = __right = __left = __back = __bottom = 0
    
    def __init__(self, nums):
        self.__top, self.__front, self.__right, self.__left, self.__back, self.__bottom = nums

    @property
    def top(self):
        return self.__top

    def rotate(self, dir):
        if dir == "E":
            self.__top, self.__left, self.__bottom, self.__right = self.__left, self.__bottom, self.__right, self.__top
        elif dir == "N":
            self.__top, self.__front, self.__bottom, self.__back = self.__front, self.__bottom, self.__back, self.__top
        elif dir == "S":
            self.__top, self.__back, self.__bottom, self.__front = self.__back, self.__bottom, self.__front, self.__top
        elif dir == "W":
            self.__top, self.__right, self.__bottom, self.__left = self.__right, self.__bottom, self.__left, self.__top

    

def main():
    nums = list(map(int, input().split()))
    commands = input()

    dice = Dice(nums)
    for dir in commands:
        dice.rotate(dir)
    print(dice.top)


    

if __name__ == "__main__":
    main()