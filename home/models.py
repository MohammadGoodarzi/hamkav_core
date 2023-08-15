from django.db import models
from wagtail.models import Page, Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, InlinePanel, FieldRowPanel, MultiFieldPanel
from wagtail.search import index
from modelcluster.fields import ParentalKey
from wagtail.contrib.forms.models import AbstractEmailForm,AbstractFormField
from wagtail.contrib.forms.panels import FormSubmissionsPanel
from django.contrib.auth.models import AbstractUser




from django import forms
from django.db import models
# import geocoder  # not in Wagtail, for example only - https://geocoder.readthedocs.io/
from wagtail.admin.panels import FieldPanel
from wagtail.admin.forms import WagtailAdminPageForm
from wagtail.models import Page




from .wagtail_models import *




  
#=====================================================
#       Django Models
#=====================================================

class ContactModel(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255)
    # subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=11, null=True)
    message = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    mupdated_date = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ('created_date',)
        # verbose_name = _("")
        # verbose_name_plural = _("s")

    def __str__(self):
        return self.full_name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})



#=====================================================
#      Customize User Model
#=====================================================

# class User(AbstractUser):
#     country = models.CharField(verbose_name='country', max_length=255)
#     status = models.ForeignKey(MembershipStatus, on_delete=models.SET_NULL, null=True, default=1)