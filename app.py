data = [
  { "ad": "Aysel Həsənova", "pese": "Qrafik dizayner", "maas": 1200 },
  { "ad": "Murad Məmmədov", "pese": "Frontend proqramçı", "maas": 1800 },
  { "ad": "Nərmin Əliyeva", "pese": "Mühasib", "maas": 1400 },
  { "ad": "Rauf Quliyev", "pese": "Backend mühəndis", "maas": 2200 },
  { "ad": "Günel Rzayeva", "pese": "Məktəb müəllimi", "maas": 800 },
  { "ad": "Orxan Hacıyev", "pese": "Sistem administratoru", "maas": 1600 },
  { "ad": "Sevinc Cəfərova", "pese": "HR mütəxəssis", "maas": 1300 },
  { "ad": "Elvin İsmayılov", "pese": "Mobil developer", "maas": 2100 },
  { "ad": "Ləman Qasımova", "pese": "Kontent menecer", "maas": 1000 },
  { "ad": "Kamran Vəliyev", "pese": "Data analitik", "maas": 2300 },
  { "ad": "Şəbnəm Ələkbərova", "pese": "Marketinq mütəxəssisi", "maas": 1500 },
  { "ad": "Emin Səfərov", "pese": "DevOps mühəndis", "maas": 2400 },
  { "ad": "Aygün Hüseynova", "pese": "UX/UI dizayner", "maas": 1700 },
  { "ad": "Samir Səmədov", "pese": "Satış meneceri", "maas": 1100 },
  { "ad": "Nigar Məmmədli", "pese": "SMM mütəxəssisi", "maas": 1200 },
  { "ad": "Tural Qarayev", "pese": "Fullstack developer", "maas": 2500 },
  { "ad": "Zəhra Abdullayeva", "pese": "Projekt menecer", "maas": 2000 },
  { "ad": "Elçin Muradov", "pese": "Mexanik mühəndis", "maas": 1600 },
  { "ad": "Leyla Rüstəmova", "pese": "Tərcüməçi", "maas": 900 },
  { "ad": "Fərid Şirinov", "pese": "Kibertəhlükəsizlik üzrə mütəxəssis", "maas": 2600 }
]
import json

st_ = json.dumps(data)
with open("data.json","w") as file:
    file.write(st_)
    file.close()
