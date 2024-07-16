# DEF: Podemos definir un objeto en programación, como un conjunto de propiedades o atributos y métodos 
# A las propiedades, también le podemos llamar DATOS
# A los métodos también las llamamos FUNCIONES

string = "Hola mundo" # longitud es 4 (propiedad)

string.replace("mundo","world") # es una acción

# TERMINOLOGÍA OOP
# CLASE: Plantilla / "Fábrica" que define las características de un objeto en concreto
# INSTANCIA: El proceso en el que se crea un objeto
# PROP o ATRIBUTOS: Características de un objeto
# MÉTODOS: la capacidad o acción de un objeto
# CONSTRUCTOR: Método especial. Su función principal es inicializar las propiedades de un objeto al instanciarse. Se ejecuta automáticamente en esa instancia. No es obligatorio tenerlo
# HERENCIA: Una clase creada mediante herencia se le llamada "subclase", y hereda todas las propiedades y los métodos de la "superclase"
# ENCAPSULAMIENTO: es la capacidad de ocultar propiedades/métodos que se consideren o bien privados o innecesarios para la interacción del objeto desde el exterior
# ABSTRACCIÓN: proceso de diseño de las clases que nos definen las cualidades del objeto
# POLIFORMISMO: La manera de que diferentes clases prodrían definir la misma prop o método


# Ejemplo clase Usuario
class Usuario:
    # constructor
    # self: hace referencia a la instancia de la clase
    def __init__(self, nombreUsuario, email, password):
        # asigno a las propiedades de la clase, lo que llega de la instancia del objeto
        self.nombreUsuario = nombreUsuario
        self.email = email
        self.password = password
        self.emailConfirmado = False
    
    # NO DEFINIR CON MISMO NOMBRE LA PROP Y EL METODO    
    # método que confirma el email
    def isEmailConfirmado(self):
        self.emailConfirmado = True
        
# Instancia de un usuario
usuario1 = Usuario("armand", "armand@gmail.com", "1111")
usuario2 = Usuario("mqaria", "maria@gmail.com", "2222")

# Imprimir todas las props de un objeto
print(usuario1.__dict__)

# Suponer que el usuario ha confirmado el email
usuario1.isEmailConfirmado()
print(usuario1.__dict__)

# Interacción con los objetos
print(usuario1.email)
print(usuario2.email)

# Puedo crear una nueva propiedad desde aquí?: SÍ
usuario1.ciudad = "Barcelona"
print(usuario1.__dict__)

#-----------------------------------
class Coche:
    def __init__(self, year, color, marca ="Mercedes"):
        self.year = year
        self.color = color
        self.marca = marca
        self.ensamblado = False
        
    def get_antig_coche(self):
        #siempre que dentro de hacemos referencia a una prop o método va procedido de "self"
        from datetime import datetime
        return datetime.now().year - self.year
    
    #Método setter (si llamo a este método, setea la prop a True)
    def set_ensamblado(self):
        self.ensamblado = True
    
    # Método getter
    def get_ensamblado(self):
        return self.ensamblado
        
    
# Instancias
miCoche1 = Coche(2022, "verde")
print(miCoche1.__dict__)
print("La antigüedad de miCoche1")

# Desde fuera lo podemos cambiar (podemos gestionar este acceso con encapsulamiento)
# miCoche1.ensamblado = True
# print(miCoche1.__dict__)
# cambiamos el ensamblando
miCoche1.set_ensamblado()# ensamblado = True
print(miCoche1.get_ensamblado()) #ensamblado = True


# MÉTODO ESTÁTICO
# Ejemplo de un método estático. No es necesario llamar a estos métodos a través de la instancia de su clase (creación del objeto)
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @staticmethod #define el método como estático    
    def get_distancia (a, b):
        dx = a.x - b.x
        dy = a.y - b.y
        return (dx**2 + dy**2)**0.5
        
punto1 = Punto(5,5)
punto2 = Punto(10, 10)
print(Punto.get_distancia(punto1, punto2))


#Herencia
#Superclase
class Vehiculo: 
    def __init__(self, color, marca, year):
        self.color = color
        self.marca = marca 
        self.year = year 
        
    def get_antiguedad_vehiculo(self):
        from datetime import datetime
        print(datetime.now().year - self.year)
        
#Subclase Coche     
class Coche(Vehiculo): 
    # El constructor hereda de la superclase sus props y añadimos las exclusivas de esta propia clase (subclase)
    def __init__(self, color, marca, year, num_puertas):
        super().__init__(color, marca, year)
        self.num_puertas = num_puertas
        
    def abrir_maletero(self):
        print("Has abierto el maletero!")
        
        
#Subclase Moto
class Moto(Vehiculo): 
    # El constructor hereda de la superclase sus props y añadimos las exclusivas de esta propia clase (subclase)
    def __init__(self, color, marca, year):
        super().__init__(color, marca, year)

    def hacer_caballito(self):
        print("Has hecho caballito!")
        
        
# Encapsulamiento
class CocheEncapsulacion:
    def __init__(self, color, marca, year):
        self.color = color
        self.marca = marca 
        self.year = year
        # Propiedad privada, en Python: se precede de "__"
        self.__nivel_deposito = 0
        
    # Si queremos interactuar con propiedades privados utilizamos métodos "setters" y "getters"
    # SETTER
    def set_llenar_depósito(self, litros):
        total = self.__nivel_deposito + litros
        # suponemos que el depósito tiene capacidad max de 100 libros 
        if total > 100:
            self.__nivel_deposito = 100
            print("Depósito lleno")
        else:
            self.__nivel_deposito = total
            return f"El depósito tiene {total} litos"
      
   #Getter
    def get_nivel_deposito(self):
        return self.__nivel_deposito
    
   
miCoche2 = CocheEncapsulacion(2020,"Rojo", "Fiat")

# comprobación de prop privada
miCoche2.__nivel_deposito = 30
print(miCoche2.__dict__)
# Attribute error: "CocheEncapsulacion" object has no attribute "__nivel:deposito"
print(miCoche2.get_nivel_deposito())

#repostamos
miCoche2.set_llenar_depósito(50)
print(miCoche2.set_llenar_depósito())
miCoche2.set_llenar_depósito(55)



