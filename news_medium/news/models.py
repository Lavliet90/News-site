from django.contrib.auth.models import User
from django.db import models
from embed_video.fields import EmbedVideoField
from django.urls import reverse




class CategoryArticle(models.Model):
    name_category = models.CharField(max_length=30, verbose_name='Name tags')
    slug = models.SlugField(max_length=35, unique=True, db_index=True, verbose_name='URL', blank=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')

    def get_absolute_url(self):
        return reverse('article_by_tag', kwargs={'category_slug:': self.slug})

    def __str__(self):
        return f'{self.name_category}'

    class Meta:
        ordering = ('-create',)


class Article(models.Model):
    '''
    Posts from main page
    '''
    STATUS_CHOISE = (
        ('draft', 'Draft'),
        ('publisher', 'Publisher'),
    )
    title = models.CharField(max_length=250, verbose_name='Title')
    text = models.TextField(blank=False, default='', verbose_name='Text')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts', verbose_name='Author')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True, verbose_name='Photo')
    last_change = models.DateTimeField(auto_now=True, verbose_name='Last change')
    create = models.DateTimeField(auto_now_add=True, verbose_name='Time of creation')
    slug_field = models.SlugField(max_length=250, unique=True, verbose_name='Slug')
    status = models.CharField(max_length=10, choices=STATUS_CHOISE, default='draft', verbose_name='Status')
    video = EmbedVideoField(blank=True, verbose_name='Video')
    category = models.ForeignKey(CategoryArticle, on_delete=models.CASCADE, related_name='tag', verbose_name='Category')

    def get_absolute_url(self):
        return reverse('one_article', kwargs={'slug_field': self.slug_field})

    class Meta:
        ordering = ('-create',)

    def __str__(self):
        return self.title


class Comment(models.Model):
    article = models.ForeignKey(Article, related_name='comments', on_delete=models.CASCADE, verbose_name='Related article')
    name = models.CharField(max_length=250, verbose_name='Name user')
    email = models.EmailField(verbose_name='Email')
    comment_text = models.TextField(verbose_name='Text comment')
    comment_create = models.DateTimeField(auto_now=True, verbose_name='Time of creation')

    class Meta:
        ordering = ('-comment_create',)

    def __str__(self):
        return f'Comment by {self.name} on {self.article}'

    def get_absolute_url(self):
        return reverse('add_comment')
