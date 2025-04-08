from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model  # Import the custom user model
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework import status

from authentication.serializers import GroupSerializer, UserSerializer, SignUpSerializer, SignInSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import serializers

# Fetch the custom user model
User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')  # Use the custom user model
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all().order_by('name')
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class SignUpView(viewsets.ViewSet):
    serializer_class = SignUpSerializer
    queryset = User.objects.all()
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow unauthenticated access

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SignInView(APIView):
    authentication_classes = []  # Disable authentication for this view
    permission_classes = [AllowAny]  # Allow unauthenticated access
    serializer_class = SignInSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        print(request.data, serializer.is_valid())
        try:
            serializer.is_valid(raise_exception=True)
        except serializers.ValidationError as e:
            print(e)
            if 'Incorrect Credentials' in str(e) or 'User does not exist' in str(e):
                return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
            raise e

        if serializer.is_valid():
            print(serializer.validated_data)
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            tokens = {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
            return Response(tokens, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)