from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from user.models import User


class User_Admin(UserAdmin):
	list_display = ('username','first_name','last_name','email')
	search_feild = ('username','email')
	#readonly_feild = ('first_name ', 'last_name ')

	filter_horizontal = ()
	list_filter = ()
	fieldsets = ()

admin.site.register(User, User_Admin)
