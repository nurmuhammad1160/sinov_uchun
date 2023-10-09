# mavzu listlar ustida ishlash



# mevalar = ['olma', 'anor','olcha', 'banan','sliva', 'apelsin']

# mevalar.sort(reverse=True)
#  teskari aylantirib beradi va yana sort() alfabit bo'ylab tartiblaydi va sort(reverse(True)) alfabit boyicha teskari qiladi
# print(mevalar)


# sonlar = list(range(0, 6))
# summa = sum(sonlar)  sonlarni umumiy qiymatini topadi
# summa = max(sonlar)  sonlarni eng katta qiymatini topadi
# summa = min(sonlar)  sonlarni eng kichkina qiymatini topadi
# print(summa)
# print(len(sonlar)) sonlar qatorini sanaydi
# print(sonlar[10:21]) sonlarni qirqib olish
# sonlar.append('salom') listga malumot qo'shish
# print(sonlar)

# malumot = []
# ism = input("ismingizni kiriting: ")
# yosh = input("Yoshingizni kiriting: ")
# malumot.append(ism)
# malumot.append(yosh)
# print(malumot)


# ismlar = ['Salombek', 'Alikbek', 'Nurmuhammad','Testbek']
# ismlar.remove('Nurmuhammad')
# print(ismlar)


# lang = ('uz','ru','en') ozgarmas Tuple 
# lang2 = list(lang) ozgarmas Tupleni ozgaradigan Tuplega ozgartirish
# print(type(lang2))
# birnima = []
# input1 = input("birinchi: ")
# input2 = input("ikkinchi: ")
# input3 = input("uchinchi: ")
# birnima.append(input1)
# birnima.append(input2)
# birnima.append(input3)

# for bir in birnima:
#     print(bir)

# notebook = {
#     'nomi':'lenovo',
#     'xotirasi':'1tr',
#     'ssd':256,
#     'ram':'4gb'
# }
# sor = 'salom'
# # print(sor.lower())
# print(notebook['nomi'].lower())



#  lug'atlar


# notebok = {

# }

# inp1 = input("Notebook nomini kiriting: ")
# inp2 = input("Notebook rangini kiriting: ")
# inp3 = input("Notebook hotirasini kiriting: ")

# notebok['nomi'] = inp1
# notebok['rangi'] = inp2
# notebok['hotirasi'] = inp3

# for i,e in notebok.items(): items hammasini qavislar ichida olish
#     print(i, ' : ', e)

# print(notebok)


#  while lar va ro'yhatlar 

# cars = []
# amal = True


# while amal:
#     print("Agar dasturdan chiqishni hohlasangiz 'chiqish' deb yozing!" )
#     text = input("nomni kiriting: ")
#     son = input("sonini kiriting: ")
#     lugat = {

#     }
#     lugat['nomi'] = text 
#     lugat['soni'] = son
#     if text == 'chiqish' and son == 'chiqish':
#         amal = False
#         print(f"Ro'yhat uzunligi: {len(cars)}")
#         print(f"Ro'yhat: {cars}")
#         for i,e in lugat.items():
#             lugat = {

#             }
#             lugat['nomi'] = text 
#             lugat['soni'] = son
#             print(i, ' : ', e)
#             cars.append(text)
           
#     else:
#         for i,e in lugat.items():
#             lugat = {

#             }
#             lugat['nomi'] = text 
#             lugat['soni'] = son
#             print(i, ' : ', e)
#             cars.append(text)
#             cars.append(son)
#         print(cars)
#         print("""


#         """)



#  funksiyalar 


# def car(**son):
#     print(1,2,3,4,5,6)

# car()


# def car(**mal):     kwargs
#     return f"Mashina nomi: {mal['nomi']}; Narxi: {mal['narxi']}"

# tayyor = car(nomi='malibu',narxi=12345)
# print(tayyor) 
# izoh bitta yulduzcha hohlagancha nom kiritish ikkta yulduzcha hohlagancha kiritilgan nomga kalit so'zi yozib qo'shish


# Modulashtirish yani kodni kamaytirish boshqa fayl ochib
#  yangi faylga funksiya yozib import fayl nomi deb chaqirib ishlatib ketiladi
#  ishlashi
#  ozgaruvchi nom = funksiya nomi(kalit soz va qiymati) 






# mashinalar = []
# amal = True

# while amal:
#     print("Mashinlar ro'yhati sayitimizga xush kelibsiz!")
#     inp_kompaniya = input("Kompaniya nomini kiriting: ")
#     inp_model = input("Mashina modelini kiriting: ")
#     inp_yili = input("Mashina yilini kiriting: ")
#     inp_rangi = input("Mashina rangini kiriting: ")
#     inp_narxi = input("Mashina narxini kiriting: ")
#     print("""

#     """)
#     yana = input("Yana mashina qo'shishni xohlaysizmi (yes,no): ")
#     def auto_info(kompaniya, modeli, yili, rangi, narxi=None):
#         auto = {
#             'kompaniya':kompaniya,
#             'modeli':modeli,
#             'yili':yili,
#             'rangi':rangi,
#             'narxi':narxi
#         }
#         auto["kompaniya"] = inp_kompaniya
#         auto["modeli"]= inp_model
#         auto["narxi"]= inp_narxi
#         auto["rangi"]= inp_rangi
#         auto["yili"]= inp_yili
#         mashinalar.append(auto)
#     auto_info(inp_kompaniya,inp_model,inp_yili,inp_rangi,inp_narxi)
#     if yana == "no":
#         break

# print("Sizning mashinalaringiz ro'yhati!")
# for mash in mashinalar:
#     print(mash)


#  git hubdan foydalanish haqida malumotlar
# birinchi orinda git ilovasini yuklaymiz 
# Git bush dasturidan royhatdan otamiz royhatdan otishni githowto sayitidan ko'rishimiz mumkin
#  Ro'yhatdan otgan ozimizning fayilimizga kirib terminalni ochamiz 
# git init buyurig'i biz uchun mahalliy git omborini sozlaydi
# git add fayl nomini yozishimiz mumkun yoki nuqta hammasini qo'shish degani bu gitga qoshish uchun ishlatiladi
# git commit -m yozamiz bu bizga hamma narsani yeg'ib yani qutiga solib tayyorlab beradi
# git status qilib tasdiqlash
# va git hubga kirib yangi repazitoriya qo'shish bo'limiga kirib nom yozish
# 