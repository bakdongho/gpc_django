from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator

from .models import Article
# Create your views here.

def hello_world(request, to):
    return HttpResponse(f'hello {to}~!')

## CBV(Class Based View)
# 목록 보기
class ArticleListView(TemplateView):
    template_name='article_list.html'

    # template에 데이터 전달
    def get(self, request, *arg, **kwargs):
        page = self.request.GET.get('page',1)
        article_obj=Article.objects.order_by('-created_dt')
        article = Paginator(article_obj,10)
        ctx={
            'view' : self.__class__.__name__,
            'data' : article.get_page(page),
        }
        return self.render_to_response(ctx)

# 게시글 상세보기
class ArticleDetailView(TemplateView):
    template_name='article_detail.html'
    query_set= Article.objects.all()
    pk_url_kwargs='article_id'

    def get_object(self, query_set=None):
        query_set= query_set or self.query_set
        pk = self.kwargs.get(self.pk_url_kwargs)
        return query_set.filter(pk=pk).first()

    def get(self, request, *arg, **kwargs):
        article=self.get_object()
        if not article:
            messages.error(self.request, '게시글을 찾을 수 없습니다.', extra_tags='danger')
        ctx={
            'view' : self.__class__.__name__,
            'article' : article,
        }
        
        return self.render_to_response(ctx)


# 생성 및 수정
# @method_decorator(csrf_exempt, name='dispatch')
class ArticleCreateUpdateView(LoginRequiredMixin,TemplateView):  # 게시글 추가, 수정
    template_name = 'article_update.html'
    query_set= Article.objects.all()
    pk_url_kwargs='article_id'
    success_message = '게시글이 저장되었습니다.'
    
    def get_object(self, query_set=None):
        query_set = query_set or self.query_set
        pk = self.kwargs.get(self.pk_url_kwargs)
        article=query_set.filter(pk=pk).first()
        return article

    # 화면 요청
    def get(self, request, *args, **kwargs):  
        article = self.get_object()
        ctx = {
            'view': self.__class__.__name__,
            'article': article
        }
        return self.render_to_response(ctx)
    # 액션
    def post(self, request, *args, **kwargs): 
        action= request.POST.get('action')
        post_data={key:request.POST.get(key) for key in ('title', 'content')}
        for key in post_data:
            if not post_data[key]:
                messages.error(self.request, '{} 값이 존재하지 않습니다.'.format(key), extra_tags='danger')
        post_data['author'] = self.request.user
        print('>>>>>post data : ',post_data)
        if len(messages.get_messages(request))==0:
            if action=='create':
                article=Article.objects.create(**post_data)
                messages.success(self.request, self.success_message)
            elif action=='update':
                article = self.get_object()
                for key, value in post_data.items():
                    setattr(article,key,value)
                article.save()
                messages.success(self.request, self.success_message)
            else:
                messages.error(self.request, '알 수 없는 요청입니다.', extra_tags='danger')
            
            return HttpResponseRedirect('/article/')
        ctx = {
            'view' : self.__class__.__name__,
            'article' : self.get_object() if action == 'update' else None,
        }
        return self.render_to_response(ctx)
