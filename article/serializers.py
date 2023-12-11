from rest_framework import serializers
from .models import Article, Categories,UserPreferences
from accounts.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()  # Nested serializer for author
    category = CategorySerializer()  # Nested serializer for category

    class Meta:
        model = Article
        fields = '__all__'

class CreateArticleSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

class GetUserPreferences(serializers.ModelSerializer):
    preference = CategorySerializer()
    class Meta:
        model = UserPreferences
        fields = '__all__'


class UserPreferencesSerializers(serializers.ModelSerializer):
    class Meta:
        model = UserPreferences
        fields = '__all__'