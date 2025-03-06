from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Explore, Search

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password', 'is_verified']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data)
        user.generate_verification_token()
        return user

class ExploreSerializer(serializers.ModelSerializer):
    image_url = serializers.ReadOnlyField()

    class Meta:
        model = Explore
        fields = ['id', 'title', 'description', 'category', 'image_url']

class SearchSerializer(serializers.ModelSerializer):
    search_image = serializers.URLField(read_only=True)

    class Meta:
        model = Search
        fields = '__all__'