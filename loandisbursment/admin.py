from django.contrib import admin
from .models import Contributions, Loans, WholeAccounts

admin.site.register(Contributions)
admin.site.register(Loans)
admin.site.register(WholeAccounts)