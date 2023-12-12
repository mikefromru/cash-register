from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Bill
from .serializers import BillSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponseRedirect
from rest_framework.parsers import JSONParser
from .models import Item

import os
import fpdf
import qrcode
from datetime import datetime
from django.http import FileResponse


@api_view(['POST'])
def load_bill(request):
    current_datetime = datetime.now()
    formtatted_datetime = current_datetime.strftime('%d.%m.%y %H:%M')
    ids = request.data.get('items', None)
    queryset = Item.objects.filter(pk__in=ids)

    pdf = fpdf.FPDF(format='letter') #pdf format
    pdf.add_page() #create new page
    path = os.path.abspath('app/OpenSans/OpenSans-Bold.ttf')
    pdf.add_font('OpenSans', '', path, uni=True)
    pdf.set_font('OpenSans', size=12) # font and textsize
    pdf.cell(200, 10, txt='ООО "КОМПАНИЯ К"', ln=1, align='T')
    pdf.cell(200, 10, txt='Добро пожаловать', ln=1, align='T')
    pdf.cell(200, 10, txt='ККМ 00075411 #3969', ln=1, align='T')
    pdf.cell(200, 10, txt='ЭКЛЗ 3851495566', ln=1, align='T')
    pdf.cell(200, 10, txt='ДАТА СИС', ln=1, align='T')
    pdf.cell(200, 10, txt=formtatted_datetime, ln=1, align='T')

    total = 0
    for x in queryset:
        pdf.cell(200, 10, txt=f'{x.title} = {x.price}', ln=2, align='L')
        total += x.price

    pdf.cell(200, 10, txt=f'ИТОГ {total}', ln=1, align='T')
    pdf.cell(200, 10, txt=f'НАЛИЧНЫМИ = {total}', ln=1, align='T')
    pdf.cell(200, 10, txt='****************************', ln=1, align='T')
    pdf.cell(200, 10, txt='000003751# 05970', ln=1, align='T')

    pdf.output('media/чек.pdf')
    url = 'http://localhost:8000/media/чек.pdf'
    img = qrcode.make(url)
    img.save('media/qr-bill.png')

    qr_url = 'http://localhost:8000/media/qr-bill.png'



    # var = open('bill.png', 'rb')
    # response = FileResponse(var)
    # return HttpResponseRedirect(redirect_to='https://google.com')

    # return HttpResponseRedirect(redirect_to='http://localhost:8000/media/чек.pdf')
    # return HttpResponse('var')
    # return HttpResponse('var', content_type='image/png')

    # return Response(var, content_type='image/png')

    return Response({'redirect_url': qr_url})