from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from django.urls import reverse

# Create your models here.
class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)

class Category(models.Model):
    name = models.CharField(_("nama-kategori"), max_length=255, db_index=True)
    slug = models.SlugField(_("slug"), max_length=255, unique=True)
    

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categorys")
    
    def get_absolute_url(self):
        return reverse('store:category_list', args=[self.slug])


    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Category_detail", kwargs={"pk": self.pk})


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name=_("category"), on_delete=models.CASCADE)
    created_by = models.ForeignKey(User,  verbose_name=_("product_creator"), on_delete=models.CASCADE)
    title = models.CharField(_("judul"), max_length=255)
    author = models.CharField(_("pencipta"), max_length=255, default = 'admin')
    description = models.TextField(_("deskripsi"), blank=True)
    image = models.ImageField(_("gambar"), upload_to='images/', height_field=None, width_field=None, max_length=None)
    slug = models.SlugField(_("product-slug"), max_length=255)
    price = models.DecimalField(_("harga"), max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(_("stok"), default=True)
    is_active = models.BooleanField(_("aktif"), default=True)
    created = models.DateTimeField(_("tanggal_created"), auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(_("tangal_update"), auto_now=True, auto_now_add=False)

    objects = models.Manager()
    products = ProductManager()


    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")
        ordering = ('-created',)

    def get_absolute_url(self):
        return reverse('store:product_detail', args=[self.slug])

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("Product_detail", kwargs={"pk": self.pk})




    

    

