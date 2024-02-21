

from rest_framework import serializers

from mobile.models import Mobiles

class MobileSerializers(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Mobiles
        fields="__all__"