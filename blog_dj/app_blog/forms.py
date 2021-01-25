from ckeditor.widgets import CKEditorWidget
from .models import Post
from django import  forms


class  PostForm(forms.ModelForm):
    #title = forms.CharField(max_length=100)
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Post
        fields = fields = ('title','content','image','status','category') 