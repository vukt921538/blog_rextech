from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from home.models import Profile, Post, CommentPost, Comment_to_comment
from django.contrib.auth.models import User

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập...'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Nhập mật khẩu...'}))

class RegistrationForm(UserCreationForm):
    f_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ...'}))
    l_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên...'}))
    username = forms.CharField(
                    help_text='Tên đăng nhập bao gồm các kí tự và số, không bao gồm kí tự đặc biệt',
                    label='Tên đăng nhập', widget=forms.TextInput(
                        attrs={'class': 'form-control', 'placeholder': 'Tên đăng nhập...'})
                        )
    password1 = forms.CharField(
                    help_text='Mật khẩu nhiều hơn 8 ký tự',
                    label = 'Password*', 
                    widget=forms.PasswordInput(
                        attrs={'class': 'form-control', 'placeholder': 'Mật khẩu...'})
                        )
    password2 = forms.CharField(help_text='(*)Hai trường mật khẩu không được khác nhau',
        label = 'Password confirmation*', widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Xác nhận mật khẩu...'}))
    class Meta:
        model = User
        fields = ('f_name', 'l_name', 'username', 'password1', 'password2')

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=True)
        user_create = Profile.objects.create(user=user, f_name=self.cleaned_data['f_name'], l_name=self.cleaned_data['l_name'])
        if commit:
            user.save()
            user_create.save()
        return user


class UpdateProfileForm(forms.ModelForm):
    f_name = forms.CharField(label='First name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Họ...'}))
    l_name = forms.CharField(label='Last name', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tên...'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com ...'}), required=False)
    address = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Địa chỉ...'}), required=False)
    dob = forms.DateField(label='Date of birth',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-mm-dd...'}), required=False)
    job = forms.CharField(label='Job',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nghề nghiệp...'}), required=False)
    descriptions = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Thêm mô tả...'}), required=False)
    class Meta:
        model = Profile
        fields = ('f_name', 'l_name', 'email', 'address', 'dob', 'job', 'descriptions')
        widgets = {'user': forms.HiddenInput()}

class AvataForm(forms.ModelForm):
    img = forms.ImageField(label='Avata', required=False)
    class Meta:
        model = Profile
        fields = ('img',)
        widgets = {'user': forms.HiddenInput()}

class PostForm(forms.ModelForm):
    title = forms.CharField(label='Tiêu đề', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Nội dung', widget=forms.Textarea(attrs={'class': 'form-control'}))
    cover = forms.ImageField(label='Thêm ảnh', required=False)
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {'author': forms.HiddenInput(), 'cover': forms.HiddenInput()}

class CommentForm(forms.ModelForm):
    comment_box = forms.CharField(label='Để lại bình luận', widget=forms.Textarea(attrs={'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write a comment...'}))
    class Meta:
        model = CommentPost
        fields = '__all__'
        widgets = {
            'post_id': forms.HiddenInput(),
            'user_id': forms.HiddenInput()
        }

class CTCForm(forms.ModelForm):
    comment_field = forms.CharField(label='Trả lời bình luận', widget=forms.Textarea(attrs={'class': 'form-control',
                'rows': 3,
                'placeholder': 'Write a comment...'}))
    class Meta:
        model = Comment_to_comment
        fields = '__all__'
        widgets = {
            'comment_id': forms.HiddenInput(),
            'user_ctc_id': forms.HiddenInput()
        }