from modeltranslation.translator import register, TranslationOptions
from .models import Department

@register(Department)
class DepartmentTranslationOptions(TranslationOptions):
    fields = ('name',)
