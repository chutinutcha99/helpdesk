import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUSES_CHOICES = (
    ('PROCESSING', 'กำลังซ่อม'),
    ('COMPLETE', 'ซ่อมเสร็จแล้ว'),
    ('CANCEL', 'ยกเลิก'),
)

class InstallMent(models.Model):
    installment = models.CharField(verbose_name='ประจำงวด', max_length=255)

    def __str__(self):
        return self.installment

class Devices(models.Model):
    device_name = models.CharField(verbose_name='อุปกรณ์', max_length=255)

    def __str__(self):
        return self.device_name

class OS_System(models.Model):
    os_system_name = models.CharField(verbose_name='ระบบปฏิบัติการ', max_length=255)

    def __str__(self):
        return self.os_system_name

class Status(models.Model):
    status = models.CharField(verbose_name='สถานะการซ่อม', max_length=255)

    def __str__(self):
        return self.status

class Change_Device(models.Model):
    change_device = models.CharField(verbose_name='เปลี่ยนอุปกรณ์หรือไม่?', max_length=255)

    def __str__(self):
        return self.change_device

class AddTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    installment = models.ForeignKey(InstallMent, on_delete=models.CASCADE, verbose_name='ประจำงวด')
    place = models.CharField(verbose_name='สถานที่ตั้งอุปกรณ์', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    institution = models.CharField(verbose_name='หน่วยงาน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    informer = models.CharField(verbose_name='ผู้แจ้งปัญหา', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    phone_number = models.CharField(verbose_name='เบอร์โทรศัพท์', null=True, blank=True, max_length=50, default='กรุณาป้อนข้อมูล')
    issue_date = models.DateField(default=datetime.date.today, verbose_name='วันที่แจ้งปัญหา', null=True, blank=True)
    issue = models.CharField(verbose_name='ปัญหาที่เกิดขึ้น', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    device_name = models.ForeignKey(Devices, on_delete=models.CASCADE, verbose_name='อุปกรณ์', default='กรุณาป้อนข้อมูล')
    brand = models.CharField(verbose_name='ยี่ห้อ', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    model = models.CharField(verbose_name='รุ่น', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    inventory_number = models.CharField(verbose_name='หมายเลขคุรุภัณฑ์', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    serial_number = models.CharField(verbose_name='หมายเลขประจำอุปกรณ์', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    os_system_name = models.ForeignKey(OS_System, on_delete=models.CASCADE, verbose_name='ระบบปฏิบัติการ')
    delegation = models.CharField(verbose_name='มอบหมายงาน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    responsibility = models.CharField(verbose_name='ผู้รับผิดชอบ', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    detail = models.CharField(verbose_name='รายละเอียดในการซ่อม', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    blocklog = models.CharField(verbose_name='งานค้าง', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    status = models.CharField(max_length=255, choices=STATUSES_CHOICES, verbose_name='สถานะการซ่อมบำรุง')
    job_complete_date = models.DateField(default=datetime.date.today, verbose_name='วันที่ซ่อมเสร็จ', null=True, blank=True)
    reason = models.CharField(verbose_name='หมายเหตุ', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    give_back_date = models.DateField(default=datetime.date.today, verbose_name='วันที่ส่งคืนอุปกรณ์', null=True, blank=True)
    spare_device = models.CharField(verbose_name='อุปกรณ์สำรอง', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    serial_number_spare = models.CharField(verbose_name='หมายเลขอุปกรณ์สำรอง', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    spare_device_date = models.DateField(default=datetime.date.today, verbose_name='วันที่สำรองอุปกรณ์', null=True, blank=True)
    got_back_spare_device_date = models.DateField(default=datetime.date.today, verbose_name='วันที่รับคืนอุปกรณ์สำรอง', null=True, blank=True)
    change_device = models.ForeignKey(Change_Device, on_delete=models.CASCADE, verbose_name='เปลี่ยนอุปกรณ์หรือไม่?', null=True, blank=True)
    change_device_name = models.CharField(verbose_name='อุปกรณ์ที่เปลี่ยน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    change_for_brand = models.CharField(verbose_name='ยี่ห้อที่เปลี่ยน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    change_for_model = models.CharField(verbose_name='รุ่นที่เปลี่ยน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    change_for_serial_number = models.CharField(verbose_name='หมายเลขอุปกรณ์ที่เปลี่ยน', max_length=255, null=True, blank=True, default='กรุณาป้อนข้อมูล')
    upload_image_before = models.FileField(upload_to='file_uploads', null=True, blank=True, verbose_name='ภาพก่อนซ่อม')
    upload_image_after = models.FileField(upload_to='file_uploads', null=True, blank=True, verbose_name='ภาพหลังซ่อม')

    original_status = None
    original_detail = None

    def save(self, *args, **kwargs):    
        if self._state.adding:
            super().save(*args, **kwargs)
            self.original_status = self.status 
            self.original_detail = self.detail           
        else:
            super().save(*args, **kwargs)

    def modified_data(self):
        result_text = 'มีการเปลี่ยนแปลงข้อมูล\n'
        result_text += f'สถานะการซ่อม {self.status}\n' if self.original_status != self.status else ''
        result_text += f'รายละเอียดการซ่อม {self.detail}\n' if self.original_detail != self.detail else ''

        self.original_status = self.status
        self.original_detail = self.detail
        return result_text

    def __str__(self):
        return self.user.username + ' - ' + str(self.status) + ' - ' + str(self.id)
         
    class Meta:
        verbose_name_plural = 'AddTicket'
    