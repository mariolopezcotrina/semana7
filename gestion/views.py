from rest_framework.generics import CreateAPIView 
from rest_framework.request import Request
from .serializers import RegistrarUsuarioSerializers
from rest_framework.response import Response
from rest_framework import status
from .enviar_correos import enviar_correo_validacion

# Create your views here.

class RegistroUsuarioView(CreateAPIView):
    serializer_class = RegistrarUsuarioSerializers

    def post(self, request: Request):
        data = self.serializer_class(data= request.data)
        data.is_valid(raise_exception=True)
        data.save()
        print(enviar_correo_validacion(data.data.get('correo')))

        return Response(data={
            'message': 'Usuario creado exitosamente',
            'context': ''

        }, status=status.HTTP_201_CREATED)