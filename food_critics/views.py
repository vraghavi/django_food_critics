from django.shortcuts import render, redirect
from .models import food_blogs, food_blogs_copy, regular_user, admin_user
from datetime import datetime
import copy

# Create your views here.

#to show blogs in list
def blog_list(request,bloglist=food_blogs):
    return render(request,
                  "blogs/blogs_list/list.html",
                  {"food_blogs": bloglist})

#to show detailed blogs
def blog_in_detail(request, blog_id):
    for blog in food_blogs:
        if(blog.id == blog_id):
            break
    return render(request,
                  "blogs/blogs_list/blog-in-detail.html",
                  {"blog": blog})
#home
def home(request):
    return render(request, "blogs/home.html", {"home":home})

#login view
def login(request):
    pid = request.POST.get("pid")
    password = request.POST.get("password")
    if(pid == regular_user['pid']) and (password == regular_user['password']):
        request.session['pid'] = pid
        request.session['role'] = 'user'
        return redirect('food_critics:blog-list')
    elif(pid == admin_user['pid']) and (password == admin_user['password']):
        request.session['pid'] = pid
        request.session['role'] = 'admin'
        return redirect('food_critics:blog-list')
    else:
        return redirect('food_critics:home')
    
#logout view
def logout(request):
    del request.session['pid']
    del request.session['role']
    return redirect('food_critics:home')

#search view
def search(request):
    keyword = request.GET.get("search-keyword")
    if(keyword.lower()=="blacksburg"):
        food_blogs=copy.deepcopy(food_blogs_copy)
        del food_blogs[1:4]
    elif(keyword.lower()=="ncr"):
        food_blogs=copy.deepcopy(food_blogs_copy)
        food_blogs.pop(0)
        food_blogs.pop(-1)
    elif(keyword.lower()=="mexican"):
        food_blogs=copy.deepcopy(food_blogs_copy)
        del food_blogs[:3]
    elif(keyword.lower()=="family"):
        food_blogs=copy.deepcopy(food_blogs_copy)
        del food_blogs[:2]
        food_blogs.pop(-1)
    elif(keyword.lower()=="food"):
        food_blogs=copy.deepcopy(food_blogs_copy)
    elif(keyword.lower()==""):
        food_blogs=copy.deepcopy(food_blogs_copy)
    return render(request,
                  "blogs/blogs_list/list.html",
                  {"food_blogs": food_blogs})

# adding a new comment
def newcomment(request):
    newComment = request.GET.get('newComment')
    blogid = request.GET.get('blog_id')
    # pid=request.session.pid
    food_blogs[int(blogid)].comments.append({11,int(blogid),datetime.now(),"anonymous",newComment })
    return redirect('food_critics:blog-in-detail',blog_id=int(blogid))

#editing an existing comment
def editcomment(request):
    edited_comment = request.POST.get('edited_comment')
    comment_id = request.POST.get('comment_id')
    blogid = request.POST.get('blog_id')
    for blog in food_blogs:
        if blog.id == blogid:
            for comment in blog.comments:
                if(comment.id == comment_id):
                    comment.description = copy.deepcopy(edited_comment)
                    break
    return redirect('food_critics:blog-in-detail',blog_id=int(blogid))

#deleting an existing comment
def deletecomment(request):
    deletecomment_id = request.POST.get('comment_id')
    blogid = ''
    for blog in food_blogs:
        for comment in blog.comments:
            if(comment.id == int(deletecomment_id)):
                blogid = comment.blog_id
                blog.comments.remove(comment)
                break
    return redirect("food_critics:blog-in-detail",blog_id=int(blogid))