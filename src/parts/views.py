from rest_framework import viewsets
from .models import Part
from .serializers import PartSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from collections import Counter
import re


class PartViewSet(viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartSerializer

class CommonWordsView(APIView):
    def get(self, request):
        descriptions = Part.objects.values_list('description', flat=True)
        words = []

        for desc in descriptions:
            words += re.findall(r'\b\w+\b', desc.lower())  # divide por palavras

        common = Counter(words).most_common(5)
        return Response({word: count for word, count in common})
