from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from cultureapp.tourism.tourism import Data_tourism_View
from cultureapp.tourism.tourism_all import Data_tourism_all
from cultureapp.medical.medical_graph import Data_medical_View
from cultureapp.medical.medical_map import Medical_map
from cultureapp.hospital.numbed_graph import Num_bed_View
from cultureapp.hospital.numbed_map import Num_bed_map

# Create your views here.
def tourism(request) :
    ### 클래스 생성시키기
    data_view2 = Data_tourism_View()
    data_view3 = Data_tourism_all()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
       
    data_view = data_view2.setYearDataFrame(year)
    data_view1 = data_view3.setYearDataFrame()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'cultureapp/tourism.html', {"data_view" : data_view,
                                                        "year_data" : year,
                                                        "fig" : fig,
                                                        "fig2" : fig2})


def medical(request) :
    ### 클래스 생성시키기
    data_view2 = Data_medical_View()
    map_view = Medical_map()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year)
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'cultureapp/medical.html', {"data_view" : data_view,
                                                           "map_html" : map_html,
                                                            "year_data" : year,
                                                            "area_data" : area,
                                                            "fig" : fig})


def hospital(request) :
    ### 클래스 생성시키기
    data_view2 = Num_bed_View()
    map_view = Num_bed_map()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year)
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'cultureapp/hospital.html', {"data_view" : data_view,
                                                        "map_html" : map_html,
                                                        "year_data" : year,
                                                        "area_data" : area,
                                                        "fig" : fig})

