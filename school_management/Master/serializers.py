from rest_framework import serializers
from .models import CountryMaster, UserMaster, ReferalMaster, StateMaster, BankMaster, GenderMaster, DocumentMaster



class CountrySerializer(serializers.ModelSerializer):
	class Meta:
		model = CountryMaster
		fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserMaster
        fields = '__all__'

class ReferalSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReferalMaster
        fields = '__all__'

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateMaster
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankMaster
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = GenderMaster
        fields = '__all__'

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentMaster
        fields = '__all__'
