from rest_framework.views import APIView
from rest_data.serializers import NoteSerializer
from notes.models import Note
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class NoteListApi(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        queryset = Note.objects.all()
        res = NoteSerializer(queryset, many=True)
        return Response(res.data)


class AuthorNoteListApi(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        queryset = Note.objects.filter(user__username=username)
        res = NoteSerializer(queryset, many=True)
        print res.data
        return Response(res.data)

    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class NoteApi(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        note = kwargs['note_id']
        try:
            queryset = Note.objects.filter(user__username=username)[int(note)-1]
        except IndexError:
            return Response([])
        res = NoteSerializer(queryset)
        return Response(res.data)

    def post(self, request, *args, **kwargs):
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            print('after')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)