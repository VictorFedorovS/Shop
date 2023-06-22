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

def product_page():

    query_descriptions = models.db.select(models.Description)
    query_brands = models.db.select(models.Brand)
    query_names = models.db.select(models.Phone)
    query = models.db.select(models.Phone)

    if "description" in request.args and len(request.args["description"]) > 0:
        query = query.join(models.Phone.description).where(models.Description.pk == request.args["description"])

    if "brand" in request.args and len(request.args["brand"]) > 0:
        query = query.join(models.Phone.brand).where(models.Brand.pk == request.args["brand"])

    if "name" in request.args and len(request.args["name"]) > 0:
        query = query.join(models.Phone.name).where(models.Phone.pk == request.args["name"])
    
    descriptions = models.db.session.execute(query_descriptions).scalars()
    brands = models.db.session.execute(query_brands).scalars()
    phones = models.db.session.execute(query).scalars()
    names = models.db.session.execute(query_names).scalars()

    return render_template("product.html", description=descriptions,brand = brands, phones=phones, name=names)
    
