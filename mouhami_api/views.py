from rest_framework.decorators import api_view
from rest_framework.response import Response
from mouhami_api.models import Language, Lawyer, Specialities
from .serializers import LawyerSerializer, LanguageSerializer, SpecialitiesSerializer
import json


@api_view(['GET', 'POST'])
def lawyerData(request):
    # Read data from cabinets.json file
    with open('scraper/cabinets.json', 'r', encoding='utf-8') as json_file:
        cabinets_data = json.load(json_file)
    if request.method == 'POST':
    # Insert data into the database
        for data in cabinets_data:
            print(data)
            specialities_data = data.pop('specialities', [])
            languages_data = data.pop('languages', [])
    
            # Create and save Language instances
            language_instances = []
            for lang in languages_data:
                language_instance, created = Language.objects.get_or_create(name=lang)
                language_instances.append(language_instance)
    
            # Save Specialities instances
            speciality_instances = []
            for speciality_name in specialities_data:
                speciality_instance, created = Specialities.objects.get_or_create(name=speciality_name)
                speciality_instances.append(speciality_instance)
    
            # Create and save User instance (assuming 'email' is unique)
            #user_instance, created = User.objects.get_or_create(email=data['email'])
    
            # Create and save Lawyer instance
            lawyer_instance = Lawyer(**data)
            lawyer_instance.save()
    
            # Update many-to-many relationships
            lawyer_instance.languages.set(language_instances)
            lawyer_instance.specialities.set(speciality_instances)
    
        return Response({"data inserted to the database successfully!!"})

   
    elif request.method == 'GET':
        # Serialize data and return response
        serializer_lawyer = LawyerSerializer(Lawyer.objects.all(), many=True)
        lawyer_data = serializer_lawyer.data

        serializer_language = LanguageSerializer(Language.objects.all(), many=True)
        language_data = serializer_language.data

        serializer_specialities = SpecialitiesSerializer(Specialities.objects.all(), many=True)
        specialities_data = serializer_specialities.data

        return Response({
            "lawyers": lawyer_data,
            "languages": language_data,
            "specialities": specialities_data
        })
