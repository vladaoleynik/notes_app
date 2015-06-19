__author__ = 'vladaoleynik'

from notes.models import Note
from django.contrib.auth.models import User
from rest_framework import serializers


class NoteSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    color = serializers.SerializerMethodField()
    tag = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()

    class Meta:
        model = Note
        fields = ['user', 'title', 'text', 'media', 'color', 'tag', 'category']

    def get_user(self, note):
        return note.user.username

    def get_color(self, note):
        return note.color.color

    def get_tag(self, note):
        return [unicode(tag) for tag in note.tag.all()]

    def get_category(self, note):
        return [unicode(cat) for cat in note.category.all()]

    def create(self, validated_data):
        username = validated_data.pop('username')
        clr = validated_data.pop('color')
        cat = validated_data.pop('category')
        tg = validated_data.pop('tag')
        user = User.objects.get(username=username)
        color = Note.objects.get(color__color__in=clr)
        category = [cat for cat in Note.objects.filter(category__in=cat)]
        tag = [tag for tag in Note.objects.filter(tag__in=tg)]
        print user, color, category, tag
        return Note.objects.create(user=user, color=color, tag=tag, category=category, **validated_data)