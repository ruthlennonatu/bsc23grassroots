from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
)
from django.utils.translation import gettext_lazy as _


########################################################################################################################
# THE CODE BETWEEN THE HASHES IS NOT BEING USED, BUT IS KEPT FOR REFERENCE, THE CODE BELLOW THIS BLOCK IS THE CURRENT CODE
class Person(models.Model):
    """
    Django Model: Person

    This class defines a Django model for representing a person, with various attributes such as userID, username, password, name, phone, and address.

    Model Fields:
    - 'userID': An integer field serving as the primary key for identifying a person uniquely.
    - 'username': A character field representing the person's username with a maximum length of 255 characters.
    - 'password': A character field representing the person's password with a maximum length of 255 characters.
    - 'name': A character field representing the person's name with a maximum length of 255 characters.
    - 'phone': A character field representing the person's phone number with a maximum length of 255 characters.
    - 'address': A text field representing the person's address.

    Usage:
    - Include this model in a Django app to represent persons in the database.
    - Customize the fields based on the specific requirements of the person entity.

    Example:
        class Person(models.Model):
            userID = models.IntegerField(primary_key=True)
            username = models.CharField(max_length=255)
            password = models.CharField(max_length=255)
            name = models.CharField(max_length=255)
            phone = models.CharField(max_length=255)
            address = models.TextField()
    """
    userID = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.TextField()


def viewProfile(self):
    """
        Placeholder function for viewing a profile.

        This function currently has no specific implementation and should be customized
        based on the requirements of the profile viewing functionality.

        Usage:
        - Implement the necessary logic within the function to handle profile viewing.
        - Utilize the attributes of the instance (self) to retrieve and display profile information.

        Example:
            class ExampleClass:
                # ... (other class members)

                def viewProfile(self):
                    # Implement logic to retrieve and display the profile information.
                    # Example: return f"Profile for {self.username} - Name: {self.name}, Phone: {self.phone}"
    """
    pass



class Customer(Person):
    """
    Customer Class

    This class represents a customer, extending the 'Person' class. It introduces a method
    'applyForGrant' that is currently a placeholder with no specific implementation.

    Class Hierarchy:
    - The 'Customer' class inherits from the 'Person' class, capturing the attributes and
      behaviors of a person.

    Methods:
    - 'applyForGrant(self)': Placeholder method for handling the customer's application for a grant.
      - Implement the necessary logic within this function to process grant applications.

    Usage:
    - Utilize this class to create instances representing customers in the system.
    - Extend or override methods as needed to customize the behavior of the 'Customer' class.

    Example:
        class Customer(Person):
            def applyForGrant(self):
                # Implement logic to handle the customer's grant application.
                # Example: return "Grant application submitted successfully."
    """
    def applyForGrant(self):
        """
            Apply for Grant Function

            This function, 'applyForGrant', is a placeholder for handling the application process for a grant.
            It is currently incomplete and requires specific implementation.

            Function:
            - 'applyForGrant(self)': Placeholder function for submitting an application for a grant.
              - Implement the necessary logic within this function to process and handle grant applications.

            Usage:
            - Utilize this function within an instance of the relevant class to initiate the application process for a grant.
            - Customize the logic within 'applyForGrant' based on the specific requirements for applying for a grant.

            Example:
                class GrantApplicant:
                    # ... (other class members)

                    def applyForGrant(self):
                        # Implement logic to handle the application for a grant.
                        # Example: return "Grant application submitted successfully."
            """
        pass


class Admin(Person):
    """
       Admin Class

       This class represents an administrator, extending the 'Person' class. It introduces a method
       'viewApplications' that is currently a placeholder with no specific implementation.

       Class Hierarchy:
       - The 'Admin' class inherits from the 'Person' class, capturing the attributes and
         behaviors of a person.

       Methods:
       - 'viewApplications(self)': Placeholder method for an administrator to view applications.
         - Implement the necessary logic within this function to retrieve and display applications.

       Usage:
       - Utilize this class to create instances representing administrators in the system.
       - Extend or override methods as needed to customize the behavior of the 'Admin' class.

       Example:
           class Admin(Person):
               def viewApplications(self):
                   # Implement logic to retrieve and display applications.
                   # Example: return "List of applications: ..."
       """
    def viewApplications(self):
        """
           View Applications Function

           This function, 'viewApplications', is a placeholder for handling the viewing process of applications.
           It is currently incomplete and requires specific implementation.

           Function:
           - 'viewApplications(self)': Placeholder function for retrieving and displaying a list of applications.
             - Implement the necessary logic within this function to retrieve and present information about applications.

           Usage:
           - Utilize this function within an instance of the relevant class to initiate the process of viewing applications.
           - Customize the logic within 'viewApplications' based on the specific requirements for viewing applications.

           Example:
               class ApplicationViewer:
                   # ... (other class members)

                   def viewApplications(self):
                       # Implement logic to retrieve and display a list of applications.
                       # Example: return "List of applications: ..."
           """
        pass

    def editApplication(self):
        """
            Admin Class Method: editApplication

            This method, 'editApplication', is part of the 'Admin' class, representing an administrator.
            Currently, it is a placeholder with no specific implementation.

            Method:
            - 'editApplication(self)': Placeholder method for an administrator to edit an existing application.
              - Implement the necessary logic within this function to modify the details of an application.

            Usage:
            - Utilize this method within an instance of the 'Admin' class to handle the editing of applications.
            - Customize the logic within 'editApplication' based on the specific requirements for application editing.

            Example:
                class Admin(Person):
                    def editApplication(self):
                        # Implement logic to edit the details of an application.
                        # Example: return "Application edited successfully."
            """
        pass

    def viewCustomer(self):
        """
            Admin Class Method: viewCustomer

            This method, 'viewCustomer', is part of the 'Admin' class, representing an administrator.
            Currently, it is a placeholder with no specific implementation.

            Method:
            - 'viewCustomer(self)': Placeholder method for an administrator to view customer details.
              - Implement the necessary logic within this function to retrieve and display customer information.

            Usage:
            - Utilize this method within an instance of the 'Admin' class to handle the viewing of customer details.
            - Customize the logic within 'viewCustomer' based on the specific requirements for customer information retrieval.

            Example:
                class Admin(Person):
                    def viewCustomer(self):
                        # Implement logic to retrieve and display customer details.
                        # Example: return "Customer details: ..."
            """
        pass


########################################################################################################################
# THIS IS THE MODELS USED IN THE CURRENT CODE
class UserManager(BaseUserManager):
    """
        Custom user manager for creating regular users and superusers.
        This manager is associated with the custom User model.
        The customer user model is a safer way to save user credentials.
        """
    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        :param email: The email address of the user.
        :param password: The password of the user.
        :param extra_fields: Extra fields to be saved with the user.
        :return: The created user object.
        """

        def create_user(self, email, password=None, **extra_fields):
            if not email:
                raise ValueError('The Email field must be set')
            email = self.normalize_email(email)
            user = self.model(email=email, **extra_fields)
            user.set_password(password)
            user.save(using=self._db)
            return user

    def create_superuser(self, email, password=None, **extra_fields):
        """
        Create and save a regular user with the given email and password.

        :param email: The email address of the user.
        :param password: The password for the user.
        :param extra_fields: Additional fields for the user.
        :return: The created User object.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if not extra_fields.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True.')
        if not extra_fields.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, password, **extra_fields)


# Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model that uses email as the unique identifier for authentication.

    This model replaces the default Django User model and includes additional
    fields like first_name, last_name, phone, and address.
    """
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True)
    address = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
        related_name="%(app_label)s_%(class)s_groups",
        related_query_name="%(app_label)s_%(class)ss",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        help_text=_('Specific permissions for this user.'),
        related_name="%(app_label)s_%(class)s_user_permissions",
        related_query_name="%(app_label)s_%(class)ss",
    )

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        """
        :return: a string representation of the user, typically the user's email address.
        """
        return self.email


class Grant(models.Model):
    """
        Django Model: Grant

        This class defines a Django model for representing grants, with various attributes such as
        grantID, grantName, grantAmount, and description.

        Model Fields:
        - 'grantID': An integer field serving as the primary key for identifying a grant uniquely.
        - 'grantName': A character field representing the name of the grant with a maximum length of 255 characters.
        - 'grantAmount': A float field representing the amount of the grant.
        - 'description': A text field providing a detailed description of the grant.

        Methods:
        - 'viewApplications(self)': Placeholder method for viewing grant applications.
          - Implement the necessary logic within this function to retrieve and display grant applications.

        Usage:
        - Include this model in a Django app to represent grants in the database.
        - Customize the fields and methods based on the specific requirements of the grant entity.

        Example:
            class Grant(models.Model):
                grantID = models.IntegerField(primary_key=True)
                grantName = models.CharField(max_length=255)
                grantAmount = models.FloatField()
                description = models.TextField()

                def viewApplications(self):
                    # Implement logic to retrieve and display grant applications.
                    # Example: return "List of grant applications: ..."
        """
    grantID = models.IntegerField(primary_key=True)
    grantName = models.CharField(max_length=255)
    grantAmount = models.FloatField()
    description = models.TextField()

    def viewApplications(self):
        """
           View Applications Function

           This function, 'viewApplications', is a placeholder for handling the viewing process of applications.
           It is currently incomplete and requires specific implementation.

           Function:
           - 'viewApplications(self)': Placeholder function for retrieving and displaying a list of applications.
             - Implement the necessary logic within this function to retrieve and present information about applications.

           Usage:
           - Utilize this function within an instance of the relevant class to initiate the process of viewing applications.
           - Customize the logic within 'viewApplications' based on the specific requirements for viewing applications.

           Example:
               class ApplicationViewer:
                   # ... (other class members)

                   def viewApplications(self):
                       # Implement logic to retrieve and display a list of applications.
                       # Example: return "List of applications: ..."
           """
        pass


class SpecialAward(models.Model):
    """
        Django Model: SpecialAward

        This class defines a Django model for representing special awards, with various attributes such as
        awardID, awardName, description, eligibility, detail, and status.

        Model Fields:
        - 'awardID': An integer field serving as the primary key for identifying a special award uniquely.
        - 'awardName': A character field representing the name of the special award with a maximum length of 255 characters.
        - 'description': A text field providing a detailed description of the special award.
        - 'eligibility': A character field representing the eligibility criteria for the special award with a maximum length of 255 characters.
        - 'detail': A text field providing additional details about the special award.
        - 'status': A character field representing the status of the special award with a maximum length of 255 characters.

        Methods:
        - 'applyForSpecial(self)': Placeholder method for applying for a special award.
          - Implement the necessary logic within this function to process special award applications.

        Usage:
        - Include this model in a Django app to represent special awards in the database.
        - Customize the fields and methods based on the specific requirements of the special award entity.

        Example:
            class SpecialAward(models.Model):
                awardID = models.IntegerField(primary_key=True)
                awardName = models.CharField(max_length=255)
                description = models.TextField()
                eligibility = models.CharField(max_length=255)
                detail = models.TextField()
                status = models.CharField(max_length=255)

                def applyForSpecial(self):
                    # Implement logic to handle the application for a special award.
                    # Example: return "Special award application submitted successfully."
        """
    awardID = models.IntegerField(primary_key=True)
    awardName = models.CharField(max_length=255)
    description = models.TextField()
    eligibility = models.CharField(max_length=255)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def applyForSpecial(self):
        """
            Apply for Special Award Function

            This function, 'applyForSpecial', is a placeholder for handling the application process for a special award.
            It is currently incomplete and requires specific implementation.

            Function:
            - 'applyForSpecial(self)': Placeholder function for submitting an application for a special award.
              - Implement the necessary logic within this function to process and handle special award applications.

            Usage:
            - Utilize this function within an instance of the relevant class to initiate the application process for a special award.
            - Customize the logic within 'applyForSpecial' based on the specific requirements for applying for a special award.

            Example:
                class SpecialAwardApplicant:
                    # ... (other class members)

                    def applyForSpecial(self):
                        # Implement logic to handle the application for a special award.
                        # Example: return "Special award application submitted successfully."
            """
        pass


class Application(models.Model):
    """
        Django Model: Application

        This class defines a Django model for representing grant applications, with various attributes such as
        appID, applicant, grant, award, detail, and status.

        Model Fields:
        - 'appID': An integer field serving as the primary key for identifying a grant application uniquely.
        - 'applicant': A foreign key relationship with the 'Customer' model, representing the applicant.
        - 'grant': A foreign key relationship with the 'Grant' model, representing the grant being applied for.
        - 'award': A foreign key relationship with the 'SpecialAward' model, representing any special award associated with the application (nullable).
        - 'detail': A text field providing additional details about the grant application.
        - 'status': A character field representing the status of the grant application with a maximum length of 255 characters.

        Methods:
        - 'submitApplication(self)': Placeholder method for submitting a grant application.
          - Implement the necessary logic within this function to process grant applications.

        Usage:
        - Include this model in a Django app to represent grant applications in the database.
        - Customize the fields and methods based on the specific requirements of the grant application entity.

        Example:
            class Application(models.Model):
                appID = models.IntegerField(primary_key=True)
                applicant = models.ForeignKey(Customer, on_delete=models.CASCADE)
                grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
                award = models.ForeignKey(SpecialAward, on_delete=models.CASCADE, null=True, blank=True)
                detail = models.TextField()
                status = models.CharField(max_length=255)

                def submitApplication(self):
                    # Implement logic to handle the submission of a grant application.
                    # Example: return "Grant application submitted successfully."
        """
    appID = models.IntegerField(primary_key=True)
    applicant = models.ForeignKey(Customer, on_delete=models.CASCADE)
    grant = models.ForeignKey(Grant, on_delete=models.CASCADE)
    # Assuming the Award referenced here is the SpecialAward model
    award = models.ForeignKey(SpecialAward, on_delete=models.CASCADE, null=True, blank=True)
    detail = models.TextField()
    status = models.CharField(max_length=255)

    def submitApplication(self):
        """
            Application Model Method: submitApplication

            This method, 'submitApplication', is part of the 'Application' model, representing a grant application.
            Currently, it is a placeholder with no specific implementation.

            Method:
            - 'submitApplication(self)': Placeholder method for submitting a grant application.
              - Implement the necessary logic within this function to process and handle the submission of grant applications.

            Usage:
            - Utilize this method within an instance of the 'Application' model to handle the submission of grant applications.
            - Customize the logic within 'submitApplication' based on the specific requirements for processing grant applications.

            Example:
                class Application(models.Model):
                    # ... (other model fields)

                    def submitApplication(self):
                        # Implement logic to handle the submission of a grant application.
                        # Example: return "Grant application submitted successfully."
            """
        pass

    def viewStatus(self):
        """
            Application Model Method: viewStatus

            This method, 'viewStatus', is part of the 'Application' model, representing a grant application.
            Currently, it is a placeholder with no specific implementation.

            Method:
            - 'viewStatus(self)': Placeholder method for viewing the status of a grant application.
              - Implement the necessary logic within this function to retrieve and display the status of grant applications.

            Usage:
            - Utilize this method within an instance of the 'Application' model to handle the viewing of grant application status.
            - Customize the logic within 'viewStatus' based on the specific requirements for displaying the status of grant applications.

            Example:
                class Application(models.Model):
                    # ... (other model fields)

                    def viewStatus(self):
                        # Implement logic to retrieve and display the status of a grant application.
                        # Example: return "Status of the grant application: ..."
            """
        pass

# Create your models here.
