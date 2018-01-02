#from models import User, UserLogging
from rest_framework import serializers
from models import UserLogging

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ('Quick_Id', 'Name','Phone')


class UserLoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserLogging
        fields = ('Talker_Id', 'last_Logging_Time','Talker_Status')
        