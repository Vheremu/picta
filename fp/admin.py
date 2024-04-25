from django.contrib import admin
from .models import Pop,Transaction,AccountBalance,ZipitWithdrawal,EcocashWithdrawal
# Register your models here.
admin.site.register(Pop)
admin.site.register(Transaction)
admin.site.register(AccountBalance)
admin.site.register(EcocashWithdrawal)
admin.site.register(ZipitWithdrawal)