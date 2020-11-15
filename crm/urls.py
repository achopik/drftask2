from rest_framework import routers

from crm.views import *


"""
Endpoint routing
"""


router = routers.SimpleRouter()
router.register(r'roles', RoleViewSet, basename='role')
router.register(r'employees', EmployeeViewSet, basename='employee')
router.register(r'companies', CompanyViewSet, basename='company')

urlpatterns = router.urls
