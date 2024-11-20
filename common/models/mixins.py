from crum import get_current_user
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models

from config import settings


class DateMixin(models.Model):

    created_at = models.DateField(
        _("создан"), null=True, blank=False, auto_now=False, auto_now_add=False)
    updated_at = models.DateField(
        _("обновлён"), null=True, blank=False, auto_now=False, auto_now_add=False)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk and not self.created_at:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(DateMixin, self).save(*args, **kwargs)


class InfoMixin(DateMixin):
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                                   "created_%(app_label)s_%(class)s", verbose_name=_("Created by"), null=True)
    updated_by = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL,
                                   "updated_%(app_label)s_%(class)s", verbose_name=_("Updated by"), null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user
        self.updated_by = user
        super().save(*args, **kwargs)
