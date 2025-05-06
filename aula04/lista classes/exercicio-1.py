class circulo:
    def __init__(self):
        self.raio = 25
        
    def calcular_area(self):
        self.area = 3.14159 * (self.raio ** 2)
        return self.area
    
    def circunferencia(self):
        self.circun = 2 * 3.14159 * self.raio
        return self.circun

x = circulo()
area = x.calcular_area()
circunferencia = x.circunferencia()
print(f"{area:.2f}")
print(f"{circunferencia:.2f}")