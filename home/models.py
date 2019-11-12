from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=50)
    job = models.CharField(max_length=30)
    dob = models.DateField(null=True)
    f_name = models.CharField(max_length=10)
    l_name = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    descriptions = models.TextField()
    img = models.ImageField(upload_to='avata', default='avata/178697.png', blank=True)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_published = models.DateTimeField(auto_now=True)
    # cover = models.ImageField(upload_to='cover', default='cover/cover_default.jpg', blank=True)

    def __str__(self):
        return self.title

class CommentPost(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_box = models.TextField()
    comment_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_id.title

class Comment_to_comment(models.Model):
    comment_id = models.ForeignKey(CommentPost, on_delete=models.CASCADE)
    user_ctc_id = models.ForeignKey(Profile, on_delete=models.CASCADE)
    comment_field = models.TextField()
    comment_ctc_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_id.comment_box