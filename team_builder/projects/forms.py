from django import forms
from . import models


class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = [
            "name",
            "description",
            "timeline",
            "requirements"
        ]


class PositionForm(forms.ModelForm):
    class Meta:
        model = models.Position
        fields = [
            "title",
            "description",
            "skill",
            "position_filled"
        ]


PositionFormSet = forms.modelformset_factory(
    models.Position,
    form=PositionForm,
)


PositionInlineFormSet = forms.inlineformset_factory(
    models.Project,
    models.Position,
    fields=('title', 'description', 'skill', 'position_filled', ),
    formset=PositionFormSet,
    can_delete=True,
    extra=2,
)