from django.db import models


class Person(models.Model):
    """Defines a Person Class Properties and Functions"""
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()

    def view_profile(self):
        """Allows a Person to view their details"""
        pass


class Customer(Person):
    """Defines a Customer Class Properties and Functions"""
    def apply_for_grant(self):
        """Creates a grant application for the Customer"""
        pass


class Admin(Person):
    """Admin functions to view and edit Customer grant applications"""
    def view_applications(self):
        """Returns all grant applications"""
        pass

    def edit_application(self):
        """Edits details of the grant application"""
        pass

    def view_customer(self):
        """Allows Admin to view a Customer"""
        pass


class Grant(models.Model):
    grantID = models.IntegerField(primary_key=True)
    grantName = models.CharField(max_length=255)
    grantAmount = models.FloatField()
    description = models.TextField()

    def view_applications(self):
        """View Grant application"""
        pass


class SpecialAward(models.Model):
    """Details of a special award"""
    awardID = models.IntegerField(primary_key=True)
    awardName = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def apply_for_special(self):
        """Create a special award application"""
        pass


class Application(models.Model):
    """Details of an application"""
    appID = models.IntegerField(primary_key=True)
    applicant = models.ForeignKey(Customer, on_delete=models.CASCADE)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    # Assuming the Award referenced here is the SpecialAward model
    award = models.ForeignKey(SpecialAward, on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def submit_application(self):
        """Submitting an Application"""
        pass

    def view_status(self):
        """Returns the Applications status"""
        pass

# Create your models here.
