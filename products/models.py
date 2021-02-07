from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):

    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, blank=True)
    brand = models.CharField(max_length=254)
    name = models.CharField(max_length=254)
    unfriendly_name = models.CharField(max_length=254, default=False)
    colour = models.CharField(max_length=100, default="Black")
    hex_colour = models.CharField(max_length=100, default="#000000")
    release_date = models.CharField(max_length=254)
    release_year = models.IntegerField(default=False, blank=False, null=False)
    size = models.CharField(max_length=254)
    os = models.CharField(max_length=254)
    screen_size = models.CharField(max_length=254)
    resolution = models.CharField(max_length=254)
    number_of_cams = models.IntegerField(blank=False, null=False)
    camera_1 = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    camera_2 = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    camera_3 = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    camera_4 = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    video = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    selfie_camera = models.BooleanField(default=False, null=True, blank=True)
    picture = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    selfie_video = models.CharField(
        max_length=254, default=False, blank=False, null=False)
    ram = models.CharField(max_length=254)
    card = models.BooleanField(default=False, null=True, blank=True)
    card_reader = models.CharField(max_length=254, blank=False, null=False)
    card_supported = models.CharField(max_length=254, blank=False, null=False)
    storage_cap = models.CharField(max_length=254)
    microphone = models.BooleanField(default=False, null=True, blank=True)
    speakers = models.BooleanField(default=False, null=True, blank=True)
    headphone_jack = models.BooleanField(default=False, null=True, blank=True)
    wireless_charging = models.BooleanField(default=False, blank=True)
    charging_port = models.CharField(max_length=254, blank=False, null=False)
    battery = models.CharField(max_length=254)
    rating = models.DecimalField(
        max_digits=3, decimal_places=1, null=True, blank=True)
    price = models.DecimalField(
        max_digits=7, decimal_places=2, null=True, blank=True)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, blank=True)
    image_display = models.ImageField(blank=True)
    image_rear_check = models.BooleanField(default=False, blank=True)
    image_front = models.ImageField(blank=True)
    image_rear = models.ImageField(blank=True)

    def __str__(self):
        return self.name
