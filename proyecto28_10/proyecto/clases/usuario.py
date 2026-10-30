class Usuario:
    def __init__(self,nombre, edad, correo,contrasena ):
        self.nombre=nombre
        self.edad=edad
        self.correo=correo
        self.contrasena=contrasena

    def datos_completos(self):
        if self.nombre==True and self.edad==True and self.correo==True and self.contrasena==True :
            return True
        else:
            print("Faltan datos por completar")
            return False
            
    
    def correo_valido(self):
        if "@pioix.edu.ar" in self.correo:
            return True
        else:
            print("El mail debe terminar con: @pioix.edu.ar")
            return False
            

    def nombre_valido(self):
        if self.nombre.isalpha():
            return True
        else:
            print("El nombre debe empezar con mayuscula")
            return False
            

    def contrasena_incorrecta(self,contrasena):
        if self.contrasena== contrasena:
            return True
        else:
            print("Contraseña incorrecta")
            return False
            