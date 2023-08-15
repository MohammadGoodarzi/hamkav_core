from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm,AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from django.contrib.auth.models import AbstractUser
from django.http import HttpResponseRedirect
from django.shortcuts import HttpResponse 
from django.shortcuts import redirect, reverse 




from django import forms
from django.db import models
# import geocoder  # not in Wagtail, for example only - https://geocoder.readthedocs.io/
from wagtail.admin.panels import FieldPanel
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.models import Page


class EventPageForm(WagtailAdminPageForm):
    address = forms.CharField()

    def clean(self):
        cleaned_data = super().clean()

        # Make sure that the event starts before it ends
        start_date = cleaned_data['start_date']
        end_date = cleaned_data['end_date']
        if start_date and end_date and start_date > end_date:
            self.add_error('end_date', 'The end date must be after the start date')

        return cleaned_data

    def save(self, commit=True):
        page = super().save(commit=False)

        # Update the duration field from the submitted dates
        page.duration = (page.end_date - page.start_date).days

        # Fetch the location by geocoding the address
        # page.location = geocoder.arcgis(self.cleaned_data['address'])

        if commit:
            page.save()
        return page


class EventPage(Page):
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    # location = models.CharField(max_length=255)

    content_panels = [
        FieldPanel('title'),
        FieldPanel('start_date'),
        FieldPanel('end_date'),
        FieldPanel('address'),
    ]
    base_form_class = EventPageForm
    
    
    
    # ============================main page     
class HomePage(Page):
    body = RichTextField(blank=True)

    
    def get_context(self, request, *args, **kwargs):
        context =  super().get_context(request, *args, **kwargs)
        return context
    
    content_panels = Page.content_panels+[
        FieldPanel('body'),
        ]

# class welcomePage(Page):
#     # HttpResponseRedirect("/blog")   
#     redirect('www.google.com') 

    
    
#=====================================================
#       Wagtail Models
#=====================================================
    
    
# # ============================main page     
# class HomePage(Page):
#     body = RichTextField(blank=True)
#     # body2 = RichTextField(blank=True)
    
#     def get_context(self, request, *args, **kwargs):
#         context =  super().get_context(request, *args, **kwargs)
#         # context = super(BlogIndexPage, self).get_context(request)
#         # productpage=self.get_children().type(ProductIndexPage)
#         product_index=self.get_children().exact_type(ProductIndexPage).first()
#         productpage=product_index.get_children().live().order_by('-first_published_at')
        
#         aboutPage = self.get_children().exact_type(AboutPageFa).live().order_by('-first_published_at')
       

#         # productpage=self.get_children().type(ProductIndexPage).get_children().type(ProductPage)
#         # productpage=self.get_children().live().order_by('-first_published_at')
#         context['productpage'] = productpage
#         context['aboutPage'] = aboutPage

#         return context
    
#     content_panels = Page.content_panels+[
#         FieldPanel('body'),
#         # FieldPanel('body2'),
#         ]

# #===========================about us page

# class AboutPageFa(Page):
#     # lastUpdateDate = models.DateField("Post date", null=True)
#     phone1 = models.CharField(max_length=50, null=True)
#     email = models.CharField(max_length=50, null=True)
#     address = models.CharField(max_length=250, null=True)
    
#     aboutUs = RichTextField(blank=True, null=True)
#     ourMission = RichTextField(blank=True, null=True)
#     ourVision = RichTextField(blank=True, null=True)
#     ourValues = RichTextField(blank=True, null=True)
    
    

#     def main_image(self):
#         gallery_item = self.gallery_images.first()
#         if gallery_item:
#             return gallery_item.image
#         else:
#             return None


#     # search_fields = Page.search_fields + [
#     #     index.SearchField('intro'),
#     #     index.SearchField('body'),
#     # ]

#     content_panels = Page.content_panels + [
#         FieldPanel('phone1'),
#         FieldPanel('address'),
#         FieldPanel('email'),
#         # FieldPanel('description'),
#         # FieldPanel('objectives'),
#         # FieldPanel('workingZone'),
#         InlinePanel('aboutus_gallery_images', label='افزودن کنار پاراگراف درباره ما'),
#         InlinePanel('brands_gallery_images', label='افزودن تصاویر برند ها '),
        
#         FieldPanel('aboutUs'),
#         FieldPanel('ourMission'),
#         FieldPanel('ourVision'),
#         FieldPanel('ourValues'),
#     ]
    
    
# class AboutUsGalleryImage(Orderable):
#     page = ParentalKey(AboutPageFa,on_delete=models.CASCADE, related_name = 'aboutus_gallery_images')
#     image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]   


# class BrandsGalleryImage(Orderable):
#     page = ParentalKey(AboutPageFa,on_delete=models.CASCADE, related_name = 'brands_gallery_images')
#     image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]  
    
        
    
# class BlogPageGalleryImage(Orderable):
#     page = ParentalKey(AboutPageFa,on_delete=models.CASCADE, related_name = 'gallery_images')
#     image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]


# #==========================contact page
# class ContactPage(Page):
#     contact_title = models.CharField(max_length=250, null=True)
#     contact_form_title = models.CharField(max_length=250, null=True)
#     contact_description = RichTextField(blank=True, null=True)
#     phone1 = models.CharField(max_length=50, null=True)
#     address = models.CharField(max_length=250, null=True)
#     email = models.CharField(max_length=250, null=True)
    
#     def main_image(self):
#         gallery_item = self.contact_gallery_images.first()     
#         if gallery_item:
#             return gallery_item.image
#         else:
#             return None
        
#     content_panels = Page.content_panels+[
#         FieldPanel('contact_title'),
#         FieldPanel('contact_description'),
#         FieldPanel('contact_form_title'),
#         FieldPanel('phone1'),
#         FieldPanel('address'),
#         FieldPanel('email'),
#         InlinePanel('contact_gallery_images', label='gallery images')
#     ]
    
    
#     def serve(self, request):                   # using django form in wagtail pages
#         from .forms import ContactForm 
#         from django.shortcuts import render
#         # from flavours.forms import FlavourSuggestionForm

#         if request.method == 'POST':
#             form = ContactForm(request.POST)
#             if form.is_valid():
#                 flavour = form.save()
#                 return render(request, 'home/contact_page.html', {
#                     'page': self,
#                     'flavour': flavour,
#                 })
#         else:
#             form = ContactForm()

#         return render(request, 'home/contact_page.html', {
#             'page': self,
#             'form': form,
#         })
        

# class ContactPageGalleryImage(Orderable):
#     page = ParentalKey(ContactPage,on_delete=models.CASCADE, related_name = 'contact_gallery_images')
#     image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]
    
    
    
        

        
        
        
    
# #========================== product page
# class ProductIndexPage(Page):
#     product_title = models.CharField(max_length=250, null=True)
    
#     # intro = RichTextField(blank=True)
#     # برای نمایش بر اساس ترتیب زمانی و 
#     # برای نمایش تنها موارد پابلیش شده
#     def get_context(self, request, *args, **kwargs):
#         context =  super().get_context(request, *args, **kwargs)
#         productpage=self.get_children().live().order_by('-first_published_at')
#         context['productpage'] = productpage
#         return context


#     content_panels = Page.content_panels + [
#         FieldPanel('product_title')
#     ]

# class ProductPage(Page):
#     product_title = models.CharField(max_length=250, null=True)
#     product_description = RichTextField(blank=True, null=True)
#     product_description_brife = RichTextField(blank=True, null=True)
#     product_specification = RichTextField(blank=True, null=True)

    
#     def main_image(self):
#         gallery_item = self.product_gallery_images.first()     
#         if gallery_item:
#             return gallery_item.image
#         else:
#             return None 
        
#     content_panels = Page.content_panels+[
#         FieldPanel('product_title'),
#         FieldPanel('product_description'),
#         FieldPanel('product_description_brife'),
#         FieldPanel('product_specification'),
#         InlinePanel('product_gallery_images', label='product gallery images'),
#     ]    
    
# class ProductPageGalleryImage(Orderable):
#     page = ParentalKey(ProductPage,on_delete=models.CASCADE, related_name = 'product_gallery_images')
#     image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name='+')
#     caption = models.CharField(blank=True, max_length=250)

#     panels = [
#         FieldPanel('image'),
#         FieldPanel('caption'),
#     ]  
    
    
#     #============================== contact email form
    
# class FormField(AbstractFormField):
#     page = ParentalKey('FormPage', on_delete=models.CASCADE, related_name='form_fields')
#     # page = ('ContactModel', on_delete=models.CASCADE, related_name='form_fields2')


# class FormPage(AbstractEmailForm):
#     intro = RichTextField(blank=True)
#     thank_you_text = RichTextField(blank=True)

#     content_panels = AbstractEmailForm.content_panels + [
#         FieldPanel('intro'),
#         InlinePanel('form_fields', label="Form fields"),
#         FieldPanel('thank_you_text'),
#         MultiFieldPanel([
#             FieldRowPanel([
#                 FieldPanel('from_address', classname="col6"),
#                 FieldPanel('to_address', classname="col6"),
#             ]),
#             FieldPanel('subject'),
#         ], "Email"),
#     ]
    
    