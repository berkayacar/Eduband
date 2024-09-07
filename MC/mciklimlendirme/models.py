from django.db import models

class Teklif(models.Model):
    # Birinci set
    genislik_1 = models.PositiveIntegerField()
    bitmis_uzunluk_1 = models.PositiveIntegerField()
    diyagonal_1 = models.PositiveIntegerField()
    lamel_uzunluk_1 = models.PositiveIntegerField()
    hatve_1 = models.PositiveIntegerField()
    adet_1 = models.PositiveIntegerField()

    # İkinci set
    genislik_2 = models.PositiveIntegerField()
    bitmis_uzunluk_2 = models.PositiveIntegerField()
    diyagonal_2 = models.PositiveIntegerField()
    lamel_uzunluk_2 = models.PositiveIntegerField()
    hatve_2 = models.PositiveIntegerField()
    adet_2 = models.PositiveIntegerField()

    # Üçüncü set
    genislik_3 = models.PositiveIntegerField(null=True, blank=True)
    bitmis_uzunluk_3 = models.PositiveIntegerField(null=True, blank=True)
    diyagonal_3 = models.PositiveIntegerField(null=True, blank=True)
    lamel_uzunluk_3 = models.PositiveIntegerField(null=True, blank=True)
    hatve_3 = models.PositiveIntegerField(null=True, blank=True)
    adet_3 = models.PositiveIntegerField(null=True, blank=True)

    # Dördüncü set
    genislik_4 = models.PositiveIntegerField(null=True, blank=True)
    bitmis_uzunluk_4 = models.PositiveIntegerField(null=True, blank=True)
    diyagonal_4 = models.PositiveIntegerField(null=True, blank=True)
    lamel_uzunluk_4 = models.PositiveIntegerField(null=True, blank=True)
    hatve_4 = models.PositiveIntegerField(null=True, blank=True)
    adet_4 = models.PositiveIntegerField(null=True, blank=True)

    # Beşinci set
    genislik_5 = models.PositiveIntegerField(null=True, blank=True)
    bitmis_uzunluk_5 = models.PositiveIntegerField(null=True, blank=True)
    diyagonal_5 = models.PositiveIntegerField(null=True, blank=True)
    lamel_uzunluk_5 = models.PositiveIntegerField(null=True, blank=True)
    hatve_5 = models.PositiveIntegerField(null=True, blank=True)
    adet_5 = models.PositiveIntegerField(null=True, blank=True)

    # Diğer form alanları
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"




class ContactFormSubmission(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Otomatik olarak oluşturulma zamanını ekler

    def __str__(self):
        return f'{self.name} - {self.email}'