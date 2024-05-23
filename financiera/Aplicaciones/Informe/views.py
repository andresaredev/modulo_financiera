import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from Models.Informe.InformeFinanciero import InformeFinanciero
from django.db.models import Max
from django.utils import timezone
# Create your views here.


def prueba(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'method not supported'})


def obtener(request):
    if request.method == 'GET':
        try:
            informe = InformeFinanciero.objects.all().order_by('id_informe').values()
            return JsonResponse({'informe': list(informe)}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'})


@csrf_exempt
def crear(request):
    if request.method == 'POST':
        try:
            max_id = InformeFinanciero.objects.all().aggregate(Max('id_informe'))['id_informe__max']
            next_id = (max_id or 0) + 1

            datos = json.loads(request.body)
            print('DATOS DESDE POSTMAN', datos)
            nuevo_informe = InformeFinanciero(
                id_informe=next_id,
                nombre_informe=datos['nombre_informe'],
                fecha=timezone.now(),
                tipo_informe=datos['tipo_informe'],
                detalle_informe=datos['detalle_informe'],
                nombre_responsable=datos['nombre_responsable'],
                id_transaccion_financiera=datos['id_transaccion_financiera']
            )
            nuevo_informe.save()
            print('DATOS CON EL MODELO', nuevo_informe)
            return JsonResponse({'message': 'Nuevo informe creado'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)


@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        try:
            datos = json.loads(request.body)
            print('DATOS DESDE POSTMAN', datos)
            informe = InformeFinanciero.objects.get(id_informe=id)
            informe.nombre_informe=datos['nombre_informe']
            informe.fecha=informe.fecha
            informe.tipo_informe=datos['tipo_informe']
            informe.detalle_informe=datos['detalle_informe']
            informe.nombre_responsable=datos['nombre_responsable']
            informe.id_transaccion_financiera=datos['id_transaccion_financiera']
            informe.save()
            print('DATOOOOSS', informe.tipo_informe)
            return JsonResponse({'informe': 'Informe actualizado'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    
@csrf_exempt
def eliminar(request, id):
    if request.method == 'DELETE':
        try:
            informe = InformeFinanciero.objects.get(id_informe=id)
            informe.delete()
            return JsonResponse({'message': 'Informe eliminado'})
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
