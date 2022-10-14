class Person:
    def __init__(self, name=None, age=None, address=None):
        self.__name = name
        self.__age = age
        self.__address = address

    def setName(self, name=None):
        if name is None:
            self.__name = "Linh"
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        self.__age = age

    def getAge(self):
        return self.__age

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    def input(self):
        self.setName(input("Nhập tên:"))
        try:
            self.setAge(int(input("Nhập tuổi:")))
        except:
            self.setAge(int(input("Nhập tuổi:")))
        self.setAddress(input("Nhập địa chỉ:"))

    def output(self):
        print("Tên:", self.getName())
        print("Tuổi:", self.getAge())
        print("Địa chỉ:", self.getAddress())
