from django.db import models

class Person(models.Model):
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()

    def viewProfile(self):
        pass

class Customer(Person):
    def applyForGrant(self):
        pass

class Admin(Person):
    def viewApplications(self):
        pass

    def editApplication(self):
        pass

    def viewCustomer(self):
        pass

class Grant(models.Model):
    grantID = models.IntegerField(primary_key=True)
    grantName = models.CharField(max_length=255)
    grantAmount = models.FloatField()
    description = models.TextField()

    def viewApplications(self):
        pass

class SpecialAward(models.Model):
    awardID = models.IntegerField(primary_key=True)
    awardName = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def applyForSpecial(self):
        pass

class Application(models.Model):
    appID = models.IntegerField(primary_key=True)
    applicant = models.ForeignKey(Customer, on_delete=models.CASCADE)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    # Assuming the Award referenced here is the SpecialAward model
    award = models.ForeignKey(SpecialAward, on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def submitApplication(self):
        pass

    def viewStatus(self):
        pass

# Create your models here.

