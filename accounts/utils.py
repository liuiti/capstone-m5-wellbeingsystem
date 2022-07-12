from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def _create_user(
        self, email, password, is_staff, is_superuser, is_worker=False, **extra_fields
    ):

        if not email:
            raise ValueError("email precisa ser passado")

        email = self.normalize_email(email)

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            is_worker=is_worker,
            **extra_fields
        )

        user.set_password(password)

        user.save(using=self.db)

        return user

    def create_user(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=False,
            **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(
            email=email,
            password=password,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
