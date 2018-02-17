from django import forms
from .models import Comment,ReplyComment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('commmentText',)
        widgets = {
        'commmentText': forms.Textarea(attrs={'cols': 40, 'rows': 3}),
        
        }

class ReplyForm(forms.ModelForm):
    
    class Meta:
        model = ReplyComment
        fields = ('replyText',)
        widgets = {
        'replyText': forms.Textarea(attrs={'cols': 20, 'rows': 3}),
        
        }
        

        
