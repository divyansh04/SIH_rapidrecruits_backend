from unicodedata import name
from django.shortcuts import render

from apis.models import ApplicantExperienceModel, ApplicantInfoModel, ApplicantQualificationModel, CollegeInfoModel, EmployeeInfoModel, VacanciesInfoModel, VacancyApplicantMapping, RecruitmentCommitteeInfoModel

from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, authenticate, logout
from rest_framework.views import APIView
from rest_framework.response import Response
import openpyxl
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from datetime import *
# Create your views here.

