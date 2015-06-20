__author__ = 'vladaoleynik'

from notes.models import Note, Tag, Category
from django.contrib.auth.models import User
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['pk', 'user', 'title', 'text', 'media', 'color', 'tag', 'category']

    def get_user(self, note):
        return note.user.username

    def get_tag(self, note):
        return [unicode(tag) for tag in note.tag.all()]

    def get_category(self, note):
        return [unicode(cat) for cat in note.category.all()]

    def create(self, validated_data):
        username = self.initial_data.get('user')
        cat = self.initial_data.get('category')
        tg = self.initial_data.get('tag')

        user = User.objects.get(username=username)
        categories = [
            cat for cat in Category.objects.filter(category__in=cat)
        ]
        tags = [
            tag for tag in Tag.objects.filter(tag__in=tg)
        ]

        note = Note.objects.create(
            user=user, **validated_data
        )
        note.tag.add(*tags)
        note.category.add(*categories)

        return note

    def update(self, instance, validated_data):
        instance.user = User.objects.get(username=self.initial_data.get('user'))
        instance.color = self.initial_data.get('color')
        instance.category = [
            cat for cat in Category.objects.filter(category__in=self.initial_data.get('category'))
        ]
        instance.tag = [
            tag for tag in Tag.objects.filter(tag__in=self.initial_data.get('tag'))
        ]

        instance.save()

        return instance


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['pk', 'category']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['pk', 'tag']


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'username', 'password']
