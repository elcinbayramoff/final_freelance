from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import OTP
from department.models import Department
from position.models import Position
from employee.models import Employee
User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=100, write_only=True)
    surname = serializers.CharField(max_length=100, write_only=True)
    department = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(), write_only=True)
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), write_only=True)
    status = serializers.BooleanField(default=True, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email', 'role', 'name', 'surname', 'department', 'position', 'status']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        name = validated_data.pop('name')
        surname = validated_data.pop('surname')
        department = validated_data.pop('department')
        position = validated_data.pop('position')
        status = validated_data.pop('status')

        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            role=validated_data['role'],
            is_active=False  
        )
        user.set_password(validated_data['password'])
        user.save()

        Employee.objects.create(
            user=user,
            name=name,
            surname=surname,
            email=user.email,
            department=department,
            position=position,
            status=status
        )

        otp = OTP.objects.create(user=user)
        otp.generate_code()
        user.send_otp_email(otp.code)

        return user

    def to_representation(self, instance):
        """Customize the representation of the serialized data."""
        representation = super().to_representation(instance)
        representation.pop('name', None)
        representation.pop('surname', None)
        representation.pop('department', None)
        representation.pop('position', None)
        representation.pop('status', None)
        return representation


class OTPVerificationSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.CharField(max_length=6)

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
