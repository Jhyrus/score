from pipeline.storage import PipelineMixin
from django.contrib.staticfiles.storage import CachedFilesMixin
from django.contrib.staticfiles.storage import StaticFilesStorage


class PipelineCachedStorage(PipelineMixin, CachedFilesMixin, StaticFilesStorage):
    pass
