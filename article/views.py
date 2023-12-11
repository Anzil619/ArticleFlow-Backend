from django.shortcuts import render
from rest_framework.generics import CreateAPIView,ListCreateAPIView,DestroyAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from .models import Article,Categories,UserPreferences
from .serializers import ArticleSerializer,CategorySerializer,CreateArticleSerialzer,UserPreferencesSerializers,GetUserPreferences
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework import status

# Create your views here.



class CreateArticle(CreateAPIView):
    queryset = Article.objects.all()
    serializer_class = CreateArticleSerialzer
    permission_classes = (AllowAny,)
    
    



class ListCategory(ListCreateAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategorySerializer


class GetArticles(APIView):
    serializer_class = ArticleSerializer
    permission_classes = (AllowAny,)

    def get(self, request, *args, **kwargs):
        category_ids = request.GET.getlist('category_ids', [])

        ids_string = category_ids[0]  
        ids_list = ids_string.split(',')  

        # print(category_ids,"anzil")
        category_ids = [int(id) for id in ids_list if id.isdigit()]
        print(category_ids,"anzil")


        if not category_ids:
            articles = Article.objects.all()
            print("hi")
        else:
            query = Q()
            for category_id in category_ids:
                query |= Q(category_id=category_id)

            articles = Article.objects.filter(query)
           

        serializer = self.serializer_class(articles, many=True)
        return Response(serializer.data)
    

class GetUserArticle(ListCreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ArticleSerializer
    def get_queryset(self):
        userid = self.kwargs.get('userid') 
        queryset = Article.objects.filter(author__id=userid)  
        return queryset



class GetUserPreference(ListCreateAPIView):
    permission_classes = (AllowAny,)

    serializer_class = GetUserPreferences
    def get_queryset(self):
        userid = self.kwargs.get('userid') 
        queryset = UserPreferences.objects.filter(user__id=userid)  
        return queryset

class DeletePreference(DestroyAPIView):
    serializer_class = UserPreferencesSerializers
    queryset = UserPreferences.objects.all()

  
class CreatePreference(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserPreferencesSerializers  
    queryset = UserPreferences.objects.all()
    

