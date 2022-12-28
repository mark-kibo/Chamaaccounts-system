from django.db import models



class Contributions(models.Model):
    name=models.CharField(max_length=255)
    amount_contributed=models.CharField(max_length=255)
    date=models.DateField()

    def __str__(self):
        return self.name

class Loans(models.Model):
    name=models.ForeignKey(to=Contributions, on_delete=models.CASCADE)
    amount_loaned=models.CharField(max_length=255)
    expected_amount_to_be_paid = models.CharField(max_length=255)
    amount_paid=models.CharField(max_length=255)
    balance_carried_forward=models.CharField(max_length=255)
    date=models.DateField()


    def __str__(self):
        return str(self.name) + '' + self.balance_carried_forward

class WholeAccounts(models.Model):
    name=models.CharField(max_length=255)
    amount_contributed=models.CharField(max_length=255)
    date=models.DateField()
    amount_loaned=models.CharField(max_length=255)
    expected_amount_to_be_paid = models.CharField(max_length=255)
    amount_paid=models.CharField(max_length=255)
    balance_carried_forward=models.CharField(max_length=255)

    def __str__(self):
        return self.name