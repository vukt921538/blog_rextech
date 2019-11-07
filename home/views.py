from django.shortcuts import render, redirect
from home.forms import RegistrationForm, UpdateProfileForm, AvataForm, PostForm, CommentForm, CTCForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserChangeForm
from .models import Profile, Post, CommentPost, Comment_to_comment

# Create your views here.
def home(request):
    posts = Post.objects.all().order_by('-date_published')
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            form.save()
            return redirect('/')
    else:
        form = PostForm(initial={
            'author': request.user
        })

    for post in posts:
        post.img_user_url = Profile.objects.get(user=post.author).img.url
        post.profile = Profile.objects.get(user=post.author)
        print(post.profile.id)
    context = {
        'posts': posts,
        'post.img_user_url': post.img_user_url,
        'form': form,
        'post.profile': post.profile
    }
    print(post.img_user_url)
    return render(request, 'index.html', context)

def reply_comment(request, id):
    reply_comment = CommentPost.objects.get(pk=id)
    print('Rep: ', reply_comment.post_id.id)

    if request.method == 'POST':
        rep_comment_label = CTCForm(request.POST)
        if rep_comment_label.is_valid():
            rep_comment_label.save()
            return redirect('reply_comment', reply_comment.id)
    else:
        rep_comment_label = CTCForm(initial={
            'comment_id': reply_comment,
            'user_ctc_id': request.user
        })
    reply_comment_comment = Comment_to_comment.objects.filter(comment_id=reply_comment).order_by('-comment_ctc_time')
    count = 0
    for comment in reply_comment_comment:
        count += 1
    print(count)
    context = {
        'reply_comment': reply_comment,
        'reply_comment_label': rep_comment_label,
        'reply_comment_comment': reply_comment_comment,
        'count': count
    }
    
    return render(request, 'reply.html', context)

# CONTENT BLOG 
def content(request, id):
    post = Post.objects.get(pk=id)
    comment_post = CommentPost.objects.filter(post_id=post)
    if request.method=='POST':
        form_comment = CommentForm(request.POST)
        if form_comment.is_valid():
            comment_box = form_comment.cleaned_data['comment_box']
            form_comment.save()
            return redirect('content', post.id)
    else:
        form_comment = CommentForm(initial={
            'user_id': request.user,
            'post_id': post
        })
        
    profile_author = Profile.objects.get(user=post.author)
    list_comment = CommentPost.objects.filter(post_id=post).order_by('-comment_time')
    for list in list_comment:
        list.count = Comment_to_comment.objects.filter(comment_id=list).order_by('-comment_ctc_time').count()
        print('LIST COMMENT: ', list.count)
    print('arr:', list_comment)
    
    new_list = [Comment_to_comment.objects.filter(comment_id=comment).order_by('-comment_ctc_time').count() for comment in list_comment]
    context = {
        'post': post,
        'profile': profile,
        'profile_author': profile_author,
        'form_comment': form_comment,
        'list_comment': list_comment,
        'new_list_1': new_list[0],
        'list.count': list.count, #Lưu ý: Muốn truyền được phải cùng tên biến với templates

    }
    # Lấy comment từ post đó xong rồi lấy comment_to_comment từ comment
    # Show ra đc các comment_to_comment của Post đó:
    return render(request, 'content.html', context)

def about(request):
    return render(request, 'about.html')

    
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            form.save()
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }

    return render(request, 'registration/register.html', context)

def profile(request, id):
    user_profile = User.objects.get(pk=id)
    if request.method=='POST':
        form_avata = AvataForm(request.POST, request.FILES, instance=request.user.profile)
        if form_avata.is_valid():
            img = form_avata.cleaned_data['img']
            form_avata.save()
            return redirect('profile', user_profile.id)

    else:
        form_avata = AvataForm(initial={
            'user': request.user,
        })
    context = {
        'user_profile': user_profile,
        'form_avata': form_avata
    }
    print('User: ', user_profile.profile.img.url)
    return render(request, 'registration/profile.html', context)

def update_profile(request, id):
    profile_user = User.objects.get(pk=id)
    if request.method=='POST':
        form = UpdateProfileForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            address = form.cleaned_data['address']
            job = form.cleaned_data['job']
            dob = form.cleaned_data['dob']
            email = form.cleaned_data['email']
            f_name = form.cleaned_data['f_name']
            l_name = form.cleaned_data['l_name']
            form.save()
            return redirect('profile', profile_user.id)

    else:
        form = UpdateProfileForm(initial={
            'user': request.user,
            'f_name': profile_user.profile.f_name,
            'l_name': profile_user.profile.l_name,
            'email': profile_user.profile.email,
            'address': profile_user.profile.address,
            'dob': profile_user.profile.dob,
            'job': profile_user.profile.job
        })

    context = {
        'form': form
    }
    print('Request: ', request.user)
    print(profile_user.profile.dob)
    print('Profile user request:', request.user.profile)
    print('profile user:', request.user.profile)
    return render(request, 'registration/update_profile.html', context)