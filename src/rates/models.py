from tortoise.models import Model
from tortoise import fields


class Rate(Model):
    cargo_type = fields.CharField(max_length=50)
    rate = fields.FloatField()
    date_from = fields.DateField()

    class Meta:
        unique_together = ('rate', 'date_from')
