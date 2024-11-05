from modeltranslation.translator import register, TranslationOptions
from .models import Position

@register(Position)
class PositionTranslationOptions(TranslationOptions):
    fields = ('name',)  
