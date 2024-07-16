# EJERCICIOS--------------
# Ejercicios:
 
# 1. Crea una clase llamada Persona que tendrá los siguientes atributos: nombre, edad y país de origen.
# La clase tendrá un método llamado mostrar_datos que mostrará los datos de la persona.
class Persona:
    def __init__(self, nombre, edad, pais_origen):
        self.nombre = nombre
        self.edad = edad
        self.pais_origen = pais_origen
    
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, País de Origen: {self.pais_origen}")

persona1 = Persona("Sylvia", 37, "Venezuela")
persona1.mostrar_datos()

 
# 2. Crea una clase llamada Rectangulo que tendrá los siguientes atributos: base y altura.
# La clase tendrá un método llamado calcular_area que mostrará el área del
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        area = self.base * self.altura  
        return area 
    
area = Rectangulo(4,5) 
print(f" El área del rectángulo es: {area.calcular_area()}")
        

# 3. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular y cantidad.
# Un titular será obligatorio al crear una cuenta, la cantidad es opcional.
# La clase tendrá dos métodos:
# - ingresar: se ingresa una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.
# - retirar: se retira una cantidad a la cuenta, si la cantidad es negativa, no se hará nada.
class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad
        
        
    def set_ingresar(self, dinero):
        self.cantidad= self.cantidad + dinero
        return print(f"Su saldo es de: {self.cantidad}")
    
    def get_retirar(self, dinero):
        if dinero <= self.cantidad:
            self.cantidad = self.cantidad - dinero
            return print(f"Su saldo es de: {self.cantidad}")
        else:
            return "Saldo insuficiente"
        
    def mostrar_saldo(self):
        print("Tu saldo es: " + str(self.cantidad))
        

dinero_cuenta = Cuenta("Sylvia",100)
dinero_cuenta.set_ingresar(20)
dinero_cuenta.get_retirar(80)
dinero_cuenta.get_retirar(80)

cuenta1 = Cuenta("Maria", 1000)
cuenta1.mostrar_saldo()
 
# 4. Crea una clase llamada Libro que tendrá los siguientes atributos: título y autor.
# La clase tendrá un método llamado mostrar_datos que mostrará los datos del libro.
# Crea una clase llamada LibroTecnico que herede de la clase Libro y añade un atributo llamado tema.
# La clase LibroTecnico tendrá un método llamado mostrar_datos que mostrará los datos del libro.
class Libro:
    #Constructor
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        
    def mostrar_datos(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")
        
    def mostrar_autor(self):
        print(f"Título: {self.titulo}")   
        
#subclase
class LibroTecnico(Libro):
    #Constructor
    def __init__(self, titulo, autor, tema):
        super().__init__(titulo, autor) #Hereda de la super clase usando la palabra SUPER
        self.tema = tema
    
    def mostrar_datos(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Tema: {self.tema}")


libroPython = LibroTecnico("Introducción a Python", "Armand", "Programación")
libroPython.mostrar_datos() #Método de la subclase
libroPython.mostrar_autor() #Método de la superclase (heredado)

 
# 5. Crea una clase llamada Electrodomestico que tendrá los siguientes atributos: precio, color, consumo_energetico y peso.
# Los atributos precio y peso deben tener valores por defecto de 100 y 5 respectivamente.
# La clase tendrá un método llamado precio_final que calculará el precio final del electrodoméstico.
class Electrodomestico:
    def __init__(self, color, consumo_energetico, precio = 100, peso = 5):
         self.precio = precio
         self.color = color
         self.consumo_energetico = consumo_energetico
         self.peso = peso
    
    def precio_final(self):  
        #precio final sobre consumo  
        if self.consumo_energetico == "A":
            self.precio += 50
        elif self.consumo_energetico == "B":
            self.precio += 60
        elif self.consumo_energetico == "C":
            self.precio += 70
        #Precio final sobre el peso
        if self.peso >= 5 and self.peso <7:
            self.precio += 30
        elif self.peso >= 7 and self.peso <10:
            self.precio += 40
        elif self.peso >= 10 and self.peso <15:
            self.precio += 50  
            
        return self.precio
        
electrodomestico1 = Electrodomestico("blanco","A") 
electrodomestico1.peso = 13
print(electrodomestico1.precio_final())