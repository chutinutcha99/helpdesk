# Generated by Django 3.2.9 on 2022-01-23 11:18

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Change_Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('change_device', models.CharField(max_length=255, verbose_name='เปลี่ยนอุปกรณ์หรือไม่?')),
            ],
        ),
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(max_length=255, verbose_name='อุปกรณ์')),
            ],
        ),
        migrations.CreateModel(
            name='InstallMent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('installment', models.CharField(max_length=255, verbose_name='ประจำงวด')),
            ],
        ),
        migrations.CreateModel(
            name='OS_System',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('os_system_name', models.CharField(max_length=255, verbose_name='ระบบปฏิบัติการ')),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=255, verbose_name='สถานะการซ่อม')),
            ],
        ),
        migrations.CreateModel(
            name='AddTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='สถานที่ตั้งอุปกรณ์')),
                ('institution', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หน่วยงาน')),
                ('informer', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='ผู้แจ้งปัญหา')),
                ('phone_number', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=50, null=True, verbose_name='เบอร์โทรศัพท์')),
                ('issue_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='วันที่แจ้งปัญหา')),
                ('issue', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='ปัญหาที่เกิดขึ้น')),
                ('brand', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='ยี่ห้อ')),
                ('model', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='รุ่น')),
                ('inventory_number', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หมายเลขคุรุภัณฑ์')),
                ('serial_number', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หมายเลขประจำอุปกรณ์')),
                ('delegation', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='มอบหมายงาน')),
                ('responsibility', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='ผู้รับผิดชอบ')),
                ('detail', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='รายละเอียดในการซ่อม')),
                ('blocklog', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='งานค้าง')),
                ('status', models.CharField(choices=[('PROCESSING', 'กำลังซ่อม'), ('COMPLETE', 'ซ่อมเสร็จแล้ว'), ('CANCEL', 'ยกเลิก')], max_length=255, verbose_name='สถานะการซ่อมบำรุง')),
                ('job_complete_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='วันที่ซ่อมเสร็จ')),
                ('reason', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หมายเหตุ')),
                ('give_back_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='วันที่ส่งคืนอุปกรณ์')),
                ('spare_device', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='อุปกรณ์สำรอง')),
                ('serial_number_spare', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หมายเลขอุปกรณ์สำรอง')),
                ('spare_device_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='วันที่สำรองอุปกรณ์')),
                ('got_back_spare_device_date', models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='วันที่รับคืนอุปกรณ์สำรอง')),
                ('change_device_name', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='อุปกรณ์ที่เปลี่ยน')),
                ('change_for_brand', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='ยี่ห้อที่เปลี่ยน')),
                ('change_for_model', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='รุ่นที่เปลี่ยน')),
                ('change_for_serial_number', models.CharField(blank=True, default='กรุณาป้อนข้อมูล', max_length=255, null=True, verbose_name='หมายเลขอุปกรณ์ที่เปลี่ยน')),
                ('upload_image_before', models.FileField(blank=True, null=True, upload_to='file_uploads', verbose_name='ภาพก่อนซ่อม')),
                ('upload_image_after', models.FileField(blank=True, null=True, upload_to='file_uploads', verbose_name='ภาพหลังซ่อม')),
                ('change_device', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdeskapp.change_device', verbose_name='เปลี่ยนอุปกรณ์หรือไม่?')),
                ('device_name', models.ForeignKey(default='กรุณาป้อนข้อมูล', on_delete=django.db.models.deletion.CASCADE, to='helpdeskapp.devices', verbose_name='อุปกรณ์')),
                ('installment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdeskapp.installment', verbose_name='ประจำงวด')),
                ('os_system_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='helpdeskapp.os_system', verbose_name='ระบบปฏิบัติการ')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AddTicket',
            },
        ),
    ]
