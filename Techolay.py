import requests
from bs4 import BeautifulSoup

data_list = []

def techolay():
    for page_number in range(1, 7):
        response = requests.get(f'https://techolay.net/sosyal/bolum/programlama.80/page-{page_number}')
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')

            konu_basliklari = soup.find_all(class_="structItem-title")
            yazar_adlari = soup.find_all(class_="structItem-parts")
            mesaj_sayilari = soup.find_all(class_="pairs pairs--justified")
            goruntulenme_sayilari = soup.find_all(class_="pairs pairs--justified structItem-minor")

            for konu, yazar, mesaj, goruntulenme in zip(konu_basliklari, yazar_adlari, mesaj_sayilari, goruntulenme_sayilari):
                baslik = konu.text.replace("Rehber", "").strip()
                yazar_ismi = yazar.text.split()[0]
                mesaj_sayisi = mesaj.text.split()[1]
                goruntulenme_sayisi = goruntulenme.text.split()[1]

                data_dict = {
                    "Konu Başlığı": baslik,
                    "Yazar Adı": yazar_ismi,
                    "Mesaj Sayısı": mesaj_sayisi,
                    "Görüntülenme Sayısı": goruntulenme_sayisi
                }

                print(f"Konu {len(data_list) + 1}:")
                for key, value in data_dict.items():
                    print(f"{key}: {value}")
                print("")

                data_list.append(data_dict)

techolay()