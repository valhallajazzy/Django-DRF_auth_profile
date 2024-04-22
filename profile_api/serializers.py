from rest_framework import serializers
from profile_api.models import User

import phonenumbers


class NumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number',]

    def validate(self, data):
        try:
            parse_number = phonenumbers.parse(data['phone_number'])
        except phonenumbers.phonenumberutil.NumberParseException:
            raise serializers.ValidationError("Phone number is not valid")
        if not phonenumbers.is_valid_number_for_region(parse_number, 'RU'):
            raise serializers.ValidationError("The entered phone number is not valid for region Russia")
        return super().validate(data)


class CodeAndNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone_number', 'code',]

    def validate(self, data):
        user = User.objects.filter(phone_number=data['phone_number'])
        if not user.exists():
            raise serializers.ValidationError("The entered phone number is not exists")
        if user.code != data['phone_number']:
            raise serializers.ValidationError("The entered code is not valid")
        return super().validate(data)