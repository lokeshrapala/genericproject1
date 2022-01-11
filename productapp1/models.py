from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class product(models .Model ):
    pid=models .AutoField (primary_key= True )
    pname=models .CharField (max_length= 20)
    pcost=models.DecimalField(max_digits=12,decimal_places=2)
    def __str__(self):
        return str(self.pid)