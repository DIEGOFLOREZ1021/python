class A:
    Num1= None
    Num2 = None

    def __init__(self) -> None:
        self.Num1 = 0
        self.Num2 = 0

    def Suma(self) -> int:
        return self.Num1 + self.Num2
    
    def Resta(self) -> int:
        return self.Num1 - self.Num2
    
class B:
    Num1= None
    Num2 = None

    def __init__(self) -> None:
        pass

    def Suma(self) -> int:
        return self.Num1 + self.Num2
    
    def Resta(self) -> int:
        return self.Num1 - self.Num2
    
class calculadora(B, A): pass

c = calculadora(36, 18)


