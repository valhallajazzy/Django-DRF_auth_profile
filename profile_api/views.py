import string

from rest_framework.views import APIView
from rest_framework.response import Response
from profile_api.serializers import NumberSerializer, CodeAndNumberSerializer


from profile_api.models import User
import random


class PhoneNumberAPIView(APIView):
    def post(self, request):
        serializer = NumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        possible_user = User.objects.filter(phone_number=request.data['phone_number'])
        random_code = ''.join([random.choice(list('123456789')) for _ in range(4)])
        if not possible_user.exists():
            invite_code = self.generate_invite_code()
            new_user = User.objects.create(
                phone_number=request.data['phone_number'],
                code=random_code,
                shared_invite_code=invite_code
            )
            return Response({"id": new_user.id, "code": int(new_user.code)})
        possible_user.update(code=random_code)
        return Response({"id": possible_user[0].id, "code": int(possible_user[0].code)})

    def generate_invite_code(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        invite_code = ''.join(random.choice(characters) for _ in range(6))
        return invite_code


class SignInAPIView(APIView):
    def post(self, request):
        serializer = CodeAndNumberSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(phone_number=request.data['phone_number'])
        who_was_ivited = User.objects.filter(friend_invite_code=user.shared_invite_code)

        personal_data = {
            'id': user.id,
            'phone_number': user.phone_number,
            'shared_invite_code': user.shared_invite_code,
            'friend_invite_code': user.friend_invite_code,
            'who_was_invited': [friend.phone_number for friend in who_was_ivited]
        }
        return Response({'personal_data': personal_data})

