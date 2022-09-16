from django.contrib.auth.models import BaseUserManager
# BaseUserManager > me permite modificar el comportamiento ENTERO de la creacion del usuario por la terminal
# UserManager > me permitir modificar el comportamiento de los campos nuevos que estoy agregando al modelo del usuario mas no a todos los campos
class AuthManager(BaseUserManager):
    def create_superuser(self, correo, password, nombre,apellido, rol):#esta funcion se debe llamar asi
        """Creacion de un superusuario por consola ()"""
        # los parametros que definamos en el metodo tienen que ser

        if not correo:
            raise ValueError('El super usuario no puede tener el correo vacio')
        
        correo_normalizado = self.normalize_email(correo)
        #inicializo un nuevo usuario con la informaion brindada en la terminal
        nuevoUsuario = self.model(correo=correo_normalizado,nombre=nombre, apellido=apellido, rol=rol, is_staff = True,is_superuser = True)
        #genera un hash de la contraseña para evitar guardar el valor de manera pura en la db
        nuevoUsuario.set_password(password)

        #guardamos el usuario de manera permanente en la db
        nuevoUsuario.save()
        
        return nuevoUsuario