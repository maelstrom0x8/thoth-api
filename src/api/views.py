from rest_framework import generics, status
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers


class LogListView(generics.ListAPIView):
    queryset = models.LogEntry.objects.all()
    serializer_class = serializers.LogEntrySerializer


class LogDetailView(generics.RetrieveAPIView):

    def get_queryset(self):
        log_id = self.request.query_params.get('log_id')
        queryset = models.LogEntry.objects.filter(log_id=log_id)

        return queryset


class CreateNewEntry(generics.CreateAPIView):

    def post(self, request: Request, *args, **kwargs):
        subject = request.data.get('subject')
        body = request.data.get('body')
        data = {'subject': subject, 'body': body}
        serializer = serializers.LogEntrySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
