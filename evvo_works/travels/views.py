from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from travels.models import TravelRequest
from travels.serializers import TravelRequestSerializer, TravelRequestStatusSerializer

class TravelRequestViewSet(viewsets.ModelViewSet):
    queryset = TravelRequest.objects.all()
    serializer_class = TravelRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_admin():
            return TravelRequest.objects.all().order_by('-created_at')
        
        return TravelRequest.objects.filter(user=self.request.user).order_by('-created_at')

    def get_permissions(self):
        if self.action in ['update', 'partial_update']:
            return [IsAdminUser()]  
        return [IsAuthenticated()] 

    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def approve(self, request, pk=None):
        """Approve a travel request."""
        instance = self.get_object()
        print(request, request.data)
        serializer = TravelRequestStatusSerializer(instance, data={'status': 'approved'}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(detail=True, methods=['patch'], permission_classes=[IsAdminUser])
    def reject(self, request, pk=None):
        """Reject a travel request."""
        instance = self.get_object()
        serializer = TravelRequestStatusSerializer(instance, data={'status': 'rejected'}, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)