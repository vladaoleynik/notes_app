__author__ = 'vladaoleynik'

from notes.models import Note, Tag, Category, Color
from django.contrib.auth.models import User
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['pk', 'user', 'title', 'text', 'media', 'color', 'tag', 'category']

    def get_user(self, note):
        return note.user.username

    def get_color(self, note):
        return note.color.color

    def get_tag(self, note):
        return [unicode(tag) for tag in note.tag.all()]

    def get_category(self, note):
        return [unicode(cat) for cat in note.category.all()]

    def create(self, validated_data):
        username = self.initial_data.get('user')
        clr = self.initial_data.get('color')
        cat = self.initial_data.get('category')
        tg = self.initial_data.get('tag')

        user = User.objects.get(username=username)
        color = Color.objects.get(color=clr)
        categories = [
            cat for cat in Category.objects.filter(category__in=cat)
        ]
        tags = [
            tag for tag in Tag.objects.filter(tag__in=tg)
        ]

        note = Note.objects.create(
            user=user, color=color, **validated_data
        )
        note.tag.add(*tags)
        note.category.add(*categories)

        return note

    def update(self, instance, validated_data):
        username = self.initial_data.get('user')
        clr = self.initial_data.get('color')
        cat = self.initial_data.get('category')
        tg = self.initial_data.get('tag')

        instance.user = self.initial_data.get('user', User.objects.get(username=username))
        instance.color = self.initial_data.get('color', Color.objects.get(color=clr))
        instance.category = self.initial_data.get('category', [
            cat for cat in Category.objects.filter(category__in=cat)
        ])
        instance.tag = self.initial_data.get('tag', [
            tag for tag in Tag.objects.filter(tag__in=tg)
        ])

        instance.save()

        return instance


class ColorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Color
        fields = ['color']


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['category']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['tag']
