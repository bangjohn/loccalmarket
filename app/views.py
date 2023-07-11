import os
import uuid

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "../templates/app/index.html")


def dashboard(request):
    # ...
    context = {
        "sidebar_active": "dashboard",
        # ...
    }
    return render(request, "../templates/app/pages/dashboard.html", context)


def product_list(request):
    # ...
    context = {
        "sidebar_active": "product_list",
        "submenu_active": "list",
        # ...
    }
    return render(request, "../templates/app/pages/product_list.html", context)


def add_product(request):
    # ...
    context = {
        "sidebar_active": "product_list",
        "submenu_active": "add_prodoct",
        # ...
    }
    return render(request, "../templates/app/pages/add_product.html", context)


# upload temp image filepond
def temp_image_upload(request):
    # Logika untuk mengunggah gambar ke server
    if request.method == "POST":
        image_file = request.FILES.get("filepond")
        if image_file:
            folder_name = str(uuid.uuid4())[:6]
            folder_path = os.path.join(
                settings.STATICFILES_DIRS[0], "temp", "images", folder_name
            )

            # Membuat direktori jika belum ada
            os.makedirs(folder_path, exist_ok=True)

            # Menyimpan file gambar di dalam folder yang menggunakan UUID
            file_path = os.path.join(folder_path, image_file.name)
            with open(file_path, "wb") as f:
                for chunk in image_file.chunks():
                    f.write(chunk)

            # Balas dengan ID lokasi unik
            return HttpResponse(folder_name, content_type="text/plain")
        else:
            # Tidak ada gambar yang diunggah
            return HttpResponse(status=400)
    else:
        # Metode HTTP tidak diizinkan
        return HttpResponse(status=405)


# delete temp image filepond
def temp_image_delete(request):
    if request.method == "DELETE":
        folder_id = request.body.decode("utf-8")
        folder_path = os.path.join(
            settings.STATICFILES_DIRS[0], "temp", "images", folder_id
        )

        if os.path.exists(folder_path):
            # Menghapus folder dan isinya
            try:
                for file_name in os.listdir(folder_path):
                    file_path = os.path.join(folder_path, file_name)
                    if os.path.isfile(file_path):
                        os.remove(file_path)

                os.rmdir(folder_path)
                return HttpResponse()
            except OSError:
                # Gagal menghapus folder
                return HttpResponse(status=500)
        else:
            # Folder tidak ditemukan
            return HttpResponse(status=404)
    else:
        # Metode HTTP tidak diizinkan
        return HttpResponse(status=405)
