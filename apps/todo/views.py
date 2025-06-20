
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializer

# create the view set for the Todo Serializer
class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

    # this shoiuld be a put...  not sure yet how to impl that in DRF
    @action(detail=True, methods=['get'])
    def set_complete(self, request, pk=None):
        # make the item complete
        item:Todo = self.get_object()
        # write to db
        item.set_complete()

        return Response({'result':True})

