from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CountrySerializer, UserSerializer, ReferalSerializer, StateSerializer, BankSerializer, GenderSerializer, DocumentSerializer
from .models import CountryMaster, UserMaster, ReferalMaster, StateMaster, BankMaster, GenderMaster, DocumentMaster
from rest_framework import status

# Create your views here.
con_list =['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'Andorra', 'Angola', 'Anguilla', 'Antigua & Barbuda', 'Argentina', 'Armenia', 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas, The', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin', 'Bermuda', 'Bhutan', 'Bolivia', 'Bosnia & Herzegovina', 'Botswana', 'Brazil', 'British Virgin Is.', 'Brunei', 'Bulgaria', 'Burkina Faso', 'Burma', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde', 'Cayman Islands', 'Central African Rep.', 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo, Dem. Rep.', 'Congo, Repub. of the', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire", 'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Faroe Islands', 'Fiji', 'Finland', 'France', 'French Guiana', 'French Polynesia', 'Gabon', 'Gambia, The', 'Gaza Strip', 'Georgia', 'Germany', 'Ghana', 'Gibraltar', 'Greece', 'Greenland', 'Grenada', 'Guadeloupe', 'Guam', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jersey', 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'Korea, North', 'Korea, South', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Martinique', 'Mauritania', 'Mauritius', 'Mayotte', 'Mexico', 'Micronesia, Fed. St.', 'Moldova', 'Monaco', 'Mongolia', 'Montserrat', 'Morocco', 'Mozambique', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'N. Mariana Islands', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania', 'Russia', 'Rwanda', 'Saint Helena', 'Saint Kitts & Nevis', 'Saint Lucia', 'St Pierre & Miquelon', 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia', 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', 'Tajikistan', 'Tanzania', 'Thailand', 'Togo', 'Tonga', 'Trinidad & Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Turks & Caicos Is', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates', 'United Kingdom', 'United States', 'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Virgin Islands', 'Wallis and Futuna', 'West Bank', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

@api_view(['GET','POST'])
def country_list(request):
    # for i in con_list:
    #     data = CountryMaster.objects.create(country_name=i)
    #     data.save()
    #     print(data)
    # return Response("Success")

    country_master = CountryMaster.objects.all()
    serializer = CountrySerializer(country_master, many =True)
    return Response(serializer.data, status = status.HTTP_200_OK)


user_type_list = [
'Admin',
'Staff',
'Student',
]

@api_view(['GET','POST'])
def user_list(request):
    # for type in user_type_list:
    #     data = UserMaster.objects.create(user_type = type)
    #     data.save()
    #     print(data)
    # return Response("Success")

    user_master = UserMaster.objects.all()
    serializer = UserSerializer(user_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

referal_type_list = [
'Facebook',
'Linkedin',
'Whatsapp',
'Others'
]

@api_view(['GET','POST'])
def referal_list(request):
    # for ref in referal_type_list:
    #     data = ReferalMaster.objects.create(referal_type = ref)
    #     data.save()
    #     print(data)
    # return Response("Referal Master Success")

    referal_master = ReferalMaster.objects.all()
    serializer = ReferalSerializer(referal_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

state_list_view = ['Andaman and Nicobar Islands', 'Andhra Pradesh', 'Arunachal Pradesh', 'Assam', 'Bihar', 'Chandigarh',
 'Chhattisgarh', 'Dadra and Nagar Haveli', 'Daman and Diu', 'Delhi', 'Goa', 'Gujarat', 'Haryana',
  'Himachal Pradesh', 'Jammu and Kashmir', 'Jharkhand', 'Karnataka', 'Kerala', 'Lakshadweep',
   'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram', 'Nagaland', 'Odisha',
    'Puducherry', 'Punjab', 'Rajasthan', 'Sikkim', 'Tamil Nadu', 'Tripura', 'Uttar Pradesh',
     'Uttarakhand', 'West Bengal']

@api_view(['GET','POST'])
def state_list(request):
    # for state in state_list_view:
    #     data = StateMaster.objects.create(state_name = state)
    #     data.save()
    #     print(data)
    # return Response("StateMaster Success")
    state_master = StateMaster.objects.all()
    serializer = StateSerializer(state_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

bank_list_view = [
'ABN-AMRO Bank',
'Abu Dhabi Commercial Bank Ltd',
'Allahabad Bank',
'American Express Bank Ltd',
'Andhra Bank',
'Axis Bank',
'Bank list',
'Bank of Baroda',
'Bank of India',
'Bank of Maharashtra',
'Bank of Rajasthan Ltd',
'Barclays Bank',
'BNP Paribas',
'Canara Bank',
'Catholic Syrian Bank Ltd',
'Central Bank of India',
'Citibank',
'City Union Bank Ltd',
'Corporation Bank',
'DBS Bank Ltd',
'Dena Bank',
'Deutsche Bank',
'Development Credit Bank Ltd',
'Dhanalakshmi Bank Ltd',
'Federal Bank Ltd',
'HDFC Bank Ltd',
'Hongkong & Shanghai Banking Corporation Ltd',
'ICICI Bank Ltd',
'Indian Bank',
'Indian Overseas Bank',
'IndusInd Bank Ltd',
'Industrial Development Bank of India (IDBI) Ltd',
'ING Vysya Bank Ltd',
'Jammu and Kashmir Bank Ltd',
'Karnataka Bank Ltd',
'Karur Vysya Bank Ltd',
'Kotak Mahindra Bank Ltd',
'Lakshmi Vilas Bank Ltd',
'Oriental Bank of Commerce',
'Punjab and Sind Bank',
'Punjab National Bank',
'SBI Commercial and International Bank Ltd',
'South Indian Bank Ltd',
'Standard Chartered Bank',
'State Bank of Bikaner and Jaipur',
'State Bank of Hyderabad',
'State Bank of India',
'State Bank of Indore',
'State Bank of Mauritius Ltd',
'State Bank of Mysore',
'State Bank of Patiala',
'State Bank of Travancore',
'Syndicate Bank',
'Tamilnad Mercantile Bank Ltd',
'UCO Bank',
'Union Bank of India',
'United Bank of India',
'United Western Bank Ltd',
'Vijaya Bank',
'Yes Bank Ltd',
]
@api_view(['GET','POST'])
def bank_list(request):
    # for bank in bank_list_view:
    #     data = BankMaster.objects.create(bank_name = bank)
    #     data.save()
    #     print(data)
    # return Response("BankMaster Success")

    bank_master = BankMaster.objects.all()
    serializer = BankSerializer(bank_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

gender_type_view = [
'Male', 'Female', 'Others'
]
@api_view(['GET','POST'])
def gender_list(request):
    # for type in gender_type_view:
    #     data = GenderMaster.objects.create(gender_type = type)
    #     data.save()
    #     print(data)
    # return Response("GenderMaster Success")

    gender_master = GenderMaster.objects.all()
    serializer = GenderSerializer(gender_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)

document_type_view = [
'Aadhar', 'VoterID', 'PAN'
]
@api_view(['GET','POST'])
def document_list(request):
    # for type in document_type_view:
    #     data = DocumentMaster.objects.create(document_type = type)
    #     data.save()
    #     print(data)
    # return Response("DocumentMaster Success")

    document_master = DocumentMaster.objects.all()
    serializer = DocumentSerializer(document_master, many = True)
    return Response(serializer.data, status = status.HTTP_200_OK)
