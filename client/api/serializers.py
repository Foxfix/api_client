from django.contrib.auth import get_user_model
from django.db.models import Q
from rest_framework import serializers
from ..models import Profile

User = get_user_model()


class ProfileSerializer(serializers.ModelSerializer):
    '''
    Serialization for Profile models
    '''
    class Meta:
        model = Profile
        fields = ('balance', 
                'passport_number', 
                'accaunt'  
                )
        read_only_fields = ('balance',)

    def update(self, instance, validated_data):        
        profile_data = validated_data.pop('user_information')
        instance.accaunt = validated_data.get('accaunt', instance.accaunt)
        instance.save()
        return instance


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
                'user_information',
                )

    def update(self, instance, validated_data):
        '''
        Update and return an existing `User` instance, given the validated data.
        If user set accaunt = False, it can be hapened only once.
        in admin we can delete his profile. 
        '''
        profile_data = validated_data.pop('user_information')
        user_information = instance.user_information
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        
        user_information.passport_number = profile_data.get('passport_number', user_information.passport_number)
        user_information.accaunt = profile_data.get('accaunt', user_information.accaunt)
        if user_information.accaunt == 'Close':
            instance.is_active = False
            instance.save()
        user_information.save()

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
                'id',
                'user_information',                
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
    username = serializers.CharField()
    password = serializers.CharField()

    class Meta:
        model = User
        fields = ('username', 
                'password')

    def validate(self, data):
        user_obj = None
        email = data.get("email", None)
        username= data.get("username", None)
        password = data["password"]
        if not email and not username:
            raise ValidationError('A username or email is required to login.')
        user = User.objects.filter(
            Q(email=email) |
            Q(username=username)
            ).distinct()
        if user.exists() and user.count() == 1:
           user = user.first()
        else:
            raise ValidationError("This username/email is not valid.")
        if user_obj:
            if not user_obj.check_password(password):
                raise ValidationError("Incorrect credentials please try again..")
        return data



