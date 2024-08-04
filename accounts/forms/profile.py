from django import forms

from ..models.profile import Profile


class ProfileForm(forms.ModelForm):
    birth_date = forms.DateField(
        widget=forms.TextInput(attrs={"class": "form-control", "type": "date"})
    )

    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["user", "created_at", "updated_at", "is_active"]

    # fix bio field more responsive
    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["bio"].widget.attrs["rows"] = 4
        self.fields["bio"].widget.attrs["cols"] = 15
