from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView

from authentication.serializers import RegistrationSerializer
from authentication.renderer import UserJSONRenderer
from authentication.serializers import LoginSerializer


class RegistrationApiView(APIView):

    renderer_classes = (UserJSONRenderer,)
    permission_classes = (AllowAny, )
    serializer_class = RegistrationSerializer

    def post(self, request):
        self.http_method_names.append("GET")
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)

        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginApiView(APIView):

    permission_classes = (AllowAny,)
    renderer_classes = (UserJSONRenderer,)
    serializer_class = LoginSerializer

    def get(self, request):
        user = request.data.get('user', {})

        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    # def get(self, request):
    #     return self.post(request)
