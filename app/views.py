from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .serializers import ItemSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Item

import os
import fpdf

@api_view(['POST'])
def load_bill(request):
    ids = request.data.get('items', None)
    queryset = Item.objects.filter(pk__in=ids)
    # for x in queryset:
        # print(x.title)
    pdf = fpdf.FPDF(format='letter') #pdf format
    pdf.add_page() #create new page
    path = os.path.abspath('app/OpenSans/OpenSans-Bold.ttf')
    pdf.add_font('OpenSans', '', path, uni=True)
    pdf.set_font('OpenSans', size=12) # font and textsize
    pdf.cell(200, 10, txt='Документ', ln=1, align='T')
    for x in queryset:
        pdf.cell(200, 10, txt=f'Наименование товара - {x.title} = {x.price}', ln=2, align='L')
        # pdf.cell(200, 10, txt=f'Способ оплаты - {method_pay}', ln=3, align='L')
    pdf.output('Накладная.pdf')
    return Response('msg')


    # bar = [x.title for x in queryset]
    # queryset = Item.objects.filter(pk__in=ids)


    # if request.method == 'POST':
    # ids = request.data.get('items', None)
    # print(type(ids), ids)

