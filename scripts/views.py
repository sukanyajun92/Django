__author__ = 'suksubra'

from .models import chassisInfo
from rest_framework import status
from .serializers import chassisSerializer
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView


class chassisList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'chassis_list.html'

    def get(self, request):
        queryset = chassisInfo.objects.all()
        #serializer = chassisSerializer(queryset)
        return Response({'chassis': queryset})

