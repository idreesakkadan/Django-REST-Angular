from django.shortcuts import render,HttpResponse,redirect,get_object_or_404,get_list_or_404
from .models import Student,District
# from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StudentSerializer,DistrictSerializer

# Create your views here.

class StudentCreateView(APIView):
    def get(self,request):

        ins_student = Student.objects.all()
        serializer = StudentSerializer(ins_student,many=True)
        return Response(serializer.data)

    def post(self, request):
        ins_student = Student()

        data = request.data
        
        ins_student.vchr_name = data['strName']
        ins_student.vchr_reg = data['strReg']
        ins_student.vchr_gender = data['strGender']
        ins_student.dat_dob = data['datDob']
        ins_student.fk_district = District(data['fkDistrict'])
        ins_student.vchr_address = data['strAddress']
        ins_student.vchr_languages = data['strLanguages']
        ins_student.save()
        
        return Response({'student':ins_student})

class StudentEditView(APIView):
    def get(self,request,pk):
        ins_student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(ins_student)
        return Response(serializer.data)


    def put(self, request, pk):
        ins_student = Student.objects.get(pk=pk)
        
        data = request.data

        ins_student.vchr_name = data['strName']
        ins_student.vchr_reg = data['strReg']
        ins_student.vchr_gender = data['strGender']
        ins_student.dat_dob = data['datDob']
        ins_student.fk_district = District(data['fkDistrict'])
        ins_student.vchr_address = data['strAddress']
        ins_student.vchr_languages = data['strLanguages']
        ins_student.save()


        return Response({'student':ins_student})

    def delete(self,request,pk):
        ins_student = Student.objects.get(pk_bint_id=pk)
        ins_student.delete()
        return Response()

    
        