from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Users, UserProfile, Role

class RegisterSerializer(serializers.Serializer):
    login = serializers.CharField(max_length=100)
    password = serializers.CharField(write_only=True)
    role_id = serializers.IntegerField(required=False)
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    surname = serializers.CharField()
    email = serializers.EmailField()

    def create(self, validated_data):
        role_id = validated_data.get('role_id')
        role = None
        if role_id:
            try:
                role = Role.objects.get(pk=role_id)
            except Role.DoesNotExist:
                pass  # можно выбросить ошибку

        user = Users.objects.create(
            login=validated_data['login'],
            password=make_password(validated_data['password']),
            role=role
        )
        UserProfile.objects.create(
            user=user,
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            surname=validated_data['surname'],
            email=validated_data['email']
        )
        return user
