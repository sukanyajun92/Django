__author__ = 'suksubra'
from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight


class chassisInfo(models.Model):
    TIME = models.CharField(max_length=200)
    AVERAGE_PACKET_SIZE = models.CharField(max_length=200)
    CPU_0_5MIN_AVG_SESSMGR_CPUS = models.CharField(max_length=200)
    EDR_SEC = models.CharField(max_length=200)
    SESSMGR_ACTIVE_CARDS = models.CharField(max_length=200)
    THROUGHPUT_KPPS = models.CharField(max_length=200)
    THROUGHPUT_MBPS = models.CharField(max_length=200)
    TOTAL_CALLS_CONNECTED_SEC = models.CharField(max_length=200)
    TOTAL_CALLS_DISCONNECTED_SEC = models.CharField(max_length=200)
    TOTAL_SUBSCRIBERS = models.CharField(max_length=200)
    UDR_SEC = models.CharField(max_length=200)

    class Meta:
        ordering = ('TIME',)

    def __str__(self):
        return self.TIME




