from django.db import models


class District(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_district_name = models.CharField(unique=True, max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'district'


class Student(models.Model):
    pk_bint_id = models.BigAutoField(primary_key=True)
    vchr_name = models.CharField(max_length=50, blank=True, null=True)
    vchr_reg = models.CharField(unique=True, max_length=30, blank=True, null=True)
    dat_dob = models.DateField(blank=True, null=True)
    vchr_gender = models.CharField(max_length=10, blank=True, null=True)
    vchr_address = models.CharField(max_length=300, blank=True, null=True)
    vchr_languages = models.CharField(max_length=50, blank=True, null=True)
    fk_district = models.ForeignKey(District, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'