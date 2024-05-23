import datetime
import json
from time import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Models.GestionCuentas.CuentasPorCobrar import CuentasPorCobrar
from Models.GestionCuentas.CuentasPorPagar import CuentasPorPagar
from django.db.models import Max

# Create your views here.
def prueba(request):
    if request.method == 'GET':
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'method not supported'})
    
def obtenerCC(request):
    if request.method == 'GET':
        try:
            cuenta = CuentasPorCobrar.objects.all().values()
            print('DATOS CON EL MODELO HOLAHOLA',cuenta)
            return JsonResponse({'cuenta': list(cuenta)}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    


@csrf_exempt
def crearCC(request):
    if request.method == 'POST':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            max_id = CuentasPorCobrar.objects.all().aggregate(Max('id_cuenta_pc'))['id_cuenta_pc__max']
            next_id = (max_id or 0) + 1

            nueva_cuenta = CuentasPorCobrar(
                id_cuenta_pc = next_id,
                monto_pendiente=datos['monto_pendiente'],
                fecha_vencimiento=datos['fecha_vencimiento'],
                id_cliente=datos['id_cliente'],
                id_transaccion=datos['id_transaccion'],
               )
            nueva_cuenta.save()
            print('DATOS CON EL MODELO',nueva_cuenta)
            return JsonResponse({'message': 'Nueva transaccion creada'}) 
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)

    else:
        return JsonResponse({'Error': 'Método no permitido'})


@csrf_exempt
def actualizarCC(request, id):
    if request.method == 'PUT':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            cuenta = CuentasPorCobrar.objects.get(id_cuenta_pc = id)
            cuenta.monto_pendiente = datos['monto_pendiente']
            cuenta.fecha_vencimiento = datos['fecha_vencimiento']
            cuenta.id_cliente = datos['id_cliente']
            cuenta.id_transaccion = datos['id_transaccion']
            cuenta.save()
            print('DATOS CON EL MODELO',cuenta)
            return JsonResponse({'cuenta': 'Cuenta actualizada'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)

@csrf_exempt   
def eliminarCC(request, id):
    if request.method == 'DELETE':
        try:
            cuenta = CuentasPorCobrar.objects.get(id_cuenta_pc=id)
            cuenta.delete()
            print('DATOS CON EL MODELO',cuenta)
            return JsonResponse({'cuenta': 'Cuenta eliminada'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    

def obtenerCP(request):
    if request.method == 'GET':
        try:
            cuenta = CuentasPorPagar.objects.all().values()
            print('DATOS CON EL MODELO HOLAHOLA',cuenta)
            return JsonResponse({'cuenta': list(cuenta)}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})
    
@csrf_exempt
def crearCP(request):
    if request.method == 'POST':
        try:
            datos = json.loads(request.body)
            print('DATA', datos)

            max_id = CuentasPorPagar.objects.all().aggregate(Max('id_cuenta_pp'))['id_cuenta_pp__max']
            next_id = (max_id or 0) + 1

            nueva_cuenta = CuentasPorPagar(
                id_cuenta_pp=next_id,
                numero_factura=datos['numero_factura'],
                monto_pendiente=datos['monto_pendiente'],
                fecha_vencimiento=datos['fecha_vencimiento'],
                proveedor_debe=datos['proveedor_debe'],
                estado=datos['estado'],
                id_transaccion=datos['id_transaccion'],
            )
            nueva_cuenta.save()
            return JsonResponse({'message': 'Nueva transaccion creada'}) 
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})


@csrf_exempt
def actualizarCP(request, id):
    if request.method == 'PUT':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            cuenta = CuentasPorPagar.objects.get(id_cuenta_pp = id)
            cuenta.numero_factura=datos['numero_factura']
            cuenta.monto_pendiente=datos['monto_pendiente']
            cuenta.fecha_vencimiento=datos['fecha_vencimiento']
            cuenta.proveedor_debe=datos['proveedor_debe']
            cuenta.estado=datos['estado']
            cuenta.id_transaccion=datos['id_transaccion']
            cuenta.save()
            print('DATOS CON EL MODELO',cuenta)
            return JsonResponse({'cuenta': 'Cuenta actualizada'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
        
@csrf_exempt
def eliminarCP(request, id):
    if request.method == 'DELETE':
        try:
            cuenta = CuentasPorPagar.objects.get(id_cuenta_pp=id)
            cuenta.delete()
            print('DATOS CON EL MODELO',cuenta)
            return JsonResponse({'cuenta': 'Cuenta eliminada'}, status=200)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Formato Json inválido en el cuerpo de la solicitud'}, status=400)
    else:
        return JsonResponse({'Error': 'Método no permitido'})