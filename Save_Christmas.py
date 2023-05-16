import mmap, os
from pathlib import Path
from tqdm import tqdm
import re
import random
import time
import countryinfo as ci
import pycountry_convert as pc
import csv
start = time.time()
progress=0




file="../Save_The_Christmas_Lab/LETTERSV222.txt"
class Copil:
    next_id = 0
    def __init__(self, name, pcolor, cadouri):
        self.id = Copil.next_id
        Copil.next_id += 1
        self.name = name
        self.pcolor = pcolor
        self.cadouri = cadouri
        self.adresa = ''
    def get_name_cadouri(self):
        v = []
        for cadou in self.cadouri:
            v.append(cadou.obj)
        return v
class Gift:
    def __init__(self, obj, quantity, adjectives):
        self.obj = obj
        self.quantity = quantity
        self.time=0
        self.adjectives = adjectives
        self.UID = id
    def add_time_toy(self,time_toy):
        self.time= self.time+time_toy

colordict = {}


electronics = {'huawei', 'iphone', 'xiaomi', 'samsung', 'nintendo', 'xbox', 'smartphone', 'console', 'phone', 'tablet',
               'oral-b', 'amd', 'nvidia', 'computer', 'laptop', 'tv', 'monitor', 'keyboard', 'microphone', 'headphones',
               'camera', 'electronic', 'kindle', 'smart', 'robot', 'earphones', 'buds','drone','dryer',"scooter","printer"}
food = {'cheese', 'candy', 'fruit', 'chocolate', 'wafers','burger','pie',"jellies"}
textiles = {'pants', 'shirt', 't-shirt', 'dress', 'shorts', 'sandals', 'shoes', 'stiletto', 'wig', 'scarf', 'backpack',
            'handbag', 'pillow', 'blanket', 'slippers', 'hoodie', 'hat', 'sweater', 'jeans', 'plush', 'nike', 'dior',
            'burlon', 'balenciaga', 'adidas', 'versace', 'jordan', 'prada', 'gucci', 'kors', 'chanel', 'lv', 'moschino',
            'zara', 'reserved', 'skirt','sweater', 'boots', 'hat','underwear','adidas','jumbo','skirt','jacket',
            'Nike','Valentino', 'art','bag','belt', 'socks', 'Moschino','roller skates'}
paper = {'poster', 'book', 'giftcard'}
 
time_common_toys={'huawei':38.35,"jellies":3,'burger':4,"pie":20, 'iphone':49.42, 'xiaomi':33.25, 'samsung':53.65, 'nintendo':65.37, 'xbox':85.28, 'smartphone':31.87, 'console':78.63, 'phone':30.23, 'tablet':41.56,
               'oral-b':12.40, 'amd':37.79, 'nvidia':34.53, 'computer':98.99, 'laptop':113.43, 'tv':57.55, 'monitor':50.36, 'keyboard':23.44, 'microphone':18.76, 'headphones':27.77,
               'camera':50.36, 'electronic':20.20, 'kindle':39.52, 'smart':26.49, 'robot':279.96, 'earphones':16.40, 'buds':23.63,'drone':53.12,'dryer':11.32,"scooter":65.25,"printer":32.31,
               
               'cheese':30.12, 'candy':15.23, 'fruit':3.53, 'chocolate':25.11, 'wafers':9.83,

               'pants':10.23, 'shirt':12.20, 't-shirt':7.03, 'dress':18.34, 'shorts':8.80, 'sandals':13.25, 'shoes':20.97, 'stiletto':21.59, 'wig':13.40, 'scarf':4.20, 'backpack':21.89,
               'handbag':19.08, 'pillow':8.28, 'blanket':7.54, 'slippers':5.84, 'hoodie':16.87, 'hat':9.12, 'sweater':15.05, 'jeans':11.13, 'plush':15.67, 'nike':23.24, 'dior':20.38,
               'burlon':9.24, 'balenciaga':28.30, 'adidas':21.07, 'versace':25.26, 'jordan':24.20, 'prada':17.74, 'gucci':10.43, 'kors':18.27, 'chanel':20.76, 'lv':5.52, 'moschino':12.36,
                'zara':16.95, 'reserved':17.99, 'skirt':8.09,

                "skateboard":6.23,"skate":6.23,"doll":16.23,"bike":23.34,"bicycle":23.34,

                'poster':3.13, 'book':10.65, 'giftcard':1.84}
surface_common_toys = {'huawei': 0.00381,"jellies":0.00080,'burger':0.00123,"pie":0.00213,'iphone': 0.00373, 'xiaomi': 0.00397, 'samsung': 0.00365, 'nintendo': 0.00865,
                              'xbox': 0.01165, 'smartphone': 0.00365, 'console': 0.00765, 'phone': 0.00373, 'tablet': 0.00965,
                              'oral-b': 0.0012, 'amd': 0.0166, 'nvidia': 0.08887, 'computer': 0.02654, 'laptop': 0.0954,
                              'tv': 0.02654,'drone':0.01143,'dryer':0.0065,"scooter":0.02353,"printer":0.01923,
                              'monitor': 0.02654, 'keyboard': 0.01801, 'microphone': 0.00373, 'headphones': 0.00473,
                              'camera': 0.00654, 'electronic': 0.00054, 'kindle': 0.02634, 'smart': 0.03232, 'robot': 0.10234,
                              'earphones': 0.0032, 'buds': 0.0023,

                              'cheese': 0.0666, 'candy': 0.0666, 'fruit': 0.0666, 'chocolate': 0.08888, 'wafers': 0.00473,

                              'pants': 0.03602, 'shirt': 0.02602, 't-shirt': 0.03602, 'dress': 0.02602, 'shorts': 0.00432,
                              'sandals': 0.0156,
                              'shoes': 0.00902, 'stiletto': 0.00402, 'wig': 0.00402, 'scarf': 0.01002, 'backpack': 0.0456,
                              'handbag': 0.03602, 'pillow': 0.03601, 'blanket': 0.0235, 'slippers': 0.00502, 'hoodie': 0.0834,
                              'hat': 0.0332,
                              'sweater': 0.06344, 'jeans': 0.03602, 'plush': 0.01523, 'nike': 0.00902, 'dior': 0.00662,
                              'burlon': 0.03601, 'balenciaga': 0.02602, 'adidas': 0.0390, 'versace': 0.0390, 'jordan': 0.03601,
                              'prada': 0.01274, 'gucci': 0.06661, 'kors': 0.03602, 'chanel': 0.0390, 'lv': 0.0130,
                              'moschino':0.01901,
                              'zara': 0.03602, 'reserved': 0.02202, 'skirt': 0.03602,

                              "skateboard": 0.06602, "skate": 0.03602, "doll": 0.00360, "bike": 0.70300, "bicycle": 0.80300,

                              'poster': 1, 'book': 0.05654, 'giftcard': 0.00052}
surface_common_toys_list=list(surface_common_toys.keys())








class Materials:
    #liters 
    def __init__(self):
        self.paint=0
    def add_total_paint(self,liters):
        self.paint=self.paint+liters
    def get_total_paint(self):
        return(self.paint)
    #quantities used in g
    quantities = {
                
                'plastic': 0,
                'glass': 0,
                'textile' : 0,
                'iron' : 0,
                'aluminium' : 0,
                'copper' : 0,
                'gold' : 0,
                'silver' : 0,
                'wood' : 0,
                'porcelain' : 0,
                'rubber' : 0,
                'paper' : 0,
                'groceries' : 0
                }
    #speed in kg/hr (production time BOOOOOOOY u stupid production boyyy)
    speed = {
        'plastic': 72000000,
        'glass': 6833333,
        'textile' : 496564,
        'iron' : 4333333,
        'aluminium' : 33500,
        'copper' : 2833333,
        'gold' : 408.3,
        'silver' : 2566,
        'wood' : 78869,
        'porcelain' : 316666,
        'rubber' : 3833333,
        'paper' : 84500,
        'groceries' : 1
        }

    #total time to produce each material
    time = {
        'plastic': 0,
        'glass': 0,
        'textile' : 0,
        'iron' : 0,
        'aluminium' : 0,
        'copper' : 0,
        'gold' : 0,
        'silver' : 0,
        'wood' : 0,
        'porcelain' : 0,
        'rubber' : 0,
        'paper' : 0,
        'groceries' : 0
        }

    def get_mat_qtt(self, material : str):
        return self.quantities[material]

    def get_mat_speed(self, material : str):
        return self.speed[material]

    def add_mat(self, material : str, qtt):
        self.quantities[material] += qtt

    def add_time(self, material : str, add_time):
        self.time[material] += add_time

    def get_mat_time(self, material : str):
        return self.time[material]


    def __getitem__(self, material : str): #handles the [] operator
        qtt = self.quantities[material]
        time = self.speed[material]
        return (qtt, time)
MatL = Materials()
class Time():
    def __init__(self):
        self.time_material=0
        self.time_individual_toy=0
        self.time_paint=0
    def add_individual_toy_time(self,time):
        self.time_individual_toy=self.time_individual_toy+time
    def add_total_paint_time(self,time):
        self.time_paint=self.time_paint+time
    def get_total_paint_time(self):
        return self.time_paint
    def add_total_material_time(self,time):
        self.time_material=self.time_material+time
    def get_total_time(self):
        return self.time_individual_toy+self.time_material+self.time_paint
totalTime=Time()
total_time=0
def paint_qtt(surface,pcolor):
    if pcolor not in list(colordict) and pcolor!="":
        colordict[pcolor] = 0
        colordict[pcolor]=colordict[pcolor]+ surface #1 L of paint ==> 6m^2
        return
    elif pcolor in list(colordict):
        colordict[pcolor]=colordict[pcolor]+ surface
        return
    elif pcolor=="":
        color_paint=color()
        if color_paint in list(colordict):
            colordict[color_paint]=colordict[color_paint]+ surface
            return
        else:
            colordict[color_paint]=0
            colordict[color_paint]=colordict[color_paint]+ surface
            return

def color():
    colors = [
        "blue","red","green",
        "pink","yellow","white",
        "orange","brown","purple",
        "gray","silver","gold",
        "kaki","indigo","lime",
        "cyan","azure","olive",
        "aqua","black","emerald"
    ]
    index = random.randrange(0,20)
    return (colors[index])



def qtt(gift,pcolor):
    stop=False
    gift=re.split(" ", gift)
    for G in gift:
        G=G.lower()
        if G in surface_common_toys_list:
            stop=True
            paint_qtt(surface_common_toys[G]/6,pcolor)     
        if stop==True:
            stop=False
            break
        else: 
            paint_qtt(float("{0:.5f}".format(random.random())),pcolor)
def verificare_materiale(MalumaLaurentiu): #Trebuie modificata (mai putine functii random)
    
#MalumaLaurentiu.gifts.append(Gift("zee beez zing toy", "1", "khaki", "1234AV"))
#MalumaLaurentiu.gifts.append(Gift("Huawei Media Pad T2 7", "1", "", "1234AV"))


    for i in MalumaLaurentiu.cadouri:                  #Xiaomi mi a 2/ a Xiaomi mi a 2  phone
        declassified = ""
        toy = re.split(" ", i.obj)
        for j in toy:
            if(j=="a" or j=="an") or (j>="0" and j<="9") or j=="of":
                continue
            try:
                x=j[0].lower()+ j[1:]
            except:
                continue
            declassified=""
            if x in electronics:
                declassified = x
                #qtt = random.randrange(10, 18)
                qtt = 1
                qtt += i.quantity
                MatL.add_mat('copper', qtt)
                qtt = 5
                qtt += i.quantity
                MatL.add_mat('gold', qtt)
                qtt = 4
                qtt += i.quantity
                MatL.add_mat('silver', qtt)
                #qtt = random.randrange(100, 500)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('plastic', qtt)            
                #qtt = random.randrange(10, 50)
                qtt = 1
                qtt += i.quantity
                MatL.add_mat('iron', qtt)
                break
            elif x in food:
                declassified = x
                #qtt = random.randrange(500, 2000)
                qtt = 3
                qtt += i.quantity
                MatL.add_mat('groceries', qtt)
                break
            elif x in textiles:
                declassified = x
                #qtt = random.randrange(250, 1000)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('textile', qtt)
                break
            elif x in paper:
                declassified = x
                #qtt = random.randrange(25, 250)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('paper', qtt)            
                break
            elif x == 'bike' or x == 'bicycle':
                declassified = x
                qtt = 1
                qtt += i.quantity
                MatL.add_mat('aluminium', qtt)
                qtt = 3
                qtt += i.quantity
                MatL.add_mat('rubber', qtt)
                #qtt = random.randrange(250, 500)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('textile', qtt)
                break
            elif x == 'doll':
                declassified = x
                #qtt = random.randrange(10, 20)
                qtt = 4
                qtt += i.quantity
                MatL.add_mat('textile', qtt)
                #qtt = random.randrange(100, 250)
                qtt = 1
                qtt += i.quantity
                MatL.add_mat('plastic', qtt)
                break
            elif x == 'skateboard' or x == 'skate':
                declassified = x
                #qtt = random.randrange(450, 900)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('wood', qtt)
                qtt = 3
                qtt += i.quantity
                MatL.add_mat('iron', qtt)
                qtt = 2
                qtt += i.quantity
                MatL.add_mat('rubber', qtt)
                break
        if declassified!="":
            try:
                i.add_time_toy(time_common_toys[declassified]*float(i.quantity))
            except:
                i.add_time_toy(16)
            try:
                totalTime.add_individual_toy_time(time_common_toys[declassified]*float(i.quantity))
            except:
                totalTime.add_individual_toy_time(16)

        if declassified == "":
            adj = re.split(" ", i.adjectives)
            for j in adj:
                sum = 0
                for k in j:
                    sum += ord(k)
                key = sum % 8
                # print("ZOING DOING BOING")
                # print(j)
                if key == 0:
                    declassified = 1
                    #qtt = random.randrange(50, 500)
                    qtt = 3
                    qtt += i.quantity
                    MatL.add_mat('copper', qtt)
                    break
                elif key == 1:
                    declassified = 1
                    #qtt = random.randrange(5, 200)
                    qtt = 3
                    qtt += i.quantity
                    MatL.add_mat('gold', qtt)
                    break
                elif key == 2:
                    declassified = 1
                    #qtt = random.randrange(5, 300)
                    qtt = 2
                    qtt += i.quantity
                    MatL.add_mat('silver', qtt)
                    break
                elif key == 3:
                    declassified = 1
                    #qtt = random.randrange(100, 500)
                    qtt = 3
                    qtt += i.quantity
                    MatL.add_mat('aluminium', qtt)
                    break
                elif key == 4:
                    declassified = 1
                    #qtt = random.randrange(50, 500)
                    qtt = 2
                    qtt += i.quantity
                    MatL.add_mat('glass', qtt)
                    break
                elif key == 5:
                    declassified = 1
                    #qtt = random.randrange(50, 500)
                    qtt = 2
                    qtt += i.quantity
                    MatL.add_mat('porcelain', qtt)
                    break
                elif key == 6:
                    declassified = 1
                    #qtt = random.randrange(50, 500)
                    qtt = 4
                    qtt += i.quantity
                    MatL.add_mat('rubber', qtt)
                    break
                elif key == 7:
                    declassified = 1
                    #qtt = random.randrange(200, 1000)
                    qtt = 2
                    qtt += i.quantity
                    MatL.add_mat('wood', qtt)
                    break

        if declassified == "":
            #qtt = random.randrange(200, 600)
            qtt = 1
            qtt += i.quantity
            MatL.add_mat('plastic', qtt)
            #var=random.randrange(6, 70)
            var = 6 + 2
            i.add_time_toy= var*i.quantity
def timp_total_vopsire():
    for i in colordict:
        MatL.add_total_paint(colordict[i])
def calcul_timp_total():
    global total_time
    M_Names = ['plastic','glass','textile','iron','aluminium','copper', 'gold','silver', 'wood', 'porcelain','rubber', 'paper','groceries']
    for material in M_Names:
        buffer = MatL[material]
        #in hrs (t_buffer)
        t_buffer = MatL[material][0] // 1000 // MatL[material][1]
        MatL.add_time(material, t_buffer)
        print(f"The production time of {material} is: {MatL.get_mat_time(material)}")
        try:
            total_time += int(t_buffer)
        except:
            total_time += 1
    #minutes (totalTime)
    totalTime.add_total_material_time(total_time)
    #print(totalTime.get_total_time())
###################################################Productie+Achizitii############################################
def impachetare(kid):
    for i in kid.cadouri:
        setattr(i, "ambalaj", kid.pcolor)
###################################################Impachetare####################################################
###Liste Tari Ordonate si Dictionare
LCO=['Afghanistan', 'Albania', 'Algeria', 'American Samoa', 'American Samoa', 'Andorra', 'Angola', 'Anguilla',
     'Antarctica (the territory South of 60 deg S)', 'Antigua and Barbuda', 'Argentina', 'Armenia', 'Australia',
     'Austria', 'Azerbaijan', 'Bahamas', 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', 'Belize', 'Benin',
     'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', 'Botswana', 'Bouvet Island (Bouvetoya)', 'Brazil',
     'British Indian Ocean Territory (Chagos Archipelago)', 'British Virgin Islands', 'British Virgin Islands',
     'Brunei Darussalam', 'Bulgaria', 'Burkina Faso', 'Burundi', 'Cambodia', 'Cameroon', 'Canada', 'Cape Verde',
     'Cayman Islands', 'Central African Republic', 'Chad', 'Chile', 'China', 'Christmas Island',
     'Cocos (Keeling) Islands', 'Colombia', 'Comoros', 'Congo', 'Cook Islands', 'Costa Rica', "Cote d'Ivoire",
     'Croatia', 'Cuba', 'Cyprus', 'Czech Republic', 'Denmark', 'Djibouti', 'Dominica', 'Dominican Republic', 'Ecuador',
     'Egypt', 'El Salvador', 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Ethiopia', 'Falkland Islands (Malvinas)',
     'Faroe Islands', 'Federated States of Micronesia', 'Fiji', 'Finland', 'France', 'French Guiana',
     'French Polynesia', 'French Southern Territories', 'Gabon', 'Gambia', 'Georgia', 'Germany', 'Ghana', 'Greece',
     'Greenland', 'Grenada', 'Guadeloupe', 'Guatemala', 'Guernsey', 'Guinea', 'Guinea-Bissau', 'Guyana', 'Haiti',
     'Heard Island and McDonald Islands', 'Holy See (Vatican City)', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland',
     'India', 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Isle of Man', 'Israel', 'Italy', 'Jamaica', 'Japan', 'Jordan',
     'Kazakhstan', 'Kenya', 'Kiribati', 'Kuwait', 'Kyrgyz Republic', "Lao People's Democratic Republic", 'Latvia',
     'Lebanon', 'Lesotho', 'Liberia', 'Libyan Arab Jamahiriya', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macao',
     'Madagascar', 'Malawi', 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius',
     'Mayotte', 'Mexico', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Montserrat', 'Morocco', 'Mozambique',
     'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'Netherlands Antilles', 'Netherlands Antilles',
     'New Caledonia', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', 'Niue', 'Norfolk Island', 'North Korea', 'Norway',
     'Oman', 'Pakistan', 'Palau', 'Palestinian Territory', 'Panama', 'Papua New Guinea', 'Paraguay', 'Peru',
     'Philippines', 'Pitcairn Islands', 'Poland', 'Portugal', 'Puerto Rico', 'Qatar', 'Reunion', 'Romania',
     'Russian Federation', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Lucia',
     'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome and Principe', 'Saudi Arabia', 'Senegal',
     'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Slovakia (Slovak Republic)', 'Slovenia', 'Solomon Islands',
     'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', 'Sudan', 'Suriname',
     'Svalbard & Jan Mayen Islands', 'Swaziland', 'Sweden', 'Switzerland', 'Syrian Arab Republic', 'Taiwan',
     'Tajikistan', 'Tanzania', 'Thailand', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey',
     'Turkmenistan', 'Turks and Caicos Islands', 'Tuvalu', 'Uganda', 'Ukraine', 'United Arab Emirates',
     'United Kingdom', 'United States', 'United States Minor Outlying Islands', 'United States Virgin Islands',
     'Uruguay', 'Uzbekistan', 'Vanuatu', 'Venezuela', 'Vietnam', 'Western Sahara', 'Yemen', 'Zambia', 'Zimbabwe']

LCO1 = ["Russian Federation", "New Zealand", "Fiji", "Tuvalu", "Marshall Islands", "Vanuatu", "Solomon Islands",
        "Australia", "Nauru", "Federated States of Micronesia", "Papua New Guinea", "Japan", "Indonesia", "China",
        "Palau", "South Korea", "North Korea", "Philippines", "East Timor", "Taiwan", "Mongolia", "Malaysia",
        "Brunei Darussalam", "Hong Kong", "Macau", "Vietnam", "Cambodia", "Laos", "Thailand", "Singapore", "Myanmar",
        "Bouvet Island (Bouvetoya)", "Palestinian Territory", "India", "Bangladesh", "Bhutan", "Nepal", "Kazakhstan",
        "Sri Lanka", "Kyrgyz Republic", "Pakistan", "Tajikistan", "Afghanistan", "Maldives", "Uzbekistan",
        "British Indian Ocean Territory (Chagos Archipelago)", "French Southern and Antarctic Lands", "Antarctica",
        "Turkmenistan", "Mauritius", "Iran", "Oman", "United Arab Emirates", "Seychelles", "Saudi Arabia", "Yemen",
        "Qatar", "Somalia", "Bahrain", "Madagascar", "Azerbaijan", "Kuwait", "Iraq", "American Samoa", "Ethiopia",
        "Georgia", "Armenia", "Turkey", "Comoros", "Djibouti", "Eritrea", "Syrian Arab Republic", "Kenya", "Mozambique",
        "Tanzania", "Ukraine", "Jordan", "Sudan", "South Africa", "Lebanon", "Malawi", "Egypt", "South Sudan", "Israel",
        "Uganda", "Cyprus", "Norway", "Zimbabwe", "Zambia", "Belarus", "Swaziland", "Finland",
        "Democratic Republic of the Congo", "Congo", "Rwanda", "Burundi", "Moldova", "Romania", "Greece", "Lesotho",
        "Botswana", "Bulgaria", "Latvia", "Estonia", "Central African Republic", "Lithuania", "Namibia", "Libya",
        "Sweden", "Poland", "Angola", "Chad", "Serbia", "Hungary", "Slovakia", "Albania", "Montenegro",
        "Bosnia and Herzegovina", "Croatia", "Czech Republic", "Republic of the Congo", "Italy", "France", "Austria",
        "Slovenia", "Cameroon", "Niger", "Denmark", "Germany", "Malta", "Gabon", "Nigeria", "San Marino",
        "Vatican City", "Algeria", "Tunisia", "Equatorial Guinea", "Switzerland", "Liechtenstein", "Monaco",
        "Sao Tome and Principe", "Netherlands", "Luxembourg", "Belgium", "Spain", "Mali", "Benin", "Burkina Faso",
        "Andorra", "Togo", "Ghana", "Morocco", "Côte d'Ivoire", "Mauritania", "United Kingdom", "Ireland", "Portugal",
        "Faroe Islands", "Saint Lucia", "Liberia", "Guinea", "Western Sahara", "Mayotte",
        "United States Minor Outlying Islands", "Guernsey", "Netherlands Antilles", "Sierra Leone", "Senegal",
        "Greenland", "Iceland", "Guinea-Bissau", "Gambia", "Cape Verde", "Brazil", "Canada", "Uruguay", "Argentina",
        "Suriname", "Paraguay", "Guyana", "Bolivia", "Barbados", "Venezuela", "Trinidad and Tobago",
        "Saint Vincent and the Grenadines", "Saint Lucia", "Dominica", "Grenada", "Antigua and Barbuda",
        "Saint Kitts and Nevis", "United States", "Puerto Rico", "Chile", "Colombia", "Dominican Republic", "Peru",
        "Haiti", "Bahamas", "Cuba", "Ecuador", "Jamaica", "Panama", "Costa Rica", "Nicaragua", "Honduras", "Mexico",
        "Belize", "El Salvador", "Guatemala", "Kiribati", "Samoa", "Tonga", "Timor-Leste", "Norfolk Island",
        "Christmas Island", "Cocos (Keeling) Islands", "Falkland Islands (Malvinas)", "British Virgin Islands",
        "French Polynesia", "Cook Islands", "Niue", "Reunion", "New Caledonia", "French Guiana", "Anguilla",
        "Isle of Man"]

Tz={'New Zealand': 'GMT+12', 'Fiji': 'GMT+12', 'Tuvalu': 'GMT+12', 'Marshall Islands': 'GMT+12', 'Vanuatu': 'GMT+11',
     'Solomon Islands': 'GMT+11', 'Australia': 'GMT+11', 'Nauru': 'GMT+12', 'Papua New Guinea': 'GMT+11',
     'Japan': 'GMT+09', 'Indonesia': 'GMT+09', 'China': 'GMT+08', 'Palau': 'GMT+09', 'South Korea': 'GMT+09',
     'North Korea': 'GMT+09', 'Philippines': 'GMT+08', 'Taiwan': 'GMT+08', 'Mongolia': 'GMT+08', 'Malaysia': 'GMT+08',
     'Hong Kong': 'GMT+08', 'Vietnam': 'GMT+07', 'Cambodia': 'GMT+07', "Lao People's Democratic Republic": 'GMT+07',
     'Thailand': 'GMT+07', 'Singapore': 'GMT+08', 'British Virgin Islands': 'GMT-04', 'Myanmar': 'GMT+06',
     'India': 'GMT+05', 'Bangladesh': 'GMT+06', 'Bhutan': 'GMT+06', 'Nepal': 'GMT+05', 'Kazakhstan': 'GMT+06',
     'Sri Lanka': 'GMT+05', 'Kyrgyz Republic': 'GMT+06', 'Pakistan': 'GMT+05', 'Tajikistan': 'GMT+05',
     'Afghanistan': 'GMT+04', 'Maldives': 'GMT+05', 'Uzbekistan': 'GMT+05', 'Czech Republic': 'GMT+02',
     'United Kingdom': 'GMT', 'Turkmenistan': 'GMT+05', 'Mauritius': 'GMT+04', 'Iran': 'GMT+04', 'Oman': 'GMT+04',
     'United Arab Emirates': 'GMT+04', 'Seychelles': 'GMT+04', 'France': 'GMT+02', 'Saudi Arabia': 'GMT+03',
     'Yemen': 'GMT+03', 'Qatar': 'GMT+03', 'Somalia': 'GMT+03', 'Bahrain': 'GMT+03', 'Madagascar': 'GMT+03',
     'Azerbaijan': 'GMT+04', 'Kuwait': 'GMT+03', 'Iraq': 'GMT+03', 'Ethiopia': 'GMT+03', 'Georgia': 'GMT+04',
     'Armenia': 'GMT+04', 'Turkey': 'GMT+03', 'Comoros': 'GMT+03', 'Djibouti': 'GMT+03', 'Eritrea': 'GMT+03',
     'Kenya': 'GMT+03', 'Mozambique': 'GMT+02', 'Tanzania': 'GMT+03', 'Ukraine': 'GMT+03', 'Jordan': 'GMT+03',
     'Sudan': 'GMT+03', 'South Africa': 'GMT+02', 'Lebanon': 'GMT+03', 'Malawi': 'GMT+02', 'Egypt': 'GMT+02',
     'Israel': 'GMT+03', 'Uganda': 'GMT+03', 'Cyprus': 'GMT+03', 'Norway': 'GMT+02', 'Zimbabwe': 'GMT+02',
     'Zambia': 'GMT+02', 'Belarus': 'GMT+03', 'Swaziland': 'GMT+02', 'Finland': 'GMT+03', 'Rwanda': 'GMT+02',
     'Burundi': 'GMT+02', 'Moldova': 'GMT+03', 'Romania': 'GMT+02', 'Greece': 'GMT+03', 'Botswana': 'GMT+02',
     'Bulgaria': 'GMT+03', 'Latvia': 'GMT+03', 'Estonia': 'GMT+03', 'Central African Republic': 'GMT+01',
     'Lithuania': 'GMT+03', 'Namibia': 'GMT+02', 'Sweden': 'GMT+02', 'Poland': 'GMT+02', 'Angola': 'GMT+01',
     'Chad': 'GMT+01', 'Serbia': 'GMT+02', 'Hungary': 'GMT+02', 'Albania': 'GMT+02', 'Montenegro': 'GMT+02',
     'Bosnia and Herzegovina': 'GMT+02', 'Croatia': 'GMT+02', 'Italy': 'GMT+02', 'Austria': 'GMT+02',
     'Slovenia': 'GMT+02', 'Cameroon': 'GMT+01', 'Niger': 'GMT+01', 'Germany': 'GMT+02', 'Malta': 'GMT+02',
     'Gabon': 'GMT+01', 'Nigeria': 'GMT+01', 'San Marino': 'GMT+02', 'Holy See (Vatican City)': 'GMT+02',
     'Algeria': 'GMT+01', 'Tunisia': 'GMT+01', 'Equatorial Guinea': 'GMT+01', 'Switzerland': 'GMT+02',
     'Liechtenstein': 'GMT+02', 'Monaco': 'GMT+02', 'Sao Tome and Principe': 'GMT', 'Netherlands': 'GMT+02',
     'Luxembourg': 'GMT+02', 'Belgium': 'GMT+02', 'Mali': 'GMT', 'Benin': 'GMT+01', 'Burkina Faso': 'GMT',
     'Andorra': 'GMT+02', 'Togo': 'GMT', 'Ghana': 'GMT', 'Morocco': 'GMT+01', 'Mauritania': 'GMT', 'Ireland': 'GMT',
     'Portugal': 'GMT', 'Faroe Islands': 'GMT+01', 'Saint Lucia': 'GMT-04', 'Liberia': 'GMT', 'Guinea': 'GMT',
     'Sierra Leone': 'GMT', 'Senegal': 'GMT', 'Greenland': 'GMT', 'Iceland': 'GMT', 'Guinea-Bissau': 'GMT',
     'Gambia': 'GMT', 'Brazil': 'GMT-03', 'Uruguay': 'GMT-03', 'Argentina': 'GMT-03', 'Suriname': 'GMT-03',
     'Paraguay': 'GMT-03', 'Guyana': 'GMT-04', 'Bolivia': 'GMT-04', 'Barbados': 'GMT-04', 'Venezuela': 'GMT-04',
     'Trinidad and Tobago': 'GMT-04', 'Saint Vincent and the Grenadines': 'GMT-04', 'Dominica': 'GMT-04',
     'Grenada': 'GMT-04', 'Antigua and Barbuda': 'GMT-04', 'Saint Kitts and Nevis': 'GMT-04', 'Puerto Rico': 'GMT-04',
     'Chile': 'GMT-03', 'Colombia': 'GMT-05', 'Dominican Republic': 'GMT-04', 'Peru': 'GMT-05', 'Haiti': 'GMT-04',
     'Bahamas': 'GMT-04', 'Cuba': 'GMT-04', 'Ecuador': 'GMT-05', 'Jamaica': 'GMT-05', 'Panama': 'GMT-05',
     'Costa Rica': 'GMT-06', 'Nicaragua': 'GMT-06', 'Honduras': 'GMT-06', 'Mexico': 'GMT-05', 'Belize': 'GMT-06',
     'El Salvador': 'GMT-06', 'Guatemala': 'GMT-06', 'Kiribati': 'GMT+12', 'Samoa': 'GMT+12', 'Tonga': 'GMT+12',
     'Norfolk Island': 'GMT+11', 'Christmas Island': 'GMT+07', 'Cocos (Keeling) Islands': 'GMT+06',
     'Falkland Islands (Malvinas)': 'GMT-03', 'French Polynesia': 'GMT-09', 'Cook Islands': 'GMT-10', 'Niue': 'GMT-11',
     'Isle of Man': 'GMT'}

finder={'stan': 'Afghanistan', 'ania': 'Albania', 'eria': 'Algeria', 'amoa': 'American Samoa', 'orra': 'Andorra',
     'gola': 'Angola', 'illa': 'Anguilla', 'buda': 'Antigua and Barbuda', 'tina': 'Argentina', 'enia': 'Armenia',
     'alia': 'Australia', 'tria': 'Austria', 'ijan': 'Azerbaijan', 'amas': 'Bahamas', 'rain': 'Bahrain',
     'desh': 'Bangladesh', 'ados': 'Barbados', 'arus': 'Belarus', 'gium': 'Belgium', 'lize': 'Belize', 'enin': 'Benin',
     'utan': 'Bhutan', 'ivia': 'Bolivia', 'vina': 'Bosnia and Herzegovina', 'wana': 'Botswana',
     'oya)': 'Bouvet Island (Bouvetoya)', 'azil': 'Brazil', 'ands': 'British Virgin Islands',
     'slands': 'British Virgin Islands', 'alam': 'Brunei Darussalam', 'aria': 'Bulgaria', 'Faso': 'Burkina Faso',
     'undi': 'Burundi', 'odia': 'Cambodia', 'roon': 'Cameroon', 'nada': 'Canada', 'erde': 'Cape Verde',
     ' Islands': 'Cayman Islands', 'blic': 'Central African Republic', 'Chad': 'Chad', 'hile': 'Chile', 'hina': 'China',
     'land': 'Christmas Island', 'ng) Islands': 'Cocos (Keeling) Islands', 'mbia': 'Colombia', 'oros': 'Comoros',
     'ook Islands': 'Cook Islands', 'Rica': 'Costa Rica', 'atia': 'Croatia', 'Cuba': 'Cuba', 'prus': 'Cyprus',
     'public': 'Czech Republic', 'oire': "Côte d'Ivoire", 'mark': 'Denmark', 'outi': 'Djibouti', 'nica': 'Dominica',
     'Republic': 'Dominican Republic', 'ador': 'Ecuador', 'gypt': 'Egypt', 'lvador': 'El Salvador',
     'inea': 'Equatorial Guinea', 'trea': 'Eritrea', 'onia': 'Estonia', 'opia': 'Ethiopia',
     'nas)': 'Falkland Islands (Malvinas)', 'roe Islands': 'Faroe Islands', 'esia': 'Federated States of Micronesia',
     'Fiji': 'Fiji', 'inland': 'Finland', 'ance': 'France', 'iana': 'French Guiana', 'ynesia': 'French Polynesia',
     'ries': 'French Southern Territories', 'abon': 'Gabon', 'Gambia': 'Gambia', 'rgia': 'Georgia', 'many': 'Germany',
     'hana': 'Ghana', 'eece': 'Greece', 'enland': 'Greenland', 'renada': 'Grenada', 'oupe': 'Guadeloupe',
     'mala': 'Guatemala', 'nsey': 'Guernsey', 'Guinea': 'Guinea', 'ssau': 'Guinea-Bissau', 'yana': 'Guyana',
     'aiti': 'Haiti', 'ald Islands': 'Heard Island and McDonald Islands', 'ity)': 'Holy See (Vatican City)',
     'uras': 'Honduras', 'Kong': 'Hong Kong', 'gary': 'Hungary', 'celand': 'Iceland', 'ndia': 'India',
     'onesia': 'Indonesia', 'Iran': 'Iran', 'Iraq': 'Iraq', 'reland': 'Ireland', ' Man': 'Isle of Man',
     'rael': 'Israel', 'taly': 'Italy', 'aica': 'Jamaica', 'apan': 'Japan', 'rdan': 'Jordan', 'khstan': 'Kazakhstan',
     'enya': 'Kenya', 'bati': 'Kiribati', 'wait': 'Kuwait', 'yz Republic': 'Kyrgyz Republic',
     'ic Republic': "Lao People's Democratic Republic", 'tvia': 'Latvia', 'anon': 'Lebanon', 'otho': 'Lesotho',
     'iberia': 'Liberia', 'riya': 'Libyan Arab Jamahiriya', 'tein': 'Liechtenstein', 'huania': 'Lithuania',
     'ourg': 'Luxembourg', 'acao': 'Macao', 'scar': 'Madagascar', 'lawi': 'Malawi', 'ysia': 'Malaysia',
     'ives': 'Maldives', 'Mali': 'Mali', 'alta': 'Malta', 'all Islands': 'Marshall Islands', 'itania': 'Mauritania',
     'tius': 'Mauritius', 'otte': 'Mayotte', 'xico': 'Mexico', 'dova': 'Moldova', 'naco': 'Monaco', 'olia': 'Mongolia',
     'egro': 'Montenegro', 'rrat': 'Montserrat', 'occo': 'Morocco', 'ique': 'Mozambique', 'nmar': 'Myanmar',
     'ibia': 'Namibia', 'auru': 'Nauru', 'epal': 'Nepal', 'rlands': 'Netherlands', 'lles': 'Netherlands Antilles',
     'edonia': 'New Caledonia', 'ealand': 'New Zealand', 'agua': 'Nicaragua', 'iger': 'Niger', 'igeria': 'Nigeria',
     'Niue': 'Niue', 'Island': 'Norfolk Island', 'orea': 'North Korea', 'rway': 'Norway', 'Oman': 'Oman',
     'kistan': 'Pakistan', 'alau': 'Palau', 'tory': 'Palestinian Territory', 'nama': 'Panama',
     'w Guinea': 'Papua New Guinea', 'guay': 'Paraguay', 'Peru': 'Peru', 'ines': 'Philippines',
     'irn Islands': 'Pitcairn Islands', 'Poland': 'Poland', 'ugal': 'Portugal', 'Rico': 'Puerto Rico', 'atar': 'Qatar',
     'ongo': 'Republic of the Congo', 'nion': 'Reunion', 'omania': 'Romania', 'ssia': 'Russia', 'anda': 'Rwanda',
     'evis': 'Saint Kitts and Nevis', 'ucia': 'Saint Lucia', ' Lucia': 'Saint Lucia',
     'adines': 'Saint Vincent and the Grenadines', 'a': 'Samoa', 'rino': 'San Marino', 'cipe': 'Sao Tome and Principe',
     'abia': 'Saudi Arabia', 'egal': 'Senegal', 'rbia': 'Serbia', 'helles': 'Seychelles', 'eone': 'Sierra Leone',
     'pore': 'Singapore', 'lic)': 'Slovakia (Slovak Republic)', 'ovenia': 'Slovenia', 'mon Islands': 'Solomon Islands',
     'omalia': 'Somalia', 'rica': 'South Africa', ' Korea': 'South Korea', 'udan': 'South Sudan', 'pain': 'Spain',
     'anka': 'Sri Lanka', 'n': 'Sudan', 'name': 'Suriname', 'yen Islands': 'Svalbard & Jan Mayen Islands',
     'ziland': 'Swaziland', 'eden': 'Sweden', 'erland': 'Switzerland', 'ab Republic': 'Syrian Arab Republic',
     'iwan': 'Taiwan', 'jikistan': 'Tajikistan', 'nzania': 'Tanzania', 'ailand': 'Thailand', 'este': 'Timor-Leste',
     'Togo': 'Togo', 'onga': 'Tonga', 'bago': 'Trinidad and Tobago', 'isia': 'Tunisia', 'rkey': 'Turkey',
     'nistan': 'Turkmenistan', 'cos Islands': 'Turks and Caicos Islands', 'valu': 'Tuvalu', 'Uganda': 'Uganda',
     'aine': 'Ukraine', 'ates': 'United Arab Emirates', 'gdom': 'United Kingdom', 'States': 'United States',
     'ing Islands': 'United States Minor Outlying Islands', 'gin Islands': 'United States Virgin Islands',
     'ruguay': 'Uruguay', 'bekistan': 'Uzbekistan', 'uatu': 'Vanuatu', 'uela': 'Venezuela', 'tnam': 'Vietnam',
     'hara': 'Western Sahara', 'emen': 'Yemen', 'Zambia': 'Zambia', 'abwe': 'Zimbabwe'}

ORD_d={'Afghanistan': 0, 'Albania': 1, 'Algeria': 2, 'American Samoa': 3, 'Andorra': 4, 'Angola': 5, 'Anguilla': 6,
     'Antigua and Barbuda': 7, 'Argentina': 8, 'Armenia': 9, 'Australia': 10, 'Austria': 11, 'Azerbaijan': 12,
     'Bahamas': 13, 'Bahrain': 14, 'Bangladesh': 15, 'Barbados': 16, 'Belarus': 17, 'Belgium': 18, 'Belize': 19,
     'Benin': 20, 'Bhutan': 21, 'Bolivia': 22, 'Bosnia and Herzegovina': 23, 'Botswana': 24,
     'Bouvet Island (Bouvetoya)': 25, 'Brazil': 26, 'British Virgin Islands': 28, 'Brunei Darussalam': 29,
     'Bulgaria': 30, 'Burkina Faso': 31, 'Burundi': 32, 'Cambodia': 33, 'Cameroon': 34, 'Canada': 35, 'Cape Verde': 36,
     'Cayman Islands': 37, 'Central African Republic': 38, 'Chad': 39, 'Chile': 40, 'China': 41, 'Christmas Island': 42,
     'Cocos (Keeling) Islands': 43, 'Colombia': 44, 'Comoros': 45, 'Cook Islands': 46, 'Costa Rica': 47, 'Croatia': 48,
     'Cuba': 49, 'Cyprus': 50, 'Czech Republic': 51, "Côte d'Ivoire": 52, 'Denmark': 53, 'Djibouti': 54, 'Dominica': 55,
     'Dominican Republic': 56, 'Ecuador': 57, 'Egypt': 58, 'El Salvador': 59, 'Equatorial Guinea': 60, 'Eritrea': 61,
     'Estonia': 62, 'Ethiopia': 63, 'Falkland Islands (Malvinas)': 64, 'Faroe Islands': 65,
     'Federated States of Micronesia': 66, 'Fiji': 67, 'Finland': 68, 'France': 69, 'French Guiana': 70,
     'French Polynesia': 71, 'French Southern Territories': 72, 'Gabon': 73, 'Gambia': 74, 'Georgia': 75, 'Germany': 76,
     'Ghana': 77, 'Greece': 78, 'Greenland': 79, 'Grenada': 80, 'Guadeloupe': 81, 'Guatemala': 82, 'Guernsey': 83,
     'Guinea': 84, 'Guinea-Bissau': 85, 'Guyana': 86, 'Haiti': 87, 'Heard Island and McDonald Islands': 88,
     'Holy See (Vatican City)': 89, 'Honduras': 90, 'Hong Kong': 91, 'Hungary': 92, 'Iceland': 93, 'India': 94,
     'Indonesia': 95, 'Iran': 96, 'Iraq': 97, 'Ireland': 98, 'Isle of Man': 99, 'Israel': 100, 'Italy': 101,
     'Jamaica': 102, 'Japan': 103, 'Jordan': 104, 'Kazakhstan': 105, 'Kenya': 106, 'Kiribati': 107, 'Kuwait': 108,
     'Kyrgyz Republic': 109, "Lao People's Democratic Republic": 110, 'Latvia': 111, 'Lebanon': 112, 'Lesotho': 113,
     'Liberia': 114, 'Libyan Arab Jamahiriya': 115, 'Liechtenstein': 116, 'Lithuania': 117, 'Luxembourg': 118,
     'Macao': 119, 'Madagascar': 120, 'Malawi': 121, 'Malaysia': 122, 'Maldives': 123, 'Mali': 124, 'Malta': 125,
     'Marshall Islands': 126, 'Mauritania': 127, 'Mauritius': 128, 'Mayotte': 129, 'Mexico': 130, 'Moldova': 131,
     'Monaco': 132, 'Mongolia': 133, 'Montenegro': 134, 'Montserrat': 135, 'Morocco': 136, 'Mozambique': 137,
     'Myanmar': 138, 'Namibia': 139, 'Nauru': 140, 'Nepal': 141, 'Netherlands': 142, 'Netherlands Antilles': 143,
     'New Caledonia': 144, 'New Zealand': 145, 'Nicaragua': 146, 'Niger': 147, 'Nigeria': 148, 'Niue': 149,
     'Norfolk Island': 150, 'North Korea': 151, 'Norway': 152, 'Oman': 153, 'Pakistan': 154, 'Palau': 155,
     'Palestinian Territory': 156, 'Panama': 157, 'Papua New Guinea': 158, 'Paraguay': 159, 'Peru': 160,
     'Philippines': 161, 'Pitcairn Islands': 162, 'Poland': 163, 'Portugal': 164, 'Puerto Rico': 165, 'Qatar': 166,
     'Republic of the Congo': 167, 'Reunion': 168, 'Romania': 169, 'Russian Federation': 170, 'Rwanda': 171,
     'Saint Kitts and Nevis': 172, 'Saint Lucia': 174, 'Saint Vincent and the Grenadines': 175, 'Samoa': 176,
     'San Marino': 177, 'Sao Tome and Principe': 178, 'Saudi Arabia': 179, 'Senegal': 180, 'Serbia': 181,
     'Seychelles': 182, 'Sierra Leone': 183, 'Singapore': 184, 'Slovakia': 185, 'Slovenia': 186, 'Solomon Islands': 187,
     'Somalia': 188, 'South Africa': 189, 'South Korea': 190, 'South Sudan': 191, 'Spain': 192, 'Sri Lanka': 193,
     'Sudan': 194, 'Suriname': 195, 'Svalbard & Jan Mayen Islands': 196, 'Swaziland': 197, 'Sweden': 198,
     'Switzerland': 199, 'Syrian Arab Republic': 200, 'Taiwan': 201, 'Tajikistan': 202, 'Tanzania': 203,
     'Thailand': 204, 'Timor-Leste': 205, 'Togo': 206, 'Tonga': 207, 'Trinidad and Tobago': 208, 'Tunisia': 209,
     'Turkey': 210, 'Turkmenistan': 211, 'Turks and Caicos Islands': 212, 'Tuvalu': 213, 'Uganda': 214, 'Ukraine': 215,
     'United Arab Emirates': 216, 'United Kingdom': 217, 'United States': 218,
     'United States Minor Outlying Islands': 219, 'United States Virgin Islands': 220, 'Uruguay': 221,
     'Uzbekistan': 222, 'Vanuatu': 223, 'Venezuela': 224, 'Vietnam': 225, 'Western Sahara': 226, 'Yemen': 227,
     'Zambia': 228, 'Zimbabwe': 229}

Lo= {'stan': 0, 'ania': 1, 'eria': 2, 'amoa': 3, 'orra': 4, 'gola': 5, 'illa': 6, 'buda': 7, 'tina': 8, 'enia': 9,
     'alia': 10, 'tria': 11, 'ijan': 12, 'amas': 13, 'rain': 14, 'desh': 15, 'ados': 16, 'arus': 17, 'gium': 18,
     'lize': 19, 'enin': 20, 'utan': 21, 'ivia': 22, 'vina': 23, 'wana': 24, 'oya)': 25, 'azil': 26, 'ands': 27,
     'slands': 28, 'alam': 29, 'aria': 30, 'Faso': 31, 'undi': 32, 'odia': 33, 'roon': 34, 'nada': 35, 'erde': 36,
     ' Islands': 37, 'blic': 38, 'Chad': 39, 'hile': 40, 'hina': 41, 'land': 42, 'ng) Islands': 43, 'mbia': 44,
     'oros': 45, 'ook Islands': 46, 'Rica': 47, 'atia': 48, 'Cuba': 49, 'prus': 50, 'public': 51, 'oire': 52,
     'mark': 53, 'outi': 54, 'nica': 55, 'Republic': 56, 'ador': 57, 'gypt': 58, 'lvador': 59, 'inea': 60, 'trea': 61,
     'onia': 62, 'opia': 63, 'nas)': 64, 'roe Islands': 65, 'esia': 66, 'Fiji': 67, 'inland': 68, 'ance': 69,
     'iana': 70, 'ynesia': 71, 'ries': 72, 'abon': 73, 'Gambia': 74, 'rgia': 75, 'many': 76, 'hana': 77, 'eece': 78,
     'enland': 79, 'renada': 80, 'oupe': 81, 'mala': 82, 'nsey': 83, 'Guinea': 84, 'ssau': 85, 'yana': 86, 'aiti': 87,
     'ald Islands': 88, 'ity)': 89, 'uras': 90, 'Kong': 91, 'gary': 92, 'celand': 93, 'ndia': 94, 'onesia': 95,
     'Iran': 96, 'Iraq': 97, 'reland': 98, ' Man': 99, 'rael': 100, 'taly': 101, 'aica': 102, 'apan': 103, 'rdan': 104,
     'khstan': 105, 'enya': 106, 'bati': 107, 'wait': 108, 'yz Republic': 109, 'ic Republic': 110, 'tvia': 111,
     'anon': 112, 'otho': 113, 'iberia': 114, 'riya': 115, 'tein': 116, 'huania': 117, 'ourg': 118, 'acao': 119,
     'scar': 120, 'lawi': 121, 'ysia': 122, 'ives': 123, 'Mali': 124, 'alta': 125, 'all Islands': 126, 'itania': 127,
     'tius': 128, 'otte': 129, 'xico': 130, 'dova': 131, 'naco': 132, 'olia': 133, 'egro': 134, 'rrat': 135,
     'occo': 136, 'ique': 137, 'nmar': 138, 'ibia': 139, 'auru': 140, 'epal': 141, 'rlands': 142, 'lles': 143,
     'edonia': 144, 'ealand': 145, 'agua': 146, 'iger': 147, 'igeria': 148, 'Niue': 149, 'Island': 150, 'orea': 151,
     'rway': 152, 'Oman': 153, 'kistan': 154, 'alau': 155, 'tory': 156, 'nama': 157, 'w Guinea': 158, 'guay': 159,
     'Peru': 160, 'ines': 161, 'irn Islands': 162, 'Poland': 163, 'ugal': 164, 'Rico': 165, 'atar': 166, 'ongo': 167,
     'nion': 168, 'omania': 169, 'ssia': 170, 'anda': 171, 'evis': 172, 'ucia': 173, ' Lucia': 174, 'adines': 175,
     'a': 176, 'rino': 177, 'cipe': 178, 'abia': 179, 'egal': 180, 'rbia': 181, 'helles': 182, 'eone': 183, 'pore': 184,
     'akia': 185, 'ovenia': 186, 'mon Islands': 187, 'omalia': 188, 'rica': 189, ' Korea': 190, 'udan': 191,
     'pain': 192, 'anka': 193, 'n': 194, 'name': 195, 'yen Islands': 196, 'ziland': 197, 'eden': 198, 'erland': 199,
     'ab Republic': 200, 'iwan': 201, 'jikistan': 202, 'nzania': 203, 'ailand': 204, 'este': 205, 'Togo': 206,
     'onga': 207, 'bago': 208, 'isia': 209, 'rkey': 210, 'nistan': 211, 'cos Islands': 212, 'valu': 213, 'Uganda': 214,
     'aine': 215, 'ates': 216, 'gdom': 217, 'States': 218, 'ing Islands': 219, 'gin Islands': 220, 'ruguay': 221,
     'bekistan': 222, 'uatu': 223, 'uela': 224, 'tnam': 225, 'hara': 226, 'emen': 227, 'Zambia': 228, 'abwe': 229}

Del_n=[('Andrei Madaras', 28958150), ('Karla Chitimia', 28948428), ('Roberto Balacenoiu', 28974648),
      ('Cristian Ciocoi', 28969850), ('Flavius Soimosan', 28954757), ('Petru Zatic', 28951539),
      ('Alexandru Bulzan', 28972640), ('Pricope Ionut', 28969100), ('Alexandra Colf', 28987788),
      ('Vlad Caraiman', 28967905), ('Raluca Balea', 28990282), ('Amalia Berine', 28977184), ('Dan Proca', 28973590),
      ('Razvan Dinga', 28979371), ('Vlad Petcu', 28950208), ('Ovidiu Olariu', 28992444), ('Gelil Fabian', 28970255),
      ('Octavian Radulescu', 28950265), ('Marius Bubui', 28971809), ('Alin Filip', 28958899), ('Radu Flesar', 28969602),
      ('Gabriel Brezeanu', 28975887), ('Ivan Bumbuc', 28987655), ('Robert Gherman', 28969117),
      ('Cristian Gabor', 28984216), ('Tudorel Tihenea', 28951722), ('Isabela Stochin', 28992064),
      ('Mihaela Foltrauer', 28952289), ('Alexandru Galea', 28988512), ('Raul Sauca', 28973796),
      ('Vincze Simona', 28976645), ('Rares Stanciu', 28967880), ('Luciana Bulgar', 28968145),
      ('Daniel Bogdan', 28985217), ('Dragos Vîrtopeanu', 28960616), ('Laurentiu Casa', 28953489),
      ('Tania Curuțchi', 28964744), ('Constantin Geangalau', 28969837), ('Paul Feier', 28976660),
      ('Cosmina Dutcă', 28993023), ('Raul Cotuț', 28978233), ('Dragos  Badea', 28949428), ('Bogdan Filip', 28956874),
      ('Vlad Branduse', 28981594), ('Serban Duta', 28958677), ('Rares Ganea', 28949161), ('Bianca Giurgiu', 28951794),
      ('Marco Ghiriti', 28965741), ('Mihai Fârțală', 28977429), ('Andreea Udrescu', 28964346),
      ('Amalia Berinde', 28991313), ('Serban Duta', 28962386), ('Razvan Maciovan', 28973805),
      ('Andrei Pleian', 28957734), ('Roberta Iordan', 28971886), ('Ionut Mercescu', 28975450),
      ('Miruna Lascu', 28947891), ('George Hutanu', 28991625), ('Alex Iepure', 28991016), ('Claudiu Dinea', 28975398),
      ('Vlad Hritu', 28988899), ('Matei Isac', 28993424), ('Edi Toropu', 28962386), ('Alexandru Livadariu', 28949737),
      ('David Popa', 28964534), ('Roxana Gruianu', 28971186), ('Cristina Juletecan', 28965838),
      ('Valentina Hozit', 28967547), ('Cristian Knebel', 28978310), ('Andrei Matei', 28951191),
      ('Daniel Aguiar', 28973532), ('Xavier Elber', 28980676), ('Daniele Viola', 28982489), ('Iosif Goga', 28947925),
      ('Adrian Capusan', 28956467), ('Florin Ionut', 28986703), ('Alexandru Ghincea', 28968437)]



continents = {
     'EU': 'Europe',
     'NA': 'Americas',
     'SA': 'Americas',
     'AS': 'Asia',
     'OC': 'Oceania',
     'AF': 'Africa',
     'AN': 'Antarctica'
}
Tari_Harta=[]
cts=pc.map_countries()
#for i in range(48):
def Harta_Gen(i):
     l=0
     for c in LCO1:
          for x in range(1, i + 1):
                    l+=1
                    if x == 1:
                        proc = random.randrange(5, 25)
                    if x == 2:
                        proc = random.randrange(26, 50)
                    if x == 3:
                        proc = random.randrange(51, 90)
                    if x == 4:
                        proc = 100
                    try:
                        tara = ci.CountryInfo(c)
                        Tari_Harta.append([c,continents[pc.country_alpha2_to_continent_code(pc.country_name_to_country_alpha2(c))],proc,l,pc.country_name_to_country_alpha3(c),cts[c]['numeric']])
                    except Exception:
                           if c == "Reunion":
                               Tari_Harta.append([c, "Europe", proc, l, "REU", "638"])
                           if c == "Montenegro":
                               Tari_Harta.append([c, "Europa", proc, l, "MNE ", "891"])
                           if c == "Côte d'Ivoire":
                               Tari_Harta.append([c, "Africa", proc, l, "CIV", "384"])
                           if c == "Antarctica":
                               Tari_Harta.append(["Antarctica", "Antarctida", proc, l, "ATA", "010"])
                           if c == "Liberia":
                               Tari_Harta.append(["Liberia", "Africa", proc, l, "LBR", "430"])
                           if c == "Congo":
                               Tari_Harta.append(["Congo", "Africa", proc, l, "COG", "178"])
                           if c == "East Timor":
                               Tari_Harta.append(["East Timor", "Asia", proc, l, "TLS", "626"])
                           if c == "French Southern and Antarctic Lands":
                               Tari_Harta.append(["French Southern and Antarctic Lands", "Oceania", proc, l, "ATF", "260"])
                           if c == "Democratic Republic of the Congo":
                               Tari_Harta.append(["Democratic Republic of the Congo", "Africa", proc, l, "COD", "180"])

     with open(f"Mappppp.csv", "w", newline="", encoding="UTF-8") as csvfile:
       w = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
       w.writerow(["countries", "continents", "procent", "pas", "iso_alpha3", "iso_num"])
       for tari in Tari_Harta:
              w.writerow(tari)

Harta_Gen(4)

def Get_Tara(x):
    x=x.adresa.split(',')
    return x[3][1:]














def Get_T(c,loc):
    t=random.randint(1, 480)
    try:
        tz=Tz[loc]
    except Exception:
        tz="Local Time"
    m=t%60
    h=22+t//60
    if h > 24:
        h=h % 24
    if h == 24:
        h = 0
    if m >= 10:
        setattr(c,"delivery_time",str(h)+":"+str(m)+" "+tz)
    else:
        setattr(c, "delivery_time", str(h) + ":0" + str(m) + " " + tz)

def Dist_Elf(c):
         setattr(c, "delivered", "delivered")
         x=random.randint(0, len(Del_n)-1)
         setattr(c,"elf",Del_n[x][0])



csvfile=open(f"Elf-Stats.csv", "w", newline="", encoding="UTF-8")
w = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
w.writerow(["Elf","Total de Copii la care a dat"])
for elfi in Del_n:
    w.writerow([elfi[0],elfi[1]])
csvfile.close()



###################################################Citire Scrisori################################################

def nume_cadouri_culoare(line):
    for i in range(0, len(line)):
        if line[i]=="is" and line[i-1]=="name":
            i+=1
            name=line[i][:len(line[i])-1]
        elif line[i]=="colour" and (line[i-1]=="favorite" or line[i-1]=="the"):
            i+=1
            if line[i+1][len(line[i+1])-1]==".":
                pcolor=line[i]
                i+=1
                pcolor+=" "+line[i][:len(line[i])-1]
            else:
                pcolor=line[i][:len(line[i])-1]
        elif (line[i]=="want" and line[i-1]=="I" and line[i-2]=="year" and line[i-3]=="This") or (line[i]=="receive" and line[i-1]=="to" and line[i-2]=="want" and line[i-3]=="I") or (line[i]=="get" and line[i-1]=="to" and line[i-2]=="wish" and line[i-3]=="I") or (line[i+1]!="to" and line[i]=="like" and line[i-1]=="would" and line[i-2]=="I") or (line[i]=="love" and line[i-1]=="would" and line[i-2]=="I") or (line[i]=="receive" and line[i-1]=="to" and line[i-2]=="like" and line[i-3]=="would" and line[i-4]=="I") or (line[i]=="for" and line[i-1]=="wish" and line[i-2]=="I") or (line[i]=="get" and line[i-1]=="to" and line[i-2]=="wish" and line[i-3]=="I") or (line[i]=="receive" and line[i-1]=="to" and line[i-2]=="is" and line[i-3]=="wish" and line[i-4]=="My"):
            i+=1
            l=[]
            cadouri=[]
            while line[i][len(line[i])-1]!=".":
                if line[i]=="and" and len(l)>1:
                    
                    x=" ".join(l)
                    cadouri.append(Gift(x, 1, pcolor))
                    l.clear()
                elif line[i]=="and" and len(l)<1:
                    pass
                elif line[i][len(line[i])-1]==",":
                    l.append(line[i][:len(line[i])-1])
                    x=" ".join(l)
                    
                    
                    cadouri.append(Gift(x, 1, pcolor))
                    l.clear()
                else:
                    l.append(line[i])
                i+=1
            l.append(line[i][:len(line[i])-1])
            x=" ".join(l)
            
 
            
            cadouri.append(Gift(x, 1, pcolor))
            return (name, pcolor, cadouri)




parent_dir = os.getcwd()
Path = parent_dir
csvfile=open("{0}//Date.csv".format(Path), "w", newline="", encoding="UTF-8")
w = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
w.writerow(["UUID","NAME","ADRESA","CADOURI","PCOLOR","DELIVERED","ELF","ORA PRIMIRII"])
# print(psutil.virtual_memory().percent)
size=os.stat(file).st_size
with open(file, "rb") as f:
    with tqdm (total=size, desc="I'm speed") as pbar:
        with mmap.mmap(f.fileno(), 0, prot=mmap.PROT_READ) as mm:
            for line in iter(mm.readline, b''):
                row=line.decode("utf-8")
                progress += len(line)
                if progress%100==0:
                    pbar.update(progress - pbar.n)
                if len(row)<3:
                    continue

                elif row[0]=="n" and row[1]=="*":
                    continue

                elif row[0]=="D" and row[1]=="e" and row[2]=="a" and row[3]=="r":
                    continue

                elif row[0]=="e" and row[1]=="x" and row[2]=="p":
                    copil.adresa=row[4:len(row)-1]
                    #continue #aici se termina o scrisoare
                    verificare_materiale(copil)
                    Dist_Elf(copil)
                    Get_T(copil,Get_Tara(copil))
                    w = csv.writer(csvfile, quoting=csv.QUOTE_NONNUMERIC, delimiter=",")
                    l = copil.get_name_cadouri()
                    w.writerow([copil.id, copil.name, copil.adresa, l , copil.pcolor, copil.delivered, copil.elf, copil.delivery_time])
                    impachetare(copil)
                    #calcul_timp_total()
    
                else:
                    copil = Copil(*nume_cadouri_culoare(row.split()))
csvfile.close()
# print(counter)
#end = time.time()
#print(end-start)
