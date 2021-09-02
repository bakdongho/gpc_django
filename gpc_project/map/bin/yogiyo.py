import re
import requests
import json
from bs4 import BeautifulSoup
from collections import defaultdict

# 요기요
def load_store_yo(x,y,cate):
    cate_dic={
        '카페':'카페디저트',
        '양식':'피자양식',
        '일식':'일식돈까스',
        '중식':'중국집',
        '음식점':''
    }
    category = cate_dic[cate] if cate in cate_dic else cate
    headers = {
        'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2',
        'x-apikey': 'iphoneap',
    }

    params = (
        ('category', category), # 없으면 전체, 프랜차이즈,피자양식,한식,족발보쌈,중국집,일식돈까스,카페디저트,분식
        ('items', '40'),
        ('lat', x),
        ('lng', y),
        ('order', 'distance'), # 거리순 / review_avg: 별점순 / review_count : 리뷰순
        ('page', '0'), # 페이지 수
    )

    response = requests.get('https://www.yogiyo.co.kr/api/v1/restaurants-geo/', headers=headers, params=params)
    # print(json.dumps(json.loads(response.text), indent=4, sort_keys=True,ensure_ascii=False))
    site_list=json.loads(response.text)
    # print(f'site_list len : {len(site_list)}')
    # print(f'site_list type : {type(site_list)}')
    # print(f'site_list keys : {site_list.keys()}')
    # print(f"site_list 1 : {site_list['pagination']}")
    # print(f"site_list 2 : {site_list['restaurants']}")
    stop_re=re.compile('GS25|CU|세븐일레븐')
    site_dic=defaultdict(list)

    for site in site_list['restaurants']:
        # print(f'site len : {len(site)}')
        # print(f'site type : {type(site)}')
        # print(f'site keys : {site.keys()}')
        if site['open'] and stop_re.search(site['name']) is None:
            site_dic['id'].append(site['id'])
            site_dic['lat'].append(site['lat'])
            site_dic['lng'].append(site['lng'])
            site_dic['distance'].append(round(site['distance']*1000,2))
            site_dic['name'].append(site['name'])
            site_dic['star'].append(site['review_avg'])
            site_dic['review'].append(site['review_count'])
            site_dic['time'].append(site['open_time_description'])

    return site_dic

def load_menu_yo(id_list,name_list):
    stop_re=re.compile('음료|주류|사이드|추가|기타')
    store_dic={}
    menu_dic={}
    headers = {
        'x-apisecret': 'fe5183cc3dea12bd0ce299cf110a75a2',
        'x-apikey': 'iphoneap',
    }
    # 요기요 가게 api
    for id_,name in zip(id_list,name_list):
        response = requests.get(f'https://www.yogiyo.co.kr/api/v1/restaurants/{id_}/menu/', headers=headers)
        site_list=json.loads(response.text)
        for n,site in enumerate(site_list):
            # if stop_re.search(site['name']) is None:
                # name_list.append(site['name'])
                # print(site.keys())
                # print(f'site len : {len(site)}')
                # print(f'site type : {type(site)}')

            for item in site['items']:
                menu_dic[item['name']]=item['price']
        store_dic[name]=menu_dic
    return store_dic



if __name__=="__main__":
    a=["433428"]
    b=['토크카페']
    c=load_menu_yo(a,b)

    print(c)