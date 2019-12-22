from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save


class Bank(models.Model):
	name = models.CharField(max_length=30, unique=True)
	address = models.CharField(max_length=100)
	contact = models.CharField(max_length=10)
	city = models.CharField(max_length=20, default="null")
	A_pos = models.IntegerField()
	A_neg = models.IntegerField()
	B_pos = models.IntegerField()
	B_neg = models.IntegerField()
	O_pos = models.IntegerField()
	O_neg = models.IntegerField()
	AB_pos = models.IntegerField()
	AB_neg = models.IntegerField()
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	slug= models.SlugField(blank=True, unique=True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['slug', ]


	def __str__(self):
		return self.name







def pre_save_form(sender, instance, *args, **kwargs):
		if not instance.slug:
			instance.slug= slugify(instance.owner.username + "-" + instance.name)

pre_save.connect(pre_save_form, sender=Bank)

#    def has_module_perms(self, app_label):
#        return True