import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from Models.Proveedor.ProveedorModel import Proveedor
# Create your views here.

def prueba(request):
    if request.method == 'GET':
        try:
            return JsonResponse({'message': 'success'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Method Not Allowed'})


def obtener(request):
    if request.method == 'GET':
        try:
            proveedores = Proveedor.objects.all().values()
            return JsonResponse({'proveedores': list(proveedores)}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Method Not Allowed'})


@csrf_exempt
def crear(request):
    if request.method == 'POST':
        try:
            
            datos = json.loads(request.body)
            proveedor = Proveedor(
                id_proveedor=datos['id_proveedor'],
                nombre=datos['nombre'],
                direccion=datos['direccion'],
                telefono=datos['telefono'],
                tipo_proveedor=datos['tipo_proveedor'],
                condiciones_pago=datos['condiciones_pago'],
                id_cuenta_pp=datos['id_cuenta_pp']
            )
            proveedor.save()
            return JsonResponse({'proveedor': 'Proveedor creado'}, status=200)
        except Exception as e:
            return JsonResponse({'error': e}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    

@csrf_exempt
def actualizar(request, id):
    if request.method == 'PUT':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            proveedor = Proveedor.objects.get(id_proveedor=id)
            proveedor.nombre = datos['nombre']
            proveedor.direccion = datos['direccion']
            proveedor.telefono = datos['telefono']
            proveedor.tipo_proveedor = datos['tipo_proveedor']
            proveedor.condiciones_pago = datos['condiciones_pago']
            proveedor.id_cuenta_pp = datos['id_cuenta_pp']
            proveedor.save()
            return JsonResponse({'proveedor': 'Proveedor actualizado'}, status=200)
        except Exception as e:
            return JsonResponse({'error': e}, status=400)
    return JsonResponse({'error': 'Method not found'}, status=400)


@csrf_exempt
def eliminar(request, id):
    if request.method == 'DELETE':
        try:
            proveedor = Proveedor.objects.get(id_proveedor=id)
            proveedor.delete()
            return JsonResponse({'proveedor': 'Proveedor eliminado'}, status=200)
        except Exception as e:
            return JsonResponse({'error': e}, status=400)
    return JsonResponse({'error': 'Method not found'}, status=400)