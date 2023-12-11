from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Bill
from .serializers import BillSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Item

from io import BytesIO
import json
import os
import fpdf
from datetime import datetime


@api_view(['POST'])
def load_bill(request):
    current_datetime = datetime.now()
    formtatted_datetime = current_datetime.strftime('%d.%m.%y %H:%M')
    ids = request.data.get('items', None)
    queryset = Item.objects.filter(pk__in=ids)

    pdf_ = fpdf.FPDF(format='letter') #pdf format
    pdf_.add_page() #create new page
    path = os.path.abspath('app/OpenSans/OpenSans-Bold.ttf')
    pdf_.add_font('OpenSans', '', path, uni=True)
    pdf_.set_font('OpenSans', size=12) # font and textsize
    pdf_.cell(200, 10, txt='ООО "КОМПАНИЯ К"', ln=1, align='T')
    pdf_.cell(200, 10, txt='Добро пожаловать', ln=1, align='T')
    pdf_.cell(200, 10, txt='ККМ 00075411 #3969', ln=1, align='T')
    pdf_.cell(200, 10, txt='ЭКЛЗ 3851495566', ln=1, align='T')
    pdf_.cell(200, 10, txt='ДАТА СИС', ln=1, align='T')
    pdf_.cell(200, 10, txt=formtatted_datetime, ln=1, align='T')

    total = 0
    for x in queryset:
        pdf_.cell(200, 10, txt=f'{x.title} = {x.price}', ln=2, align='L')
        total += x.price

    pdf_.cell(200, 10, txt=f'ИТОГ {total}', ln=1, align='T')
    pdf_.cell(200, 10, txt=f'НАЛИЧНЫМИ = {total}', ln=1, align='T')
    pdf_.cell(200, 10, txt='****************************', ln=1, align='T')
    pdf_.cell(200, 10, txt='000003751# 05970', ln=1, align='T')

    pdf_.output('media/чек.pdf')

    return Response('msg')