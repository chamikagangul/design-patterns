class SingletonDemo:
    __instance = None

    @staticmethod
    def getInstance():
        if SingletonDemo.__instance == None:
            SingletonDemo.__instance = SingletonDemo()
        return SingletonDemo.__instance

    def __init__(self):
        if SingletonDemo.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            SingletonDemo.__instance = self

    def printID(self):
        print(id(self))


s1 = SingletonDemo.getInstance()
s1.printID()

s2 = SingletonDemo.getInstance()
s2.printID()

s3 = SingletonDemo()
s3.printID()