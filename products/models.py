from django.db import models

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    release = models.CharField(max_length=254)
    size = models.CharField(max_length=254)
    os = models.CharField(max_length=254)
    screen_size = models.CharField(max_length=254)
    resolution = models.CharField(max_length=254)
    number_of_cams = models.IntegerField(blank=False, null=False)
    camera_1 = models.CharField(max_length=254, default=False, blank=False, null=False)
    camera_2 = models.CharField(max_length=254, default=False, blank=False, null=False)
    camera_3 = models.CharField(max_length=254, default=False, blank=False, null=False)
    video = models.CharField(max_length=254, default=False, blank=False, null=False)
    picture = models.CharField(max_length=254, default=False, blank=False, null=False)
    selfie_video = models.CharField(max_length=254, default=False, blank=False, null=False)
    ram = models.CharField(max_length=254)
    card_reader = models.CharField(max_length=254, blank=False, null=False)
    card_supported = models.CharField(max_length=254, blank=False, null=False)
    storage_cap = models.CharField(max_length=254)
    microphone = models.BooleanField(default=False, null=True, blank=True)
    speakers = models.BooleanField(default=False, null=True, blank=True)
    headphone_jack = models.BooleanField(default=False, null=True, blank=True)
    wireless_charging = models.BooleanField(default=False, null=True, blank=True)
    charging_port = models.CharField(max_length=254, blank=False, null=False)
    battery = models.CharField(max_length=254)
    price = models.CharField(max_length=7)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
