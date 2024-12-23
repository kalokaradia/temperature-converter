from django.shortcuts import render


def index(request):
    hasil_konversi = None  # Inisialisasi hasil_konversi
    tipe_suhu_akhir_output = None  # Untuk menyertakan tipe suhu akhir dalam hasil

    if request.method == "POST":
        # Ambil data dari form
        try:
            suhu_awal = float(request.POST.get("suhu_awal", 0))
            tipe_suhu_awal = request.POST.get("tipe_suhu_awal", "")
            tipe_suhu_akhir = request.POST.get("tipe_suhu_akhir", "")

            # Logika Konversi Suhu
            if tipe_suhu_awal == "Celcius" and tipe_suhu_akhir == "Reamur":
                hasil_konversi = suhu_awal * 4 / 5
            elif tipe_suhu_awal == "Reamur" and tipe_suhu_akhir == "Celcius":
                hasil_konversi = suhu_awal * 5 / 4
            elif tipe_suhu_awal == "Celcius" and tipe_suhu_akhir == "Fahrenheit":
                hasil_konversi = (suhu_awal * 9 / 5) + 32
            elif tipe_suhu_awal == "Fahrenheit" and tipe_suhu_akhir == "Celcius":
                hasil_konversi = (suhu_awal - 32) * 5 / 9
            elif tipe_suhu_awal == tipe_suhu_akhir:
                hasil_konversi = suhu_awal
            else:
                hasil_konversi = "Konversi tidak didukung."

            # Set tipe suhu akhir untuk ditampilkan
            tipe_suhu_akhir_output = tipe_suhu_akhir
        except ValueError:
            hasil_konversi = "Input suhu tidak valid."

    return render(
        request,
        "index.html",
        {"hasil": hasil_konversi, "tipe_suhu_akhir": tipe_suhu_akhir_output},
    )
