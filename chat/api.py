from rest_framework import generics

from .models import Message
from .serializers import MessageSerializer


class MessageList(generics.ListAPIView):
    serializer_class = MessageSerializer
    lookup_url_kwarg = 'page_number'

    def get_queryset(self):
        page_number = self.kwargs.get(self.lookup_url_kwarg)
        offset = page_number * 10
        return Message.objects.all()[offset:offset + 10]


class MessageSingle(generics.RetrieveAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()


class MessagePost(generics.CreateAPIView):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
