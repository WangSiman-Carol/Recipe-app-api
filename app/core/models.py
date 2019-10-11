from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, \
										PermissionsMixin

class  UserManager(BaseUserManager):
	
	def create_user(self, email, password=None, **extra_fields):  # **extra_fields makes the function flexible
		"""Create and save a new user"""
		if not email:
			raise ValueError('User must have an email address')
		user = self.model(email=self.normalize_email(email), **extra_fields)
		user.set_password(password)   # password should be encrypted instead of in a clear text
		user.save(using=self._db)

		return user		

	def create_superuser(self, email, password):
		"""create a new superuser"""
		user = self.create_user(email, password)
		user.is_superuser = True
		user.is_staff = True

		return user

class User(AbstractBaseUser, PermissionsMixin):
	"""Custom user model that supports using email instead of username"""
	email = models.EmailField(max_length=255, unique=True)   # unique means one email is responding to one user
	name = models.CharField(max_length=255)
	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	USERNAME_FIELD = 'email'



