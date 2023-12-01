import json
import requests
from django.views import View
from django.shortcuts import render, HttpResponse, redirect

import hmac
import uuid
import base64
import hashlib


def gen_hmacsha256(key, signature_data):
    hmac_sha256 = hmac.new(key.encode(
        'utf-8'), signature_data.encode('utf-8'), hashlib.sha256)
    signature = base64.b64encode(hmac_sha256.digest()).decode('utf-8')
    return signature

# def gen_hmacshan256(ky, data):
#     hmac_shan256 = hmac.new(ky.encode('utf-8'), data.encode('utf-8'), hashlib.sha256)
#     signature = base64.b64encode(hmac_shan256.digest()).decode('utf-8')
#     return signature


# def home(request):
#     total_amount = 110
#     secret_key = '8gBm/:&EnhH.1/q'
#     transaction_uuid = uuid.uuid4()
#     signature_data = (
#         f"total_amount={total_amount},"
#         f"transaction_uuid={transaction_uuid},"
#         f"product_code=EPAYTEST"
#     )

#     signature = gen_hmacsha256(secret_key, signature_data)

#     context = {
#         'amount':100,
#         'tax_amount':10,
#         'total_amount':110,
#         'signature': signature,
#         'product_code':'EPAYTEST',
#         'transaction_uuid': transaction_uuid,
#     }

#     return render(request, 'home.html', context)



# def esewaPaymentVerification(request):
#     data = request.GET.get('data')
#     decoded_data = base64.b64decode(data).decode('utf-8')
#     map_data = json.loads(decoded_data)
#     if map_data.get('status') == 'COMPLETE':
#         print('eSewa payment completed')
#     return redirect('/')


def home(request):
    uid = uuid.uuid4()
    context = {
        'uid':uid,
        'return_url':'http://127.0.0.1:8000/verify-khalti-payment'
    }

    return render(request, 'home.html', context)

def khaltipayment(request):
    return_url = request.POST.get('return_url')
    amount = request.POST.get('amount')
    purchase_order_id = request.POST.get('purchase_order_id')

    url = "https://a.khalti.com/api/v2/epayment/initiate/"

    payload = json.dumps({
        "return_url": return_url,
        "website_url": "https://127.0.0.1:8000",
        "amount": amount,
        "purchase_order_id": purchase_order_id,
        "purchase_order_name": "test",
        "customer_info": {
        "name": "Ram Bahadur",
        "email": "test@khalti.com",
        "phone": "9800000001"
        }
    })
    headers = {
        'Authorization': 'key c1bf38dde5fb4426b7f9e361e472655d',
        'Content-Type': 'application/json',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    return redirect(response['payment_url'])



def khaltiPaymentVerification(request):
    url = "https://a.khalti.com/api/v2/epayment/lookup/"
    headers = {
        'Authorization': 'key c1bf38dde5fb4426b7f9e361e472655d',
        'Content-Type': 'application/json',
    }
    pidx = request.GET.get('pidx')

    payload = json.dumps({
        'pidx':pidx
    })

    response = requests.request("POST", url, headers=headers, data=payload)
    response = json.loads(response.text)

    if response['status'] == 'Completed':
        return redirect('/')






# def generate_hmac_signature(payload, secret_key):
#     # Sort the payload parameters alphabetically
#     sorted_params = sorted(payload.items())
#     print('******************')
#     print(sorted_params)
#     print('******************')

#     # Concatenate the sorted parameter values
#     concatenated_values = ''.join(str(value) for param, value in sorted_params)

#     # Generate the HMAC using SHA-256 and the secret key
#     hashed = hmac.new(secret_key.encode('utf-8'),
#                       concatenated_values.encode('utf-8'), hashlib.sha256)

#     # Encode the result in base64
#     signature = base64.b64encode(hashed.digest()).decode('utf-8')

#     return signature





# def home(request):
#     uuids = uuid.uuid4()
#     total_amount="110"
#     secret_key = '8gBm/:&EnhH.1/q'
#     payload = f"{total_amount},{uuids},EPAYTEST"
#     print(payload)

#     # Add the generated signature to the payload
#     payload = gen_hmacsha256(secret_key,payload)
#     print(payload)

#     return render(request, 'home.html', {'transaction_uuid':uuids,'signature':payload})



# def gen_hmacsha256(key,message):
#     key = key.encode('utf-8')
#     message = message.encode('utf-8')

#     hmac_sha256 = hmac.new(key, message, hashlib.sha256)
#     digest = hmac_sha256.digest()
#     signature = base64.b64encode(digest).decode('utf-8')
#     return signature




# class AsyncView(View):
#     def get(self, request):
#         url = "https://uat.esewa.com.np/epay/transrec"
#         parameters = {
#             'amt': request.GET.get('amt'),
#             'scd': 'EPAYTEST',
#             'rid': request.GET.get('refid'),
#             'pid': request.GET.get('oid'),
#         }
#         resp = req.get(url, parameters)
#         print(resp.text)
#         return HttpResponse(f'status_code---{resp.status_code}------{resp.text}')
