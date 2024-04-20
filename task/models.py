from django.db import models


class BaseModel(models.Model):
    name = models.CharField(max_length=255)

    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Region(BaseModel):
    def __str__(self):
        return self.name


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts')

    def __str__(self):
        return self.name


class Neighborhood(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='neighborhoods')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='neighborhoods')

    def __str__(self):
        return self.name


class Street(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='streets')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='streets')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='streets')

    def __str__(self):
        return self.name


class House(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='houses')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='houses')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='houses')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='houses')
    number_of_appartment = models.IntegerField()
    ownership = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    category_appartment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.number_of_appartment}-uy"


def upload_to(instance, filename):
    return 'images/{filename}'.format(filename=filename)


class Person(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='persons')
    district = models.ForeignKey(District, on_delete=models.CASCADE, related_name='persons')
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.CASCADE, related_name='persons')
    street = models.ForeignKey(Street, on_delete=models.CASCADE, related_name='persons')
    house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='persons')
    residential_status = models.CharField(max_length=255)
    passport_number = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    age = models.CharField(null=True, blank=True)
    jshshir = models.CharField()
    phone_number = models.CharField(max_length=255)
    appartment_type = models.CharField(max_length=255)
    cadastr_number = models.CharField(max_length=255)
    status_of_registration = models.CharField(max_length=255)
    time_registered = models.DateField()
    address_of_passport = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to=upload_to)
    gender = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Relative(BaseModel):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='relatives')
    document_type = models.CharField(max_length=255)
    document_series = models.CharField(max_length=20)
    document_number = models.IntegerField()
    kinship = models.CharField(max_length=255)
    jshshir = models.BigIntegerField()
    phone_number = models.CharField(max_length=255)
    nationality = models.CharField(max_length=255)
    disability = models.CharField(max_length=255)
    war_participant = models.BooleanField(default=False)
    no_breadwinner = models.BooleanField(default=False)
    lonely_old_man = models.BooleanField(default=False)
    difficult_condition = models.BooleanField(default=False)
    behind_war = models.BooleanField(default=False)
    gone_for_along_time = models.BooleanField(default=False)
    participant_of_AES = models.BooleanField(default=False)

    def __str__(self):
        return self.name
