from django.shortcuts import render
from .forms import PCForm, PieceForm
from .models import PCpiece, TypeItem
from . import priceparse
from django.http import HttpResponseRedirect

# Create your views here.
def pcbuild(request):
    if request.method == "POST":
        items = ("CPU", "GPU", "RAM", "case", "block", "motherboard")
        prices = []
        for item in items:
            piece = PCpiece.objects.get(id=request.POST.get(item)).name
            if piece != "-":
                prices.append((f"{item} {piece}", priceparse.check_price(piece)))
        context = {
            "prices": prices,
        }
        return render(request, "pcbuild/price_list.html", context)
    types = TypeItem.objects.all()
    context = {
        "pcform": PCForm(),
        "types": types,
    }
    return render(request, "pcbuild/index.html", context)


def add_piece(request, id):
    if request.method == "POST":
        name = request.POST.get("name")
        new_piece = PCpiece(name=name, typeitem=TypeItem.objects.get(id=id))
        new_piece.save()
        return HttpResponseRedirect("/")
    pieceform = PieceForm()
    context = {
        "pieceform": pieceform,
        "id": id,
        "types": TypeItem.objects.all(),
    }
    return render(request, "pcbuild/add_piece.html", context)
