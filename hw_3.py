class Computer:
    def __init__(self, __cpu, __memory):
        self.__cpu = __cpu
        self.__memory = __memory

    def __make_computations(self, __cpu, __memory):
        return f"""{__cpu} + {__memory}
                {__cpu} - {__memory}
                {__cpu} * {__memory}
                {__cpu} / {__memory}"""
    
    def aces(self):
        return self.__make_computations()

comp = Computer(2, 3)
print(comp.aces())