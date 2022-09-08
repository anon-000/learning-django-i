from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Demo API View"""

    def get(self, request, format=None):
        """Returns list of API views features"""

        api_view = [
            'This have many mehtods like get, put , patch, post, delete',
            'Is similar to django view',
            'gives you superpower of customisaation',
            'mapped manually with urls'
        ]

        return Response({'message': 'Hello!', 'api_view': api_view})
        

