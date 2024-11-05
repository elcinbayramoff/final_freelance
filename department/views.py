# department/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Department
from .serializers import DepartmentSerializer
from .permissions import IsAdminOrReadOnly

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

    def create(self, request, *args, **kwargs):
        """Handle creating a new department"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Retrieve a specific department by ID"""
        department = self.get_object()
        serializer = self.get_serializer(department)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """List all departments"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """Update a specific department"""
        department = self.get_object()
        serializer = self.get_serializer(department, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete a specific department (Admin-only)"""
        department = self.get_object()
        self.perform_destroy(department)
        return Response({"message": "Department deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
