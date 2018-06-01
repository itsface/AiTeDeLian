from django.core.management.base import BaseCommand, CommandError
from user.models import models


class Command(BaseCommand):
    help = '刷新所有缓存'

    # 必须实现的方法
    def handle(self, *args, **options):
        from django.core.cache import cache
        cache.clear()