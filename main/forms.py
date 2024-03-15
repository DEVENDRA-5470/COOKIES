from main.imports import *
class sign_form(forms.ModelForm):

    class Meta:
        model = User
        fields=['username',"email",'password']