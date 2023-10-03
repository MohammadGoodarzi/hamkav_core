from ninja import Router
# from . api_views import GetCategorisedLayoutsList
from .models import Category,Category_type2,Category_type3
from .api_views import get_category_hierarchy




router = Router()

@router.get("/type_one_cat_list")
def GetCategory_type_one_list(request):
    root_categories = Category.get_root_nodes()
    category_hierarchy_json = [get_category_hierarchy(category, 'pi pi-folder', 'pi pi-th-large') for category in root_categories]
    res = category_hierarchy_json
    # print(res)
    return  res


