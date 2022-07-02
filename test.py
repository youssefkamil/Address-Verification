import requests

url = 'http://127.0.0.1:5000/'

#if you want to verify one address uncomment the following lines

# Address  = " مكرم عبيد مدينة نصر "
# Address_json = {'Address': Address}
# x = requests.post(url, json=Address_json)
# x=x.json()
# print("success: ", x['success'])
# print("Address: ", x['Address'])
# print('confidence : ' ,x['confidence'])
# print( 'time : ', x['time'])



#Verify multiple addresses inside Cairo with speed up

CairoAddresses = list(['المبيضة، قسم روض الفرج',
                '6 أكتوبر، بركة النصر، قسم أول السلام، محافظة القاهرة',
                'إمتداد أحمد حلمي، الخازندارة',
                'ممدوح سالم الأستاد',
                'الأيقونة ثانى القاهرة الجديدة،'
                'عزبة علام المرج البحرية'])

for Address in CairoAddresses:
    Address_json = {'Address': Address,"speed_up":1}
    x = requests.post(url, json=Address_json)
    x=x.json()
    print("speed_up: ", Address_json['speed_up'])
    print("Address: ", x['Address'])
    print('confidence : ' ,x['confidence'])
    print( 'time : ', x['time'])
    print('-----------------------------------------------------')

print('=========================================================')

#Verify multiple addresses outside Egypt without speed up
OutCairoAddresses = list([  'ش فيصل، فيصل، قسم العمرانية ',
                            'حسين إسماعيل المنيب، قسم الجيزة،',
                            'الحمراء الثانية، قسم ثان أسيوط',
                            'بني مر مركز الفتح',
                            'مصطفى كامل، مدينة سمالوط',
                            'مركز كفر الدوار البحيرة',])

for Address in OutCairoAddresses:
    Address_json = {'Address': Address,"speed_up":0}
    x = requests.post(url, json=Address_json)
    x=x.json()
    print("speed_up: ", Address_json['speed_up'])
    print("Address: ", x['Address'])
    print('confidence : ' ,x['confidence'])
    print( 'time : ', x['time'])
    print('-----------------------------------------------------')