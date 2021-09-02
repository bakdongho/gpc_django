import json
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse, Http404
from .bin.naver import Naverscrap
from .bin.yogiyo import load_store_yo,load_menu_yo
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class MapMain(TemplateView):
    template_name='map.html'
    api_id='rh6gbl7odz'
    def get(self, request, *arg, **kwargs):
        ctx={
            "client_id": self.api_id
        }
        return self.render_to_response(ctx)

def MapSearch(request):
    if request.method == 'GET':
        try:
            lat=request.GET.get('y')
            lng=request.GET.get('x')
            category=request.GET.get('cate')
        except:
            raise KeyError('잘못된 파라미터 요청', 403)
        x_y_list=[]

        site_dic=Naverscrap.store_search(lat,lng,category)
        store_dic=Naverscrap.get_menu(site_dic,category)
        
        for n,v in store_dic.items():
            idx=site_dic['id'].index(v['id'])
            x_y_list.append([site_dic["lat"][idx],site_dic["lng"][idx],n,v['url']])

        status = 'success' if x_y_list != [] else 'fail'
        context = {
            'result': {
                    'xy':x_y_list,
                    'status':status
                },
        }
        return JsonResponse(context)
    else:
        return Http404