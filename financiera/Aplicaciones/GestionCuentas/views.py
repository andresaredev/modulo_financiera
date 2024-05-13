import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Models.GestionCuentas.CuentasPorCobrar import CuentasPorCobrar

# Create your views here.
def prueba(request):
    if request.method == 'GET':
        return JsonResponse('message', 'success')
    else:
        return JsonResponse('message', 'method not supported')
    
def obtener(request):
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
def crear(request):
    if request.method == 'POST':
        try:
            datos =  json.loads(request.body)
            print('DATOS DESDE POSTMAN',datos)
            nueva_cuenta = CuentasPorCobrar(
                id_cuenta_pc = datos['id_cuenta_pc'],
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
