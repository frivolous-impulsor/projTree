from django.contrib import admin
from .models import Post, Seed, Step

# Register your models here.
admin.site.register(Post)
admin.site.register(Seed)
admin.site.register(Step)