from django.contrib import admin
from .models import Article,Categories,UserInteraction,UserPreferences


admin.site.register(Article)
admin.site.register(Categories)
admin.site.register(UserInteraction)
admin.site.register(UserPreferences)


