from django import forms

from userpage.models import Bank

class OwnersForm(forms.ModelForm):
	

	class Meta:
		model = Bank
		fields = ("name", "address", "contact","city", "A_pos", "A_neg", "B_pos", "B_neg", "O_pos", "O_neg", "AB_pos", "AB_neg" )



class UpdateForm(forms.ModelForm):
	

	class Meta:
		model = Bank
		fields = ("A_pos", "A_neg", "B_pos", "B_neg", "O_pos", "O_neg", "AB_pos", "AB_neg" )

	def save(self, commit=True):
		update= self.instance

		#update.name= self.cleaned_data['name']
		#update.address= self.cleaned_data['address']
		#update.contact= self.cleaned_data['contact']
		update.A_pos= self.cleaned_data['A_pos']
		update.A_neg= self.cleaned_data['A_neg']
		update.B_pos= self.cleaned_data['B_pos']
		update.B_neg= self.cleaned_data['B_neg']
		update.O_pos= self.cleaned_data['O_pos']
		update.O_neg= self.cleaned_data['O_neg']
		update.AB_pos= self.cleaned_data['AB_pos']
		update.AB_neg= self.cleaned_data['AB_neg']

		if commit:
			update.save()
		return update
