from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from . import models

admin = Admin()
admin.add_view(ModelView(models.Brand, models.db.session))
admin.add_view(ModelView(models.Color, models.db.session))
admin.add_view(ModelView(models.Phone, models.db.session))
admin.add_view(ModelView(models.Description, models.db.session))
