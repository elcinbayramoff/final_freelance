from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Position
from .serializers import PositionSerializer
from .permissions import IsAdminOrReadOnly

class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        """Handle creating a new position"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Retrieve a specific position by ID"""
        position = self.get_object()
        serializer = self.get_serializer(position)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """List all positions"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """Update a specific position"""
        position = self.get_object()
        serializer = self.get_serializer(position, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete a specific position (Admin-only)"""
        position = self.get_object()
        self.perform_destroy(position)
        return Response({"message": "Position deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
