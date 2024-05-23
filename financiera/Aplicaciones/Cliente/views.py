import json
from django.http import JsonResponse
from django.shortcuts import render
from Models.Cliente.ClienteModel import Cliente
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max

# Create your views here.
def prueba(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message': 'method not supported'})


def obtener(request):
    if request.method == 'GET':
        try:
            clientes = Cliente.objects.all().values()
            return JsonResponse({'cliente': list(clientes)}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
        
@csrf_exempt
def crear(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            max_id = Cliente.objects.all().aggregate(Max('id_cliente'))['id_cliente__max']
            next_id = (max_id or 0) + 1
            nuevo_cliente = Cliente(
                id_cliente = next_id,
                nombre = datos['nombre'],
                direccion = datos['direccion'],
                correo = datos['correo'],
            )
            nuevo_cliente.save()
            return JsonResponse({'success':'Cliente creado exitosamente'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': e}, status=400)
        
@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        try:
            datos = json.loads(request.body)
            cliente = Cliente.objects.get(id_cliente=id)
            cliente.nombre = datos['nombre']
            cliente.direccion = datos['direccion']
            cliente.correo = datos['correo']
            cliente.save()
            return JsonResponse({'success':'Cliente actualizado exitosamente'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': e}, status=400)
        

@csrf_exempt
def eliminar(request, id):
    if request.method == 'DELETE':
        try:
            cliente = Cliente.objects.get(id_cliente=id)
            cliente.delete()
            return JsonResponse({'success':'Cliente eliminado exitosamente'})
        except Exception as e:
            print(e)
            return JsonResponse({'error': e}, status=400)
    else:
        return JsonResponse({'error':'method not found'}, status=400)