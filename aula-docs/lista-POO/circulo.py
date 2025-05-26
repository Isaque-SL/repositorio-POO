class circulo:
    def __init__(self):
        self.__raio = 0
    
    def set_raio(self, raio):
        if raio > 0:
            self.__raio = raio
        else:
            raise ValueError
    
    def get_raio(self):
        return self.__raio
    
    def calc_area(self):
        return 3.14159 * (self.__raio ** 2)
    
    def calc_circunferencia(self):
        return 2 * 3.14159 * self.__raio
    
class UI:
    @staticmethod
    def main():
        x = circulo()
        x.set_raio(float(input("Digite o raio do círculo:\n")))
        area = x.calc_area()
        circunferencia = x.calc_circunferencia()
        
        print(f"Área: {area:.2f}")
        print(f"Circunferência: {circunferencia:.2f}")

UI.main()