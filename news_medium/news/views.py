from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm, LoginUserForm
from .models import Article, Comment, CategoryArticle


class ArticleListView(ListView):
    model = Article
    template_name = 'news/article/main_page.html'
    context_object_name = 'articles'
    paginate_by = 5

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Main page'
        return context

    def get_queryset(self):
        return Article.objects.filter(status='publisher').select_related('category').only('title', 'text', 'photo', 'create', 'category')


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'news/article/article.html'
    context_object_name = 'article'
    slug_field = 'slug_field'
    slug_url_kwarg = 'slug_field'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Article'
        context['comments'] = Comment.objects.filter(article=context.get('article'))
        return context


class CommentCreateView(CreateView):
    model = Comment
    fields = ['name', 'email', 'comment_text', 'article']
    template_name = 'news/comments/add_comment.html'
    success_url = reverse_lazy('article_list')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add comment'
        return context


class TagsListVies(ListView):
    model = CategoryArticle
    template_name = 'news/tags/tags.html'
    context_object_name = 'tags_list'
    paginate_by = 5

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'List tags'
        return context


class ShowArticleListView(ListView):
    model = Article
    template_name = 'news/article/main_page.html'
    context_object_name = 'articles'

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Articles by tag'
        return context

    def get_queryset(self):
        return Article.objects.filter(category__slug=self.kwargs['category_slug'], status='publisher').select_related(
            'category').only('title', 'text', 'photo', 'create', 'category')


class ArticleCreateView(CreateView):
    model = Article
    fields = ['title', 'text', 'author', 'photo', 'status', 'video', 'category', 'slug_field']
    template_name = 'news/article/add_article.html'
    success_url = reverse_lazy('article_list')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add article'
        return context


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'news/login_register/register.html'
    success_url = reverse_lazy('article_list')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('article_list')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'news/login_register/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Log in'
        return context

    def get_success_url(self):
        return reverse_lazy('article_list')


def logout_user(request):
    logout(request)
    return redirect('login')


class TagsCreateView(CreateView):
    model = CategoryArticle
    fields = ['name_category', 'slug']
    template_name = 'news/tags/add_tag.html'
    success_url = reverse_lazy('article_list')

    def get_context_data(self, *, objects_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add tag'
        return context
