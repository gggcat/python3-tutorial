import random
import mypackage.mymodule

def main():
    x = random.random()
    y = random.random()

    print("X={}".format(x))
    print("Y={}".format(y))

    print("X+Y={}".format(mypackage.mymodule.add(x, y)))

if __name__ == '__main__':
    main()