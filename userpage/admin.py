from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from userpage.models import Bank


#class User_BankAdmin(UserAdmin):
#	list_display = ('username','name','address','contact','A_pos','A_neg','B_pos','B_neg','O_pos','O_neg','AB_pos','AB_neg')
#	search_feild = ('username','name')
	#readonly_feild = ('first_name ', 'last_name ')

#	filter_horizontal = ()
#	list_filter = ()
#	fieldsets = ()

admin.site.register(Bank)
