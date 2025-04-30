# ********************1 misol*********************************
nyuton = {'ism':'Isaak Nyuton',
           'faoliyati':'fizik olim',
           'umri':77,
           'tjoy':'Angliya',
           'ishlari':["Nyutonning 1 qonuni", "Nyutonning 2 qonuni", "Nyutonning 3 qonuni"]
           }

xoshimov = {'ism':'Utkir Xoshimov',
           'faoliyati':'yozuvchi',
           'umri':75,
           'tjoy':'Toshkent',
           'ishlari':["Daftar xowiyasidagi bitiklar", "2 ewik orasi", "Nur borki soya bor"]
           }

rokfeller = {'ism':'Jon Rokfeller',
           'faoliyati':'bisnesmen',
           'umri':95,
           'tjoy':'AQSH',
           'ishlari':["neft savdosi", "investor", "odam savdosi"]
           }

jekson = {'ism':'Maykl Jekson',
           'faoliyati':'artist',
           'umri':60,
           'tjoy':'AQSH',
           'ishlari':["quwiq aytgan", "raqsga tuwgan", "aktyorlik qilgan"]
           }

shaxslar = [nyuton, xoshimov, rokfeller, jekson]

# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     faoliyati = shaxs['faoliyati']
#     umri = shaxs['umri']
#     tjoy = shaxs['tjoy']
#     print(f"{ism} {faoliyati}-bo'lgan {tjoy}da tavallud topgan va {umri} yil yawagan raxmatli. ")



# ********************2 misol*********************************
for shaxs in shaxslar:
     ism = shaxs['ism']
     ishlari = shaxs['ishlari']
     print(f"\n{ism} ning mashxur ishlari: ")
     for ish in ishlari:
         print(ish)