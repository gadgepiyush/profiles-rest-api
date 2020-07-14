from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
class HelloApiView(APIView):
    # Test api view

    def get(self, request, format=None):
        # Returns a list of APIView features
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'is similar to a traditional Django view',
            'gives the most control over your application',
            'is mapped manually to urls'
        ]
        return Response({'message': "hello", 'an_apiview': an_apiview})
