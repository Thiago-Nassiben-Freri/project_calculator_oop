class Calculadora: 
    def __init__(self, valor_1, valor_2): 
        self.valor_1 = valor_1
        self.valor_2 = valor_2
    
    def adicao(self): 
        return self.valor_1 + self.valor_2
    
    def subtracao(self): 
        return self.valor_1 - self.valor_2
    
    def multiplicacao(self): 
        return self.valor_1 * self.valor_2
    
    def divisao(self): 
        return self.valor_1 / self.valor_2
    
valores = Calculadora(5, 9)
print(valores.adicao())
print(valores.subtracao())
print(valores.multiplicacao())
print(valores.divisao())