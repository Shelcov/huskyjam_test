from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=128, blank=True, null=False, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    name = models.CharField(max_length=128, blank=True, null=False, default=None)
    test = models.ForeignKey(Test, on_delete=models.CASCADE, null=True, default=None)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.name

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    name = models.CharField(max_length=128, blank=True, null=False, default=None)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True, default=None)
    is_active = models.BooleanField(default=True)
    is_true = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "%s" % self.id

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
