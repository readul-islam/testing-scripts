from rest_framework import serializers
from api.models import Company


# create serializers here
class companySerializer(serializers.HyperlinkedModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        # fields = ('company_id', 'name', 'location', 'about', 'type', 'added_date', 'active')
        fields= "__all__"
    

