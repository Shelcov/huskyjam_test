from django.db import models
from django.contrib.auth.models import User
from tests.models import *


class FinishTest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=None)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, default=None, related_name='finished')
    count_true_answer = models.IntegerField(blank=True, null=True, default=0)
    count_false_answer = models.IntegerField(blank=True, null=True, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = 'Пройденный тест'
        verbose_name_plural = 'Пройденные тесты'

    def __str__(self):
        return "%s : %s" % (self.user.username, self.test.name)

    def percent(self):
        return self.count_true_answer / (self.count_true_answer + self.count_false_answer) * 100


