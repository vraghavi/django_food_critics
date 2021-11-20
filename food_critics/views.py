from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Comments, FoodBlog, BlogDetailView
from actions.models import Action
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

#to show blogs in list
def blog_list(request):
    food_blogs = FoodBlog.objects.all().order_by('points')
    return render(request,
                  "blogs/blogs_list/list.html",
                  {"food_blogs": food_blogs})

def sort_by_date(request):
    food_blogs = FoodBlog.objects.all().order_by('date_posted')
    return render(request,
                  "blogs/blogs_list/list.html",
                  {"food_blogs": food_blogs})

#to show detailed blogs
def blog_in_detail(request, blog_id):
    blog = FoodBlog.objects.get(id=blog_id)
    comments = blog.blog.all()
    blogDetaiView = BlogDetailView(blog=blog, comments=comments)
    return render(request,
                  "blogs/blogs_list/blog-in-detail.html",
                  {"blog": blogDetaiView})
#home
def home(request):
    if request.session.get('username',False):
        actions = Action.objects.all().order_by('-created')
        return render(request, 'blogs/dashboard.html', {"actions":actions})
    else:
        return render(request, "blogs/home.html",)
    # if(pid == regular_user['pid']) and (password == regular_user['password']):
    #     request.session['pid'] = pid
    #     request.session['role'] = 'user'
    #     return redirect('food_critics:blog-list')
    # elif(pid == admin_user['pid']) and (password == admin_user['password']):
    #     request.session['pid'] = pid
    #     request.session['role'] = 'admin'
    #     return redirect('food_critics:blog-list')
    # else:
    #     return redirect('food_critics:home')

#search view
def search(request):
    keyword = request.GET.get("search-keyword")
    if(keyword.lower()=="blacksburg"):
        food_blogs = FoodBlog.objects.filter(title__icontains='blacksburg')
    elif(keyword.lower()=="ncr"):
        food_blogs = FoodBlog.objects.filter(Q(title__icontains= 'arlington')| Q(title__icontains= 'falls church'))
    elif(keyword.lower()=="mexican"):
        food_blogs = FoodBlog.objects.filter(title__icontains='mexi')
    elif(keyword.lower()=="family"):
        food_blogs = FoodBlog.objects.filter(detail_description__icontains='family')
    elif(keyword.lower()=="food"):
        food_blogs=FoodBlog.objects.all()
    elif(keyword.lower()==""):
        food_blogs=FoodBlog.objects.all()
    else:
        food_blogs = ''
    return render(request,
                  "blogs/blogs_list/list.html",
                  {"food_blogs": food_blogs})

# adding a new comment
def newcomment(request):
    newComment = request.GET.get('newComment')
    blogid = request.GET.get('blog_id')
    username=request.session['username']
    # food_blogs[int(blogid)].comments.append({11,int(blogid),datetime.now(),"anonymous",newComment })
    # newcomment =FoodBlog.blog.create(date_commented=datetime.now(),user_commented=pid, description=newComment)
    blog = FoodBlog.objects.get(id=blogid)
    newcomment = Comments(date_commented=datetime.now(),user_commented=username, description=newComment, blog=blog)
    newcomment.save()

    #save Action
    user = User.objects.get(username=username)
    action = Action(user=user, verb='commented', target=newcomment)
    action.save()

    messages.add_message(request, messages.SUCCESS, "Successfully commented on '%s' post!" %blog.title)
    return redirect('food_critics:blog-in-detail',blog_id=int(blogid))

#editing an existing comment
def editcomment(request):
    edited_comment = request.POST.get('edited_comment')
    comment_id = request.POST.get('comment_id')
    blogid = request.POST.get('blog_id')
    comment = Comments.objects.get(id=comment_id)
    comment.description = edited_comment
    comment.save()

    #save Action
    user = User.objects.get(username=request.session['username'])
    action = Action(user=user, verb='edited comment', target=comment)
    action.save()

    messages.add_message(request, messages.INFO, "Successfully edited the comment to : %s" %comment.description)
    return redirect('food_critics:blog-in-detail',blog_id=int(blogid))

#deleting an existing comment
def deletecomment(request):
    deletecomment_id = request.POST.get('comment_id')
    comment = Comments.objects.get(id=deletecomment_id)
    blogid = comment.blog.id
    comment_des = comment.description
    comment.delete()

    #save Action
    user = User.objects.get(username=request.session['username'])
    action = Action(user=user, verb='deleted comment', target=comment)
    action.save()

    messages.add_message(request, messages.WARNING, "Successfully deleted the comment!! : %s" %comment_des)
    return redirect("food_critics:blog-in-detail",blog_id=int(blogid))

def edit_points(request):
    is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
    if is_ajax and request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        try:
            blog = FoodBlog.objects.get(id=blog_id)
            blog.points = request.POST.get('points')
            blog.save()

            #save Action
            user = User.objects.get(username=request.session['username'])
            action = Action(user=user, verb='edited points', target=blog)
            action.save()

            return JsonResponse({"success":"success",'title':blog.title, 'points':blog.points},status=200)
        except FoodBlog.DoesNotExist:
            return JsonResponse({"error":"Blog not found with that ID"},status=200)
    else:
        return JsonResponse({"error":"Invalid Ajax Request"},status=400)

# def user_profile(request):
#     is_ajax = request.headers.get('x-requested-with') == 'XMLHttpRequest'
#     if is_ajax and request.method == 'POST':
#         username = request.POST.get('username')
#         try:
#             user = User.objects.get(username=username)
#             return JsonResponse({"success":"success", 'username':user.username, 'points':user.points },status=200)
#         except User.DoesNotExist:
#             return JsonResponse({"error":"User not found with that name"},status=200)
#     else:
#         return JsonResponse({"error":"Invalid Ajax Request"},status=400)

    