import json
import requests

from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

from .models import *

class StoreListView(View):
    def get(self,request):
        lat = request.GET.get('lat', None)
        lng = request.GET.get('lng', None)
        stores = Store.objects.select_related('country','city','district','business_district').all()
        if lat and lng:
            lat, lng        = float(lat), float(lng)
            user_point      = Point(lat,lng)
            stores          = Store.objects.filter(location__distance_lte = (user_point, 0.05)).annotate(distance = Distance('location', user_point)).order_by('distance')
        result = [{
            'name'      : store.name,
            'tel'       : store.tel,
            'hours'     : str(store.open_time)[:-3] + " ~ " + str(store.close_time)[:-3],
            'latlng'    : [store.lat, store.lng]
        } for store in stores]
        return JsonResponse({'data' : result}, status = 200)
    
class RegisterStoreView(View):
    def post(self,request):
        try:
            lat     = request.POST.get('lat')
            lng     = request.POST.get('lng')
            headers = {
                'Content-Type': 'application/json; charset=utf-8',
                'Authorization': 'KakaoAK {}'.format('d7efa09ac9724767a354f5253550ca34')
            }
            url     = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json?x=" + lng + "&y=" + lat
            result  = json.loads(str(requests.get(url,headers=headers).text))
            address = result['documents'][0]['address_name']
            city    = result['documents'][0]['region_1depth_name'][:2]
            if City.objects.filter(name = city).exists():
                RecommendedLocation.objects.create(
                location    = Point(float(lat),float(lng)),
                lat         = lat,
                lng         = lng,
                address     = address,
                country_id  = 1,
                city_id     = City.objects.get(name = city).id
            )
            else:
                City.objects.create(
                    name        = city,
                    country_id  = 1)
            return HttpResponse(status = 200)

        except KeyError:
            return JsonResponse({'message' : 'NO INPUT'}, status = 400)

        


