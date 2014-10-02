# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models.pluginmodel import CMSPlugin


class SnippetPlugin(CMSPlugin):
    content = models.TextField(_('Content'))
