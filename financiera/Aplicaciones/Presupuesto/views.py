import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Models.Presupuesto.Presupuesto import Presupuesto
from django.db.models import Max
from django.utils import timezone

# Create your views here.
def prueba(request):
    if request.method == 'GET':
        try:
            return JsonResponse({'message': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'method not supported'})


def obtener(request):
    if request.method == 'GET':
        try:
            Presuepuestos = Presupuesto.objects.all().order_by('id_presupuesto').values()
            print('DATOS CON EL MODELO HOLAHOLA', Presuepuestos)
            return JsonResponse({'presupuesto': list(Presuepuestos)}, status=200)
        except Exception as e:
            return JsonResponse({'error': e})
        

@csrf_exempt
def crear(request):
    if request.method == 'POST':
        try:
            max_id = Presupuesto.objects.all().aggregate(Max('id_presupuesto'))['id_presupuesto__max']
            next_id = (max_id or 0) + 1
            data = json.loads(request.body)
            print(data)
            presupuesto = Presupuesto(
                id_presupuesto=next_id,
                año_fiscal= timezone.now(),
                cantidad_asignada=data['cantidad_asignada'],
                cantidad_gastada=data['cantidad_gastada']
            )
            presupuesto.save()
            return JsonResponse({'presupuesto': 'Presupuesto creado'}, status=200)
        
        except Exception as e:
            return JsonResponse({'error': e}, status=400)
        
    return JsonResponse({'Error': 'method not found'})
    

@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        try:
            datos = json.loads(request.body)
            presupuesto = Presupuesto.objects.get(id_presupuesto=id)
            presupuesto.año_fiscal = datos['año_fiscal']
            presupuesto.cantidad_asignada = datos['cantidad_asignada']
            presupuesto.cantidad_gastada = datos['cantidad_gastada']
            presupuesto.save()
            print('DATOS CON EL MODELO', presupuesto)
            return JsonResponse({'presupuesto': 'Presupuesto actualizado'}, status=200)
        except Exception as e:
            return JsonResponse({'error': e}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    

@csrf_exempt
def eliminar(request, id):
    if request.method == 'DELETE':
        try:
            presupuesto = Presupuesto.objects.get(id_presupuesto=id)
            presupuesto.delete()
            return JsonResponse({'message': 'Presupuesto eliminado'})
        except Exception as e:
            return JsonResponse({'error': e}, status=400)