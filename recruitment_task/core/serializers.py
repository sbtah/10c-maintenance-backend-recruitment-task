from rest_framework import serializers

from core.models import Project, Investor


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"
        read_only_field = ["funded", "funded_by"]


class InvestorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Investor
        fields = "__all__"
        read_only_fields = ["remaining_amount"]


# Added list_inventors for listing Investors that can match with Project.
class ProjectDetailsSerializer(serializers.ModelSerializer):

    list_investors = serializers.ListField(required=False)

    class Meta:
        model = Project
        fields = "__all__"
        read_only_fields = ["funded", "funded_by", "list_investors"]
        

# Added list_projects for listing Projects that can match with Investor. 
class InvestorDetailsSerializer(serializers.ModelSerializer):

    list_projects = serializers.ListField(required=False)
   
    class Meta:
        model = Investor
        fields = "__all__"
        read_only_fields = ["remaining_amount", "list_projects "]