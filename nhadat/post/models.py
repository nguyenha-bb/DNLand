from django.db import models

class Province(models.Model):
    provinceName = models.CharField(max_length=100)
    class Meta:
        db_table = 'Provinces'
    def __str__(self):
        return self.provinceName

class District(models.Model):
    districtName = models.CharField(max_length=100)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Districts'
    def __str__(self):
        return self.districtName

class Ward(models.Model):
    wardName = models.CharField(max_length=100)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Wards'
    def __str__(self):
        return self.wardName

class Direction(models.Model):
    directionName = models.CharField(max_length=30)
    class Meta:
        db_table = 'Directions'
    def __str__(self):
        return self.directionName

class Post(models.Model):
    title = models.CharField(max_length=200)
    price = models.BigIntegerField()
    square = models.FloatField()
    description = models.TextField()
    postTime = models.DateField(blank=True, null=True)
    addressDetail = models.CharField(max_length=200)
    status = models.IntegerField(blank=True, null=True)
    image = models.ImageField(upload_to ='images/', blank=True, null=True)
    direction = models.ForeignKey(Direction, on_delete=models.CASCADE)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE)
    ward = models.ForeignKey(Ward, on_delete=models.CASCADE)
    account = models.ForeignKey('users.Account', on_delete=models.CASCADE, blank=True, null=True)
    class Meta:
        db_table = 'Posts'
