from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from profiles_api import serializers


# Create your views here.
class HelloApiView(APIView):
    # Test api view
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        # Returns a list of APIView features
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'gives the most control over your application',
            'is mapped manually to urls'
        ]
        return Response({'message': "hello", 'an_apiview': an_apiview})

    def post(self, request):
        # Create a hello message with our name
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello my name is {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        # Handle updating objects
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        # Handle a partial update of an objects
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        # Deleting an objects
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    # Test API Viewset
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        # Return a hello message

        a_viewset = [
            'uses action',
            '(list,create,retrieve update,partial_update)'
            'automatically maps to URls using Routers',
            'provies more funtionality with less code',
        ]
        return Response({"message": 'hello', "a_viewset": a_viewset})

    def create(self, request):
        # create a new message
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})

        else:
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    def retrieve(self, request, pk=None):
        # Handle getting an object by its id
        return Response({'http_method': "GET"})

    def update(self, request, pk=None):
        # Handle updateing an objects
        return Response({'http_method': "PUT"})

    def partial_update(self, request, pk=None):
        # Handle updaeting part of an objects
        return Response({'http_method': "PATCH"})

    def destroy(self, request, pk=None):
        # Handle deleting an objects
        return Response({'http_method': "DELETE"})
