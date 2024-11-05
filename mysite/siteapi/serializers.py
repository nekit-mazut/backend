from rest_framework import serializers
from .models import CustomUser, Site, Page


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email']


class SiteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Site
        fields = ['id', 'name', 'created_at', 'user']


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'site', 'title', 'html_content', 'css_content', 'js_content', 'created_at']
