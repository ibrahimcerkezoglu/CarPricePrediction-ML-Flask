from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

# Eğitilmiş modeli yükle
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Modelde kullandığımız feature isimleri (Not: ipynb ile birebir aynı sırada!)
FEATURES = [
    "wheelbase",
    "carlength",
    "carwidth",
    "curbweight",
    "enginesize",
    "horsepower",
    "citympg",
    "highwaympg",
    "carbody",
    "drivewheel",
]


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    error = None

    # Formu tekrar doldururken önceki değerler kaybolmasın diye
    input_values = {f: "" for f in FEATURES}

    if request.method == "POST":
        try:
            # Formdan gelen değerleri al
            input_values["wheelbase"] = request.form.get("wheelbase", "")
            input_values["carlength"] = request.form.get("carlength", "")
            input_values["carwidth"] = request.form.get("carwidth", "")
            input_values["curbweight"] = request.form.get("curbweight", "")
            input_values["enginesize"] = request.form.get("enginesize", "")
            input_values["horsepower"] = request.form.get("horsepower", "")
            input_values["citympg"] = request.form.get("citympg", "")
            input_values["highwaympg"] = request.form.get("highwaympg", "")
            input_values["carbody"] = request.form.get("carbody", "")
            input_values["drivewheel"] = request.form.get("drivewheel", "")

            # Sayısal olanları float'a çevir
            data = {
                "wheelbase": float(input_values["wheelbase"]),
                "carlength": float(input_values["carlength"]),
                "carwidth": float(input_values["carwidth"]),
                "curbweight": float(input_values["curbweight"]),
                "enginesize": float(input_values["enginesize"]),
                "horsepower": float(input_values["horsepower"]),
                "citympg": float(input_values["citympg"]),
                "highwaympg": float(input_values["highwaympg"]),
                "carbody": input_values["carbody"],
                "drivewheel": input_values["drivewheel"],
            }

            # Tek satırlık DataFrame oluştur
            df_input = pd.DataFrame([data], columns=FEATURES)

            # Tahmin yap
            y_pred = model.predict(df_input)[0]
            prediction = round(float(y_pred), 2)

        except Exception as e:
            # Hata olursa kullanıcıya basit bir mesaj göster
            error = "Lütfen tüm alanları eksiksiz ve doğru formatta doldurun."

    return render_template(
        "index.html",
        prediction=prediction,
        error=error,
        input_values=input_values,
    )


if __name__ == "__main__":
    # Sunucuyu başlat
    app.run(debug=True)
