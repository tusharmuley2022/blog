from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import EditArticleForm, NewArticleForm
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

def articles_list(request):
    #return render(request, 'articles/articles_list.html')
    articles = Article.objects.all().select_related('created_by').order_by('-created_at')
    if not articles:
        return JsonResponse({'status':'fail', 'message':'No articles found', 'status_code':404}, status=404)
        
    # Pass the list of articles to the template context
    context = {'articles': articles}

    # Render the HTML template and pass the context
    return render(request, 'articles/articles_list.html', context)


def article_detail(request, article_id):
    try:
        articles = Article.objects.get(id=article_id)
    except Article.DoesNotExist:
        return JsonResponse({'status':'fail', 'message':'Article Not Found', 'status_code':404}, status=404)

    context = {'articles': articles}
    return render(request, 'articles/articles_list.html', context)

@login_required
def edit_article(request, article_id):
    try:
        article_exist = Article.objects.get(id=article_id, created_by=request.user.id)
    except Article.DoesNotExist:
        return JsonResponse({'status':'fail', 'message':'Access denied: Not the article owner', 'status_code':403}, status=403)
      
    if request.method == 'POST':
        form = EditArticleForm(request.POST, instance=article_exist)
        if form.is_valid():
            form.save()
    
            # redirect ->  fucn name
            return redirect('article_detail', article_id=article_exist.id)
    else:
        form = EditArticleForm(instance=article_exist)

    return render(request, 'articles/edit_article.html', {'form': form, 'article': article_exist})

@login_required
def delete_article(request, article_id):
    if request.method == 'POST':
        try:
            article_exist = Article.objects.get(id=article_id, created_by=request.user.id)
        except Article.DoesNotExist:
            return JsonResponse({'status':'fail', 'message':'Article Not Found', 'status_code':404}, status=404)
       
        article_exist.delete()
        return redirect('articles_list')
    else:
        return JsonResponse({'status':'fail', 'message':'Method not found', 'status_code':405}, status=405)
        
      
@login_required  
def create_article(request):
    if request.method == 'POST':
        form = NewArticleForm(request.POST)
        if form.is_valid():
            # Create a new article based on the form data, but don't save it yet
            new_article = form.save(commit=False)
            
            # You can perform additional operations on the new_article here if needed
            # For example, set the author or modify other fields
            new_article.created_by=request.user

            # Finally, save the article to the database
            new_article.save()
            return redirect('articles_list')  # Redirect to a page showing a list of articles

    else:
        form = NewArticleForm()

    return render(request, 'articles/create_article.html', {'form': form})
