from rest_framework import serializers
from .models import Article, Categories,UserPreferences,UserInteraction
from accounts.serializers import UserSerializer



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class UserInteractionSerializer(serializers.ModelSerializer):
    class Meta:
        model=UserInteraction
        fields=('id','user','article','liked','disliked','blocked')

class ArticleSerializer(serializers.ModelSerializer):
    author = UserSerializer()  # Assuming UserSerializer is defined
    category = CategorySerializer()  # Assuming CategorySerializer is defined
    user_interactions = serializers.SerializerMethodField()
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()
    

    
    class Meta:
        model = Article
        fields = '__all__'

    def get_user_interactions(self, obj):
        user_interactions = UserInteraction.objects.filter(article=obj)
        serialized_interactions = UserInteractionSerializer(user_interactions, many=True).data
        return serialized_interactions
    
    def get_like_count(self, obj):
        return UserInteraction.objects.filter(article=obj, liked=True).count()
    def get_dislike_count(self, obj):
        return UserInteraction.objects.filter(article=obj, disliked=True).count()

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


