from firebase import firebase

# Tắt sử dụng process pool nếu thư viện hỗ trợ cờ này
try:
    firebase.async_compatible.use_process_pool = False
except Exception as e:
    print("Cannot disable process pool:", e)
    
firebase = firebase.FirebaseApplication('https://tt-iot-utex-default-rtdb.firebaseio.com/',None)
pk = '/PHONG_KHACH'
led01 = '/LED01'
led02 = '/LED02'

result = firebase.put(pk, led01, 'ON')
result = firebase.put(pk, led02, 'OFF')

result_pk = firebase.get(pk, None)
print("firebase.get(pk, None): ", result_pk)
result1 = firebase.get(pk, led01)
print("firebase.get(pk, led01): ", result1)
result2 = firebase.get(pk, led02)
print("firebase.put(pk, led02, 'OFF'): ", result2)
