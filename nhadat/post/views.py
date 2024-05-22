from django.shortcuts import render, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post, District, Ward
from users.models import Account
from .forms import PostForm
from django.http import JsonResponse
import datetime

# Create your views here.
number_post_per_page = 5

def view_home(request):
    list_post = Post.objects.all().order_by('-postTime')
    if request.GET.get("page"):
        print(request.GET.get("page"))
        paginator = Paginator(list_post, number_post_per_page)
        page_number = request.GET.get("page")
        try:
            list_post = paginator.page(page_number)
        except PageNotAnInteger:
            list_post = paginator.page(1)
        except EmptyPage:
            list_post = paginator.page(1)
        # list_post = paginator.get_page(page_number)
    else:
        paginator = Paginator(list_post, number_post_per_page)
        list_post = paginator.page(1)
    for post in list_post:
        post.priceBillion = round(post.price / 1000000000, 2)
        post.pricePerSquare = round(post.price / post.square / 1000000)

    return render(request, 'home.html', {"list_post": list_post})

def view_home_page(request, id):
    list_post = Post.objects.order_by('postTime')

def load_districts(request):
    province_id = request.GET.get('province_id')
    districts = District.objects.filter(province_id=province_id).values('id', 'districtName')
    return JsonResponse(list(districts), safe=False)

def load_wards(request):
    district_id = request.GET.get('district_id')
    wards = Ward.objects.filter(district_id=district_id).values('id', 'wardName')
    return JsonResponse(list(wards), safe=False)
    
def view_upload_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.postTime = datetime.date.today()
            obj.status = 0
            username = request.session.get('username')
            obj.account = Account.objects.get(username=username)
            obj.save()
            return redirect('/')
        else:
            print('Form is not valid')
            print(form.errors)
    else:
        form = PostForm()
    return render(request, 'uploadPost.html', {'form': form})

    # form = PostForm()
    # if request.method == "POST":
    #     form = PostForm(request.POST)
    #     if form.is_valid():
    #         try:
    #             form.save()
    #             return redirect('/manage-post')
    #         except:
    #             pass
    # return render(request, 'uploadPost.html', {'form': form})

def view_detail_post(request, id):
    post = Post.objects.get(id=id)
    post.priceBillion = round(post.price / 1000000000, 2)
    post.pricePerSquare = round(post.price / post.square / 1000000)
    return render(request, 'detailPost.html', {'post': post})

def view_detail_update_post(request, id):
    post = Post.objects.get(id=id)
    form = PostForm(instance=post)
    return render(request, 'updatePost.html', {'form': form, 'id': id})

def view_update_post(request, id):
    post = Post.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.postTime = datetime.date.today()
            obj.status = 0
            username = request.session.get('username')
            obj.account = Account.objects.get(username=username)
            obj.save()
            return redirect('../manage-post')
        else:
            print('Form is not valid')
            print(form.errors)
    return redirect(f'../detail-update-post/{id}')

def view_delete_post(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect('../manage-post')

def view_manage_post(request):
    username = request.session.get('username')
    account = Account.objects.get(username=username)
    if account is not None:
        list_post = Post.objects.filter(account=account).order_by('-postTime')
        if request.GET.get("page"):
            print(request.GET.get("page"))
            paginator = Paginator(list_post, number_post_per_page)
            page_number = request.GET.get("page")
            try:
                list_post = paginator.page(page_number)
            except PageNotAnInteger:
                list_post = paginator.page(1)
            except EmptyPage:
                list_post = paginator.page(1)
        else:
            paginator = Paginator(list_post, number_post_per_page)
            list_post = paginator.page(1)
        for post in list_post:
            post.priceBillion = round(post.price / 1000000000, 2)
            post.pricePerSquare = round(post.price / post.square / 1000000)
        return render(request, 'managePostUser.html', {'list_post': list_post})
    else:
        return redirect('/')

def view_censor_post(request):
    return render(request, 'censorPost.html')

def view_list_post_admin(request):
    return render(request, 'listPostAdmin.html')