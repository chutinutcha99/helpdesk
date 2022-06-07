from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import AddTicket
from .forms import AddTicketForm
import requests
import datetime 

from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile

import xlwt

from django.db.models import Count


# Create your views here.
'''
def home(request):
    members = User.objects.count()
    processing_count = AddTicket.objects.filter(status = 'PROCESSING').count()
    complete_count = AddTicket.objects.filter(status= 'COMPLETE').count()
    cancel_count = AddTicket.objects.filter(status='CANCEL').count()

    context = {
        'members': members,
        'processing_count': processing_count,
        'complete_count': complete_count,
        'cancel_count': cancel_count,
    }
    return render(request, 'helpdeskapp/home.html', context)
'''
'''
class mychartview(TemplateView):
    template_name = 'helpdeskapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["qs"] = AddTicket.objects.all()
        return context
'''
#Dashboard Charts
def mychartview(request):
    queryset = AddTicket.objects.order_by('status').values('status').annotate(status_count=Count('status'))

    queryuser = User.objects.all().values('is_staff').annotate(total=Count('is_staff'))

    data = list(queryset.values_list('status_count', flat= True))
    labels = list(queryset.values_list('status', flat=True))

    data2 = list(queryuser.values_list('total', flat=True))
    labels2 = list(queryuser.values_list('is_staff', flat=True))

    
    context = {'queryset': queryset,
                'queryuser': queryuser,
                'data': data,
                'labels': labels,
                'data2': data2,
                'labels2': labels2          
    }
    return render(request, 'helpdeskapp/home.html', context)

#เปิด Ticket แล้ว save form ลง database
@login_required
def adds(request):
    if request.method == 'POST':
        form = AddTicketForm(request.POST, request.FILES)

        if form.is_valid():
            
            helpdeskapp = form.save(commit=False)
            helpdeskapp.user = request.user
            helpdeskapp.save()
            messages.success(request, f'บันทึกข้อมูลเรียบร้อยแล้ว')

            last_id = helpdeskapp.pk 
            form_detail = AddTicket.objects.get(id__exact = last_id)
            #print(form_detail.id)
            
            '''if form_detail.place == None:
                form_detail.place = "ไม่มีข้อมูล"'''
            
            
            url = 'https://notify-api.line.me/api/notify'
            token = 'xuVeGPqonotndJpC5VAqH0E51FiimOlnkDhXg5t5S62'
            headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

            msg = ("หมายเลขงาน : "+ str(form_detail.id) +",\r\n\r\nชื่อ Login ผู้แจ้งปัญหา : "+ form_detail.user.username +",\r\n\r\nประจำงวดงาน : "+ form_detail.installment.installment +",\r\n\r\nสถานที่ตั้งอุปกรณ์ : "+ str(form_detail.place) +", \r\n\r\nหน่วยงาน : "+ form_detail.institution +",\r\n\r\nผู้แจ้งปัญหา : "+ form_detail.informer +",\r\n\r\nเบอร์โทรศัพท์ : "+ form_detail.phone_number +",\r\n\r\nวันที่แจ้งปัญหา : "+ str(form_detail.issue_date) +",\r\n\r\nอุปกรณ์ : "+ str(form_detail.device_name) +",\r\n\r\nยี่ห้อ : "+ form_detail.brand +",\r\n\r\nรุ่น : "+ form_detail.model +",\r\n\r\nหมายเลขคุรุภัณฑ์ : "+ form_detail.inventory_number +",\r\n\r\nหมายเลขประจำอุปกรณ์ : "+ form_detail.serial_number +",\r\n\r\nปัญหาที่เกิดขึ้น : "+ form_detail.issue +",\r\n\r\nผู้รับผิดชอบ : "+ form_detail.responsibility +",\r\n\r\nรายละเอียดการซ่อม : "+ form_detail.detail +",\r\n\r\nวันที่ซ่อมเสร็จ : "+ str(form_detail.job_complete_date) +",\r\n\r\nสถานะซ่อมบำรุง : "+ form_detail.status +" ")


            r = requests.post(url, headers=headers, data = {'message':msg})
            print(r.text)

            #print(form_detail.status)
            
            return redirect('helpdeskapp:mylist')
        else:
            print('Error :', form.errors)
           
    form = AddTicketForm()
    return render(request, 'helpdeskapp/adds.html', {'form': form})

#แก้ไขฟอร์ม Ticket แล้ว Update ลง Database
@login_required
def edit(request, id):
    addticket_edit = AddTicket.objects.get(id=id)
    form = AddTicketForm(instance=addticket_edit)

    if request.method == 'POST':
        form = AddTicketForm(request.POST, instance=addticket_edit)
        if form.is_valid():
            helpdeskapp = form.save(commit=False)
            helpdeskapp.user = request.user
            helpdeskapp.save()
            messages.success(request, f'แก้ไขข้อมูลเรียบร้อยแล้ว')
            print(helpdeskapp.modified_data())

            last_id = helpdeskapp.pk 
            form_detail = AddTicket.objects.get(id__exact = last_id)
            #print(form_detail.id)


            url = 'https://notify-api.line.me/api/notify'
            token = 'xuVeGPqonotndJpC5VAqH0E51FiimOlnkDhXg5t5S62'
            headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}

            msg = ("หมายเลขงาน : "+ str(form_detail.id) +",\r\n\r\nชื่อ Login ผู้แจ้งปัญหา : "+ form_detail.user.username +",\r\n\r\nประจำงวดงาน : "+ form_detail.installment.installment +",\r\n\r\nสถานที่ตั้งอุปกรณ์ : "+ str(form_detail.place) +", \r\n\r\nหน่วยงาน : "+ form_detail.institution +",\r\n\r\nผู้แจ้งปัญหา : "+ form_detail.informer +",\r\n\r\nเบอร์โทรศัพท์ : "+ form_detail.phone_number +",\r\n\r\nวันที่แจ้งปัญหา : "+ str(form_detail.issue_date) +",\r\n\r\nอุปกรณ์ : "+ str(form_detail.device_name) +",\r\n\r\nยี่ห้อ : "+ form_detail.brand +",\r\n\r\nรุ่น : "+ form_detail.model +",\r\n\r\nหมายเลขคุรุภัณฑ์ : "+ form_detail.inventory_number +",\r\n\r\nหมายเลขประจำอุปกรณ์ : "+ form_detail.serial_number +",\r\n\r\nปัญหาที่เกิดขึ้น : "+ form_detail.issue +",\r\n\r\nผู้รับผิดชอบ : "+ form_detail.responsibility +",\r\n\r\nรายละเอียดการซ่อม : "+ form_detail.detail +",\r\n\r\nวันที่ซ่อมเสร็จ : "+ str(form_detail.job_complete_date) +",\r\n\r\nสถานะซ่อมบำรุง : "+ form_detail.status +" ")


            r = requests.post(url, headers=headers, data = {'message':msg})
            print(r.text)

            #print(form_detail.status)
            
            
            return redirect('helpdeskapp:mylist')
        else:
            print('Error :', form.errors)

    context = {
        'form': form,
        'addticket_edit': addticket_edit
    
    }
    return render(request, 'helpdeskapp/edit.html', context)

@login_required
def mylist(request):
    ticket_list = AddTicket.objects.all()
    #print([e.status for e in AddTicket.objects.all()])
    context = {'ticket_list': ticket_list}
    return render(request, 'helpdeskapp/mylist.html', context)


@login_required
def DoAction(request, action):
    username = str(request.user.username).lower()
    if username.startswith("admin"):
        print('username')
        data_list = AddTicket.objects.filter(status = action)
        print('data_list')
    else:
        data_list = AddTicket.objects.filter(status = action, user = request.user)
    context = {'data_list': data_list, 'action': action}
    return render(request, 'helpdeskapp/doaction.html', context)


@login_required
def query_data(request):
    query_list = AddTicket.objects.all()

    context = {'query_list': query_list}
    return render(request, 'helpdeskapp/query.html', context)

# Export PDF Report
@login_required
def export_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Reports' + \
        str(datetime.datetime.now()) + '.pdf'

    response['Content-Transfer-Encoding'] = 'binary'

    reports = AddTicket.objects.filter(user=request.user)

    html_string = render_to_string(
        'helpdeskapp/pdf_output.html', {'reports': reports})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    
    return response

# Export XLS EXCEL Report
@login_required
def export_excel(request):

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Reports' + \
        str(datetime.datetime.now()) + '.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Reports')
    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['หมายเลขงาน','ประจำงวดงาน', 'ชื่อ Login ผู้แจ้งปัญหา', 'สถานที่ตั้งอุปกรณ์',
        'หน่วยงาน', 'วันที่แจ้งปัญหา', 'ผู้แจ้งปัญหา', 'ปัญหาที่เกิดขึ้น', 'อุปกรณ์',
        'ยี่ห้อ', 'รุ่น', 'หมายเลขคุรุภัณฑ์', 'หมายเลขประจำอุปกรณ์', 'มอบหมายงาน',
        'รายละเอียดในการซ่อม', 'งานค้าง', 'วันที่ซ่อมเสร็จ', 'วันที่ส่งคืนอุปกรณ์' ,'อุปกรณ์สำรอง', 'วันที่สำรองอุปกรณ์' 
    ]

    
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()

    rows = AddTicket.objects.filter(user=request.user).values_list(
        'id','installment__installment', 'user__username', 'place', 'institution', 'issue_date',
        'informer', 'issue', 'device_name__device_name', 'brand', 'model',
        'inventory_number', 'serial_number', 'delegation', 'detail',
        'blocklog', 'job_complete_date', 'give_back_date', 'spare_device' , 'spare_device_date'
    )
    
    for row in rows:
        row_num += 1

        
        for col_num in range(len(row)):
        #for col_num, row in enumerate(rows):
            ws.write(row_num, col_num, str(row[col_num]), font_style) 

    wb.save(response)

    return response

# Export Blank PDF
@login_required
def export_blank_pdf(request):

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; attachment; filename=Reports' + \
        str(datetime.datetime.now()) + '.pdf'

    response['Content-Transfer-Encoding'] = 'binary'

    reports = AddTicket.objects.filter(user=request.user)

    html_string = render_to_string(
        'helpdeskapp/blank_pdf.html', {'reports': reports})
    html = HTML(string=html_string)

    result = html.write_pdf()

    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    
    return response

