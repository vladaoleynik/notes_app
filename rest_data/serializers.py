__author__ = 'vladaoleynik'

from models import Note, Tag, Category, Color, UserSettings
from django.contrib.auth.models import User
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['pk', 'user', 'title', 'text', 'media', 'color', 'tag', 'category']

    def get_user(self, note):
        return note.user.username

    def get_tag(self, note):
        return [unicode(tag) for tag in note.tag.all()]

    def get_category(self, note):
        return note.category.category

    def get_color(self, note):
        return note.color.color

    def create(self, validated_data):
        username = self.initial_data.get('user')
        cat = self.initial_data.get('category')
        tg = self.initial_data.get('tag')
        clr = self.initial_data.get('color')

        user = User.objects.get(username=username)
        category = Category.objects.get(category=cat)
        color, created = Color.objects.get_or_create(color=clr, defaults={'status': 'user'})
        tags = [
            tag for tag in Tag.objects.filter(tag__in=tg)
        ]

        note = Note.objects.create(
            user=user, category=category, color=color, **validated_data
        )
        note.tag.add(*tags)

        return note

    def update(self, instance, validated_data):
        instance.user = User.objects.get(username=self.initial_data.get('user'))
        instance.title = validated_data['title']
        instance.text = validated_data['text']
        instance.color = Color.objects.get(color=self.initial_data.get('color'))
        instance.category = Category.objects.get(category=self.initial_data.get('category'))
        instance.tag = [
            tag for tag in Tag.objects.filter(tag__in=self.initial_data.get('tag'))
        ]
        instance.media = validated_data['media']
        instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['pk', 'category', 'status']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['pk', 'tag', 'status']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'password']


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['pk', 'color', 'status']


class SettingsSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = UserSettings
        fields = ['user', 'color', 'category', 'tag']

    def get_user(self, object):
        return object.user.username

    def get_tag(self, object):
        return [unicode(tag) for tag in object.tag.all()]

    def get_category(self, object):
        return [unicode(category) for category in object.category.all()]

    def get_color(self, object):
        return [unicode(color) for color in object.color.all()]

    def update(self, instance, validated_data):
        instance.color = [
            color for color in Color.objects.filter(color__in=self.initial_data.get('color'))
        ]
        instance.category = [
            category for category in Category.objects.filter(category__in=self.initial_data.get('category'))
        ]
        instance.tag = [
            tag for tag in Tag.objects.filter(tag__in=self.initial_data.get('tag'))
        ]

        instance.save()

        return instance
