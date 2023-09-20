from rest_framework import serializers
from . models import CustomUser
from drf_extra_fields.fields import Base64ImageField


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)


class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(write_only=True)
    # profile_photo = Base64ImageField(required=False)

    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone_number', 'dob',
                  'password', 'confirm_password', 'profile_photo']

    
    def validate(self, attrs):
        print("ATTRS: ", attrs)
        password = attrs.get("password")
        confirm_password = attrs.get("confirm_password")

        errors = {}
        for i in self.fields:
            if not attrs.get(i):

                errors[f'{i}'] = f"{i} not be blank."

                # raise serializers.ValidationError(f"{i} not be blank.")

        if password != confirm_password:
            errors[f'confirm_password'] = f"Password and Confirm Password not matched."

            # raise serializers.ValidationError(
            #     "Password and Confirm Password not matched.")

        if len(errors) > 0:
            raise serializers.ValidationError(errors)
        return attrs

    def create(self, validated_data):

        # password = validated_data.get('password')
        password = validated_data.pop("confirm_password")

        new_user = CustomUser(**validated_data)
        new_user.set_password(password)
        new_user.save()

        return new_user


class LogoutSerializer(serializers.Serializer):

    refresh_token = serializers.CharField(required=True)


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['fullname', 'email', 'phone_number', 'dob', 'profile_photo']
