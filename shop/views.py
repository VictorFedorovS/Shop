from flask import render_template, request
from . import models


def index_page():

    query = models.db.select(models.Phone)

    if "brand" in request.args and len(request.args["brand"]) > 0:
        query = query.join(models.Phone.brand).where(models.Brand.pk == request.args["brand"])
    if "color" in request.args and len(request.args["color"]) > 0:
        query = query.join(models.Phone.color).where(models.Color.pk == request.args["color"])

    if "priceMIN" in request.args and int(request.args["priceMIN"]) > 0:
        a = int(request.args["priceMIN"])
        query = query.filter(models.Phone.price >= a)

    if "priceMAX" in request.args and int(request.args["priceMAX"]) > 0:
        a = int(request.args["priceMAX"])
        query = query.filter(models.Phone.price <= a)
    
    query_brands = models.db.select(models.Brand)
    brands = models.db.session.execute(query_brands).scalars()
    phones = models.db.session.execute(query).scalars()
    
    query_colors = models.db.select(models.Color)
    colors = models.db.session.execute(query_colors).scalars()
    
    return render_template("index.html", phones=phones, brand = brands, color = colors)


def product_page(product_id):

    product = models.db.get_or_404(models.Phone, product_id)
    return render_template("product.html", product=product)