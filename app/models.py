from django.db import models

# Create your models here.

class Dept(models.Model):
    dname=models.CharField(max_length=10)
    dno=models.IntegerField(primary_key=5)
    dloc=models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.dname
    
class Emp(models.Model):
    dnumber=models.ForeignKey(Dept,on_delete=models.CASCADE)
    ename=models.CharField(max_length=10)
    enumber=models.IntegerField()
    
    def __str__(self) -> str:
        return self.ename