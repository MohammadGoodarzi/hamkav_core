from ninja import Router
from .models import User
import uuid
from ninja_jwt.authentication import JWTAuth  # jwt


router = Router()

@router.get('/')
def list_users(request):
    return [
        {"id": u.id, "full_name":u.full_name, "phone_number":u.phone_number, "user_uuid":u.user_uuid}
        for u in User.objects.all()
    ]

@router.get('/{id}')
def user_detail(request, id: int):
    user = User.objects.get(id = id)
    return {"id": user.id, "full_name":user.full_name, "phone_number":user.phone_number, "user_uuid":user.user_uuid}