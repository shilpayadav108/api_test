from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class MyntraAPI(APIView):
    def post(self, request):
        keywords = request.data['keywords']

        # return Response({"keyword": keywords})
        return Response({"keyword": keywords}, status=status.HTTP_201_CREATED)