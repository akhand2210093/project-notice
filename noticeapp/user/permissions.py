from rest_framework.permissions import BasePermission

class IsAdministrator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'administrator'

class IsStaff(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'staff'

class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'student'