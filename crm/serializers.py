from rest_framework import serializers

from crm.models import *


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for a Role model
    """
    class Meta:
        model = Role
        fields = ('url', 'id', 'name', 'description')


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for an Employee model
    """

    role = serializers.SlugRelatedField(queryset=Role.objects.all(), slug_field='name', label='Профессия')
    company = serializers.SlugRelatedField(queryset=Company.objects.all(), slug_field='name', label='Компания')

    class Meta:
        model = Employee
        fields = (
            'url',
            'id',
            'name',
            'age',
            'gender',
            'phone_number',
            'role',
            'company'
        )


class PartnerSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for a Company short representation in partners list
    """
    class Meta:
        model = Company
        fields = (
            'url',
            'name',
        )


class CompanySerializer(serializers.ModelSerializer):
    """
    Serializer for a Company model
    """

    employees = EmployeeSerializer(many=True, read_only=True)
    partners = PartnerSerializer(many=True, read_only=True)
    partners_write = serializers.SlugRelatedField(queryset=Company.objects.all(),
                                                  many=True,
                                                  slug_field='name',
                                                  label='Партнеры',
                                                  write_only=True)

    class Meta:
        model = Company
        fields = (
            'url',
            'id',
            'name',
            'address',
            'foundation_date',
            'type',
            'employees',
            'partners',
            'partners_write'
        )
