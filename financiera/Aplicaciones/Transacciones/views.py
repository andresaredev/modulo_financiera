from django.utils import timezone
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Models.Transacciones.TransaccionModel import Transaccion
from django.core import serializers

# Create your views here.

def test(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'Si funciona'})
    return JsonResponse('Error')

@csrf_exempt
def crear(request):
    if request.method == 'POST':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            nueva_transaccion = Transaccion(
                id_transaccion=datos['id_transaccion'],
                fecha=timezone.now(),
                monto=datos['monto'],
                tipo_transaccion=datos['tipo_transaccion'],
                id_cliente=datos['id_cliente'],
                id_presupuesto=datos['id_presupuesto'],
                id_activo_fijo=datos['id_activo_fijo'],
                id_informe=datos['id_informe'])
            nueva_transaccion.save()
            print('DATOS CON EL MODELO',nueva_transaccion)
            return JsonResponse({'message': 'Nueva transaccion creada'}) 
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)

    else:
        return JsonResponse({'Error': 'Método no permitido'})


def obtener(request):
    if request.method == 'GET':
        try:
            transaccion = Transaccion.objects.all().values()
            print('DATOS CON EL MODELO',transaccion)
            return JsonResponse({'transacciones': list(transaccion)}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
        

@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            transaccion = Transaccion.objects.get(id_transaccion=id)
            transaccion.fecha = transaccion.fecha
            transaccion.monto = datos['monto']
            transaccion.tipo_transaccion = datos['tipo_transaccion']
            transaccion.id_cliente = datos['id_cliente']
            transaccion.id_presupuesto = datos['id_presupuesto']
            transaccion.id_activo_fijo = datos['id_activo_fijo']
            transaccion.id_informe = datos['id_informe']
            transaccion.save()
            print('DATOS CON EL MODELO',transaccion)
            return JsonResponse({'message': 'Transaccion actualizada'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    
@csrf_exempt 
def eliminar(request, id):
    if request.method == 'DELETE':
        try:
            transaccion = Transaccion.objects.get(id_transaccion=id)
            transaccion.delete()
            return JsonResponse({'message': 'Transaccion eliminada'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})