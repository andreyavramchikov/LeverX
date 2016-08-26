from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import login

from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializer import LoginSerializer
from .models import User


class AccountViewSet(viewsets.ModelViewSet):
    lookup_field = 'pk'
    queryset = User.objects.all()
    serializer_class = LoginSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            user = User.objects.create_user(**serializer.validated_data)
            login(request, user)
            return Response(serializer.validated_data, status=status.HTTP_201_CREATED)

        return Response({
            'status': _('Bad request'),
            'message': _('Account could not be created with received data.'),
        }, status=status.HTTP_400_BAD_REQUEST)



