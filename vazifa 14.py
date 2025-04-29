#*********************1 misol******************************************
# otam = {'ismi':'eshpulat shayimov', 't_yili': '1955', 'manzil':'Surxondaryo vil'}
# print(f"{otam['ismi'].title()}, {otam['t_yili']}-yilda tugilgan, {otam['manzil']}-da yashaydi")

#*********************2 misol******************************************
python_izohli_lugati = {
    'integer':"Butun son",
    'float':"O'nlik son",
    'string':"Matn",
    'list':"Ro'yxat",
    'tuple':"O'zgarmas ro'yxat",
    'if':"agar",
    'else':"aks holda",
    'for':"uchun",
    'GitHub':"platforma",
    'while':"sikl"
    }
# print(python_izohli_lugati['else'])

#*********************3 misol******************************************
kalit = input("Kalit suz kiriting: ").lower()
print(python_izohli_lugati.get(kalit,"Bunday suz mavjud emas"))