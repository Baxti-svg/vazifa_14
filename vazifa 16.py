# ********************1 misol*********************************
nyuton = {'ism':'Isaak Nyuton',
           'faoliyati':'fizik olim',
           'umri':77,
           'tjoy':'Angliya'
           }

xoshimov = {'ism':'Utkir Xoshimov',
           'faoliyati':'yozuvchi',
           'umri':75,
           'tjoy':'Toshkent'
           }

rokfeller = {'ism':'Jorj Rokfeller',
           'faoliyati':'bisnesmen',
           'umri':95,
           'tjoy':'AQSH'
           }

jekson = {'ism':'Maykl Jekson',
           'faoliyati':'artist',
           'umri':60,
           'tjoy':'AQSH'
           }

shaxslar = [nyuton, xoshimov, rokfeller, jekson]

for shaxs in shaxslar:
    ism = shaxs['ism']
    faoliyati = shaxs['faoliyati']
    umri = shaxs['umri']
    tjoy = shaxs['tjoy']
    print(f"{ism} {faoliyati}-bo'lgan {tjoy}da tavallud topgan va {umri} yil yawagan raxmatli. ")