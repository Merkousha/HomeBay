from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)    
   
class State(models.Model):
    name = models.CharField(max_length=100)     
    country = models.ForeignKey(Country,on_delete=models.CASCADE)    
    
class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.ForeignKey(State,on_delete=models.CASCADE)        

class Area(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City,on_delete=models.CASCADE)    
    

class Builder(models.Model):
     name= models.TextField(max_length=20)
     description = models.TextField( max_length=2000)
     picture=models.ImageField(null=True, blank=True)
     def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField( max_length=2000)
    address = models.TextField(max_length=300)
    phone_number = models.CharField(max_length=10)
    Year_of_Construction= models.DecimalField(max_digits=4,decimal_places=0)
    Number_of_rooms= models.DecimalField(max_digits=2 ,decimal_places=0)
    Ground_Area=models.FloatField()
    Features=models.TextField(max_length=4000)
    Total_Price=models.DecimalField(max_digits=14,decimal_places=0)
    Price_per_meter=models.DecimalField(max_digits=14,decimal_places=0)
    area = models.ForeignKey(Area,on_delete=models.CASCADE)  
    Builder = models.ForeignKey(Builder,on_delete=models.CASCADE,null=True, blank=True , related_name='builder')
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['id']    


        
class Property_Images(models.Model):
    picture = models.ImageField(null=True, blank=True , upload_to ='images')
    property = models.ForeignKey(Property,on_delete=models.CASCADE , related_name='pictures')    
    
    