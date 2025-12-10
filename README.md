# 🚗 Car Price Prediction – Çoklu Doğrusal Regresyon + Flask Arayüzü  
**BLG-407 Makine Öğrenmesi – Proje 3**

Bu projede araç özelliklerine göre satış fiyatı tahmin eden bir **Çoklu Doğrusal Regresyon modeli** geliştirilmiş ve model Flask tabanlı bir web arayüzüne entegre edilmiştir.

---

## 📌 Projenin Amacı  
Araçlara ait teknik ve kategorik özellikler kullanılarak satış fiyatının tahmin edilmesi hedeflenmiştir.  
Model Python, scikit-learn ve statsmodels kütüphaneleri ile eğitilmiş, Flask web uygulaması ile kullanıcıya sunulmuştur.

---

## 📁 Proje Dosya Yapısı

```
Proje3_ML_Flask/
├── Data/
│   └── car_price.csv
│
├── templates/
│   └── index.html
│  
│
├── app.py
├── model.pkl
├── Proje3.ipynb
└── README.md
```

---

## 📊 Kullanılan Özellikler (Features)

Modele dahil edilen 10 özellik:

- wheelbase  
- carlength  
- carwidth  
- curbweight  
- enginesize  
- horsepower  
- citympg  
- highwaympg  
- carbody (kategorik)  
- drivewheel (kategorik)

---

## 🛠️ Veri İşleme Süreci

### ✔️ Sayısal Değişkenler  
`StandardScaler` ile ölçeklendirildi.

### ✔️ Kategorik Değişkenler  
`OneHotEncoder(drop='first')` yöntemiyle dummy tuzağı engellendi.

### ✔️ Pipeline Yapısı  
Tüm işlemler tek bir pipeline içerisinde birleştirildi ve model bu yapı üzerinden eğitildi.

---

## 📈 Model Eğitimi ve Performans Sonuçları

Veri seti %80 eğitim, %20 test olacak şekilde ayrılmıştır. Aşağıdaki performans metrikleri elde edilmiştir:

- **R²:** `0.74`  
- **MAE (Mean Absolute Error):** `3383.45`  
- **MSE (Mean Squared Error):** `18,991,807`

Model, fiyat tahmini için yeterli performansı göstermiştir.

---

## 🧪 Backward Elimination (Geriye Doğru Eleme)

Statsmodels OLS kullanılarak p-value değerleri incelenmiş, p > 0.05 olan değişkenler modelden çıkarılmıştır.

Modelden çıkarılan değişkenler:  
- curbweight  
- carbody_sedan  
- drivewheel_fwd  
- carlength  

Bu işlem sonunda istatistiksel olarak daha anlamlı bir model elde edilmiştir.

---

## 🧩 Flask Web Arayüzü

Model Flask uygulamasına entegre edilmiştir.  
Kullanıcı form üzerinden özellikleri girerek araç fiyatı tahmini alabilir.

---

## 💾 Modelin Kaydedilmesi

Model aşağıdaki kod ile `.pkl` formatında kaydedilmiştir:

```python
import pickle
with open("model.pkl", "wb") as f:
    pickle.dump(regressor, f)
Bu dosya Flask uygulaması tarafından yüklenerek tahmin üretmektedir.
``` 

## ▶️ Flask Uygulamasını Çalıştırma

Terminalden:

```bash
python app.py
```

Tarayıcıdan:

```bash
http://127.0.0.1:5000/
```

## 📌 Kullanılan Teknolojiler

| Teknoloji    | Açıklama                    |
| ------------ | --------------------------- |
| Python       | Veri işleme & model eğitimi |
| scikit-learn | Regresyon modeli            |
| statsmodels  | OLS & Backward Elimination  |
| Flask        | Web arayüzü                 |
| HTML/CSS     | Kullanıcı arayüzü           |
