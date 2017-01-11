from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

from dbapp.models import Data

class DataForm(ModelForm):
	class Meta:
		model = Data
		fields = ['Familiya', 'Imya', 'Otchestvo', 'gr', 'IP', 'host', 'edit_date']

@login_required
def ip_list(request,
	template_name='dbapp/ip_list.html'):
	ips = Data.objects.all()
	query = request.GET.get('query')
	if query:
		ips = ips.filter(
			Q(Familiya__icontains=query) | Q(Imya__icontains=query) | Q(Otchestvo__icontains=query) | Q(gr__icontains=query) | Q(IP__icontains=query) | Q(host__icontains=query)
			)
	alldata = {}
	alldata['object_list'] = ips

	return render(request, template_name, alldata)

@login_required
def ip_create(request,
	template_name='dbapp/ip_form.html'):
	form = DataForm(request.POST or None)
	if form.is_valid():
		form.save()
		return redirect('ip_list')
	return render(request, template_name, {'form':form})

@login_required
def ip_update(request, pk,
	template_name='dbapp/ip_form.html'):
	ips = get_object_or_404(Data, pk=pk)
	form = DataForm(request.POST or None, instance=ips)
	if form.is_valid():
		form.save()
		return redirect('ip_list')
	return render(request, template_name, {'form':form})

@login_required
def ip_delete(request, pk,
	template_name='dbapp/ip_confirm_delete.html'):
	ips = get_object_or_404(Data, pk=pk)
	if request.method=='POST':
		ips.delete()
		return redirect('ip_list')
	return render(request, template_name, {'object':ips})