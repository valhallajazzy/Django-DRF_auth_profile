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
        if user[0].code != data['code']:
            raise serializers.ValidationError("The entered code is not valid")
        return super().validate(data)


class InviteCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['friend_invite_code', 'phone_number',]

    def validate(self, data):
        user = User.objects.filter(phone_number=data['phone_number'])
        inviting_user = User.objects.filter(shared_invite_code=data['friend_invite_code'])
        if not user.exists():
            raise serializers.ValidationError("The entered phone number is not exists")
        if not inviting_user.exists():
            raise serializers.ValidationError("Invalid invite code")
        if user[0].shared_invite_code == data['friend_invite_code']:
            raise serializers.ValidationError("You can't use your invite code")
        if user[0].friend_invite_code:
            raise serializers.ValidationError("You can use invite code only once")
        return super().validate(data)


class ActiveStatusSerializer(NumberSerializer):
    class Meta:
        model = User
        fields = ['phone_number',]

    def validate(self, data):
        super().validate(data)
        user = User.objects.filter(phone_number=data['phone_number'])
        if not user.exists():
            raise serializers.ValidationError("The entered phone number is not exists in system")
        if user.first().is_active is False:
            raise serializers.ValidationError("User is not active")
        return super().validate(data)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
