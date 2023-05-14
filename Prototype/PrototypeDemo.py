from ConcretePrototype import ConcretePrototype

class PrototypeDemo:
    @staticmethod
    def main():
        prototype = ConcretePrototype()
        prototype.set_name("Prototype")
        prototype.set_value(50)

        prototype_clone = prototype.clone()
        prototype_clone.set_name("Prototype Clone")
        prototype_clone.set_value(100)

        print(prototype)
        print(prototype_clone)


PrototypeDemo.main()