from django.contrib import admin

# Register your models here.

from blog01 import models

# class MyAdmin(admin.ModelAdmin):
#     list_display = ('title','price','publish')
#     search_fields = ('title',)
#     list_filter = ('author','publish')
#     ordering = ('price',)

admin.site.register(models.Article)
admin.site.register(models.UserInfo)
admin.site.register(models.ArticleDetail)
admin.site.register(models.CommentUp)
admin.site.register(models.Comment)
admin.site.register(models.Category)
admin.site.register(models.Blog)
admin.site.register(models.UserFans)
admin.site.register(models.ArticleUpDown)
admin.site.register(models.Tag)
admin.site.register(models.Article2Tag)