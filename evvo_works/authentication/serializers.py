from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model  # Import the custom user model

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()



class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['email', 'password', "role"]
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class SignInSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        username = attrs.get('email')
        password = attrs.get('password')

        if not username or not password:
            raise serializers.ValidationError('Missing Credentials')

        # Normalize username to lowercase
        username = username.lower()

        # Look up the user
        user = User.objects.filter(email__iexact=username).first()
        if not user:
            raise serializers.ValidationError('User does not exist')
        
        if user and user.check_password(password):
            if not user.is_active:
                raise serializers.ValidationError('User account is inactive.')
            attrs['user'] = user
            attrs["id"] = user.id
            return attrs

        raise serializers.ValidationError('Incorrect Credentials')

