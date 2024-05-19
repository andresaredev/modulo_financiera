import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Models.Presupuesto.Presupuesto import Presupuesto

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
            Presuepuestos = Presupuesto.objects.all().values()
            print('DATOS CON EL MODELO HOLAHOLA', Presuepuestos)
            return JsonResponse({'informe': list(Presuepuestos)}, status=200)
        except Exception as e:
            return JsonResponse({'error': e})
        

@csrf_exempt
def crear(request):
    try:
        if request.method == 'POST':
            data = json.loads(request.body)
            print(data)
            presupuesto = Presupuesto(
                id_presupuesto=data['id_presupuesto'],
                año_fiscal=data['año_fiscal'],
                cantidad_asignada=data['cantidad_asignada'],
                cantidad_gastada=data['cantidad_gastada']
            )
            presupuesto.save()
            return JsonResponse({'presupuesto': 'Presupuesto creado'}, status=200)
        
    except Exception as e:
        return JsonResponse({'error': e}, status=400)
    

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