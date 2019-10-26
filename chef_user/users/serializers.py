from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model


from rest_framework import serializers

User = get_user_model()

class MyRegisterSerializer(RegisterSerializer):
    name = serializers.CharField(required=True, write_only=True)

    def get_cleaned_data(self):
        super(MyRegisterSerializer, self).get_cleaned_data()
        return {
            'name': self.validated_data.get('name', ''),
            'password1': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        user.name = self.cleaned_data.get('name')
        adapter.save_user(request, user, self)
        user.save()
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id","email", "name"]
