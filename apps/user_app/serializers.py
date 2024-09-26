from django.contrib.auth.models import User
from rest_framework import serializers

def admin_in_value(value):
    if 'admin' in value.lower():
        raise serializers.ValidationError("Can't be use Admin in value")
    return value

# def clean_value(value):
#     if 'admin' in value.lower():
#         raise serializers.ValidationError("Can't be use Admin in value")
#     return value

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        
        extra_kwargs = {
            'password':{'write_only':True},
            'username':{'validators':[admin_in_value]},
            'email':{'validators':[admin_in_value]},
                        }