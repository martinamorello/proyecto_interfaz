import os
from clases.usuario import Usuario
from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp


# Carga el archivo registro.kv, que está en esta misma carpeta
Builder.load_file(os.path.join(os.path.dirname(__file__), "registro.kv"))


# El nombre de esta clase (RegistroScreen) es el mismo que aparece entre < > en registro.kv.
# MDScreen es la clase de KivyMD que representa una pantalla completa.
class RegistroScreen(MDScreen):
    # Se ejecuta cuando en el .kv se escribe root.volver()
    # "inicio" es el nombre con el que se agregó InicioScreen en app.py.
    def volver(self):
        self.manager.current = "inicio"

    # Se ejecuta cuando en el .kv se escribe root.registrar()
    def registrar(self):
        app = MDApp.get_running_app()
        print(app.usuario_actual)
        print(self.ids.nombre.text)
        self.manager.current = "login"
        usuario=Usuario(self.ids.nombre.text,self.ids.edad.text,self.ids.correo.text,self.ids.contrasena.text)
        if usuario.datos_completos() and usuario.correo_valido() and usuario.nombre_valido():
            self.usuario.append(usuario)