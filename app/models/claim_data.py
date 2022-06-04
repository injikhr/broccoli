from django.db import models
from django.contrib.auth import get_user_model
from .base_data import BaseData

class ClaimData(BaseData, models.Model):
    """
    INHERITED:
    @PRIMARY    id          BIGINT      20 
    @FOREIGN    owner       VARCHAR     72 
    @FIELD      title       VARCHAR     128 
    @FIELD      content     TEXT        65535 
    @FIELD      last_update DATETIME    6
    """                                

    # @FIELD @OVERRIDE
    # Use JSON type instead of string
    content = models.JSONField()

    # VC Issuer
    issuer = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="claim"
    )

    """
    VALUE   STATUS      DESCRIPTION
    1       PENDING     Wating for issuing VC
    2       ACCEPTED    VC issued
    3       REJECTED    VC not issued
    """
    status = models.SmallIntegerField(
        default=1,
    )

    # Encrypted VC
    encrypted_vc = models.TextField(
        max_length=65535,
        blank=True,
        null=True,
        default=None
    )