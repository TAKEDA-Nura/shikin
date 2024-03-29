from django.db import models


class Erad(models.Model):
    erad_key = models.CharField(
        "e-Rad公募ID", max_length=7, unique=True, blank=True, null=True)
    erad_url = models.URLField("e-Rad公募情報URL", blank=True, null=True)
    url = models.URLField("URL", blank=True, null=True)
    publishing_date = models.DateField("公開日")
    funding_agency = models.CharField("配分機関", max_length=200)
    call_for_applications = models.CharField("公募名", max_length=200)
    application_unit = models.CharField("応募単位", max_length=200)
    approved_institution = models.CharField("機関承認の有無", max_length=200)
    opening_date = models.DateField("受付開始日")
    closing_date = models.DateField("受付終了日")

    def __str__(self):
        return self.funding_agency + "／" + self.call_for_applications
