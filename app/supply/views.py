from django.shortcuts import render
from .models import Supplier, Material, Supply

def index(request):
    suppliers = Supplier.objects.all()
    materials = Material.objects.all()
    supplies = Supply.objects.select_related("supplier", "material")

    context = {
        "project_name": "Відділ поставок",
        "student": "Маслиган Віталій Романович, ІПЗ-22009б",
        "suppliers": suppliers,
        "materials": materials,
        "supplies": supplies,
    }

    return render(request, "index.html", context)
