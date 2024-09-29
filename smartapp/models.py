from django.db import models


class mobiles(models.Model):
    id=models.AutoField(primary_key=True)
    brand=models.CharField(max_length=150)
    model=models.CharField(max_length=150)
    colour=models.CharField(max_length=150)
    price=models.IntegerField()


    class Meta:
        db_table='mobile_table'

