from ninja import Router
from . api_views import GetCategorisedLayoutsList



router = Router()

@router.get("/type_one_cat_list")
def GetCategory_type_one_list(request):
    
    res = GetCategorisedLayoutsList()
    # print(res)
    return  res


