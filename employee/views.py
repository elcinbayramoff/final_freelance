# employee/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Employee
from .serializers import EmployeeSerializer
from .permissions import IsAdminOrReadOnly, IsAdminForCreate

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly, IsAdminForCreate]

    def create(self, request, *args, **kwargs):
        """Handle creating a new employee"""
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None, *args, **kwargs):
        """Retrieve a specific employee by ID"""
        employee = self.get_object()
        serializer = self.get_serializer(employee)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        """List all employees"""
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, pk=None, *args, **kwargs):
        """Update a specific employee"""
        employee = self.get_object()
        serializer = self.get_serializer(employee, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, pk=None, *args, **kwargs):
        """Delete a specific employee (Admin-only)"""
        employee = self.get_object()
        self.perform_destroy(employee)
        return Response({"message": "Employee deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
