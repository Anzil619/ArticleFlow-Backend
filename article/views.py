from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Article,Categories
from .serializers import ArticleSerializer,CategorySerializer

# Create your views here.



class CreateArticle(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)
    
    



class ListCategory(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer
    
