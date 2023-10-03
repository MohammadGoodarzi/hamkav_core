from django.shortcuts import get_object_or_404
import json

# from .models import Category,Category_type2,Category_type3


# def GetCategorisedLayoutsList():

#     root_categories = Category.get_root_nodes()
#     # print(root_categories)
#     # Convert root categories to the desired JSON format
#     category_hierarchy_json = [get_category_one_hierarchy(category, 'pi pi-folder', 'pi pi-th-large') for category in root_categories]
#     # category_hierarchy_in_model_json = [get_category_hierarchy_in_model(category,LayoutModel,"layout_category") for category in root_categories]
#     # print(category_hierarchy_in_model_json)
#     return  category_hierarchy_json
    
    
    
    
def get_category_hierarchy(category, category_icon, item_icon): 
    #هر کتگوری که به این تابع ارسال شود لیستش بدون عناصر وابسته لود میشود 
    
    result = {
        "key": str(category.pk),
        "label": category.name,
        "icon": category_icon,
        "data": "category"
    }

    children = []
    for child in category.get_children():                     
        # layout_children = [{"key": str(layout.uuid), "label": layout.title ,   "data": "item", "icon": item_icon} for layout in child.layout_category.all()]
        layout_children = []
        if layout_children:
            children.append({
                "key": str(child.id),
                "label": child.name,
                "icon": category_icon,
                "data": "category",
                "children": layout_children
            })
        else:
            children.append(get_category_hierarchy(child, category_icon, item_icon))

    if children:
        result["children"] = children

    return result


#============================================================

def get_category_hierarchy_in_model_relation(category,category_relation_name, category_icon, item_icon):
    result = {
        "key": str(category.pk),
        "label": category.name,
        "icon": category_icon,
        "data": "category"
    }
    children = []
    for child in category.get_children():                                     
        model_children = [{"key": str(model.uuid), "label": model.title ,   "data": "item", "icon": item_icon} 
                           for model in getattr(child,category_relation_name).all()]
        if model_children:
            children.append({
                "key": str(child.id),
                "label": child.name,
                "icon": category_icon,
                "data": "category",
                "children": model_children
            })
        else:
            children.append(get_category_hierarchy_in_model_relation(child, category_relation_name, category_icon, item_icon))
    if children:
        result["children"] = children
    return result