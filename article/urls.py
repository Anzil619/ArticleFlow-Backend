from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *



urlpatterns = [

    path('createarticle/', CreateArticle.as_view(), name='createarticle'),
    path('listcategory/', ListCategory.as_view(), name='listcategory'),
    path('getarticles/', GetArticles.as_view(), name='getarticles'),
    path('getuserarticles/<int:userid>/', GetUserArticle.as_view(), name='getuserarticles'),
    path('getuserpreference/<int:userid>/', GetUserPreference.as_view(), name='getuserpreference'),
    path('deletepreference/<int:pk>/', DeletePreference.as_view(), name='updatepreference'),
    path('createpreference/', CreatePreference.as_view(), name='createpreference'),
    path('user-interaction/', ArticleInteractions.as_view(), name='user-interaction'),


    

]