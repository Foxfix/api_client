# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from ..models import Profile

# from rest_framework_jwt.settings import api_settings

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serialization for Profile models
    '''
    class Meta:
        model = Profile
        fields = ('balance', 
                'passport_number',   
                'accaunt')
        read_only_fields = ('balance', 'passport_number')


class UserDetailSerializer(serializers.ModelSerializer):
    '''
    Serialization for User Detail. Used nested relationships.
    '''
    user_information = ProfileSerializer()
    class Meta:
        model = User
        fields = ('first_name', 
                'last_name',
                'email',
                'user_information'
                )
    def update(self, instance, validated_data):
        '''
        Update and return an existing `User` instance, given the validated data.
        If user set accaunt = False, it can be hapened only once.
        in admin we can delete his profile. 
        '''
        profile_data = validated_data.pop('user_information')
        # Unless the application properly enforces that this field is
        # always set, the follow could raise a `DoesNotExist`, which
        # would need to be handled.
        user_information = instance.user_information
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        user_information.accaunt = validated_data.get('accaunt', user_information.accaunt)
        user_information.accaunt = False

        return instance

class UserSerializer(serializers.ModelSerializer):
    '''
    Serialization for User that can be show in UserListView. 
    Used nested relationships.
    '''
    user_information = ProfileSerializer()
    class Meta:
        model = User
        fields = ('first_name', 
                'last_name',   
                'username', 
                'password', 
                'email',
                'user_information'
                )


class UserCreateSerializer(serializers.HyperlinkedModelSerializer):
    '''
    Serialization for User while created.
    '''
    passport_number = serializers.CharField(source='user_information.passport_number')
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 
                'last_name', 
                'passport_number', 
                'username', 
                'password', 
                'email',)


    def create(self, validated_data):
        """
        Create and return a new `User` instance, given the validated data.
        """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'])
        user.save()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    '''
    Serialization for User login. 
    Implement and get jwt_token.
    '''
    token = serializers.CharField(allow_blank=True, read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('token',
                'username', 
                'password')

    def validate(self, data):
        user_obj = None
        username = data.get('username', None)
        password = data['password']

        if not username and not password:
            raise serializers.ValidationError('A username and password required to login.')
        user = User.objects.filter(
            Q(username=username) |
            Q(password=password)
            ).distinct()

        if user.exists() and user.count() == 1:
            user_obj = user.first()
        else:
            raise serializers.ValidationError('This username is not active.')

        if user_obj:
            if not user_obj.check_password(password):
                raise serializers.ValidationError('Incorrect password.')
        

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user_obj)
        token = jwt_encode_handler(payload)
        data['token'] = token
        return data

    
