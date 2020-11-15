from rest_framework import viewsets
from rest_framework import filters

from crm.serializers import *


class CommonViewSet(viewsets.ModelViewSet):
    """
    ViewSet provides common behavior for all endpoints
    """

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        return self.list(request)


class RoleViewSet(CommonViewSet):
    """
    API-endpoint for all actions with Roles
    """

    serializer_class = RoleSerializer
    queryset = Role.objects.all()


class EmployeeViewSet(CommonViewSet):
    """
    API-endpoint for all actions with Employees
    """

    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ('role__name', )


class CompanyViewSet(CommonViewSet):
    """
    API-endpoint for all actions with Companies
    """

    serializer_class = CompanySerializer
    queryset = Company.objects.all()



