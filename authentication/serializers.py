from rest_framework import serializers
from authentication.models import User, Profile
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate, get_user_model


class RegisterSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    role = serializers.ChoiceField(choices=[('HA', 'HOSPITAL ADMIN'),
                                            ('SU', 'SPONSOR USER'),
                                            ('HL', 'HEALTH TRACKER ADMIN')])
    # adress = serializers.CharField()

    password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )
    confirmed_password = serializers.CharField(
        max_length=128,
        min_length=6,
        write_only=True,
        error_messages={
            "min_length": "Password should be at least {min_length} characters"
        }
    )

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'confirmed_password',
                  'contact', 'adress', 'role', 'password']

    def validate(self, data):
        """
        validate data before its saved
        """
        confirmed_password = data.get('confirmed_password')
        try:
            validate_password(data.get('password'))
        except ValidationError as identifier:
            raise serializers.ValidationError({
                "password": str(identifier).replace(
                    "["", "").replace(""]", "")
            })

        if not self.password_do_match(data.get('password'), confirmed_password):
            raise serializers.ValidationError({
                'password': ('password do not match')
            })
        return data

    def create(self, validated_data):
        """create a user"""
        del validated_data['confirmed_password']
        return User.objects.create_user(**validated_data)

    def password_do_match(self, password1, password2):
        return password1 == password2


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        write_only=True, min_length=6)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError({
                'invalid': 'the password or email is wrong'
            })

        user_1 = {
            'email': user.email,
            'token': user.token,
        }
        return user_1


class ProfileCreateSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Profile
        fields = [
            'username',
            'email',
        ]

    def create(self, validated_data):
        user = get_user_model().objects.create(
            username=validated_data['user']['username'])
        user.set_password(User.objects.make_random_password())
        user.save()

        profile = Profile.objects.create(user=user)

        return profile
