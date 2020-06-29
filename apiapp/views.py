from rest_framework.response import Response
from rest_framework import generics
from . models import PredResults
from . serializers import PredSerializer
import pandas as pd

# RetrieveAPIView - used for read-only endpoints to represent a single model instance.
# https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview


class PostsView(generics.ListCreateAPIView):

    serializer_class = PredSerializer

    def get(self, request, *args, **kwargs):

        sepal_length = float(self.request.GET.get('sepal_length'))
        sepal_width = float(self.request.GET.get('sepal_width'))
        petal_length = float(self.request.GET.get('petal_length'))
        petal_width = float(self.request.GET.get('petal_width'))

        model = pd.read_pickle(r"C:\Users\azander\Downloads\new_model.pickle")
        result = model.predict(
            [[sepal_length, sepal_width, petal_length, petal_width]])

        classification = result[0]

        serializer = PredSerializer(data=self.request.GET)
        if serializer.is_valid():
            serializer.save()
            return Response(result[0])
        return Response(serializer.errors, status=400)
