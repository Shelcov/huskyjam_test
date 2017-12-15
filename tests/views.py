from collections import OrderedDict

from django.shortcuts import render, render_to_response
from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
from django.http import HttpResponseForbidden
from django.views.generic.list import ListView
from formtools.wizard.views import SessionWizardView

from tests.forms import QuestionForm
from users.models import *


class TestListView(LoginRequiredMixin, ListView):
    template_name = 'tests/test_list.html'

    def get_queryset(self):
        return Test.objects.filter(is_active=True).exclude(finished__user=self.request.user)


class FinishedTestListView(ListView, LoginRequiredMixin):
    template_name = 'tests/finished_test_list.html'

    def get_queryset(self):
        return FinishTest.objects.filter(user=self.request.user)


class TestWizardView(DetailView, SessionWizardView, LoginRequiredMixin):
    form_list = [QuestionForm]
    template_name = 'single_test.html'

    def get_queryset(self):
        return Test.objects.filter(is_active=True)\
            .exclude(pk__in=FinishTest.objects.filter(user=self.request.user))

    def get_form_kwargs(self, step=None):
        return {'question': self.instance_dict[step]}

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            self.object = self.get_object()
            forms = OrderedDict()
            instance_dict = {}
            for question in self.object.question_set.all():
                forms[str(question.pk)] = QuestionForm
                instance_dict[str(question.pk)] = question
            self.instance_dict = instance_dict
            self.form_list = forms
        return super(TestWizardView, self).dispatch(request, *args, **kwargs)

    def done(self, form_list, **kwargs):
        count_true_answer = 0
        count_false_answer = 0
        for form in form_list:
            answer = set(form.question.answer_set.filter(is_true=True).values_list('pk', flat=True))
            user_answer = set(map(int, form.cleaned_data['answers']))
            if answer == user_answer:
                count_true_answer += 1
            else:
                count_false_answer += 1
        finished_test = FinishTest(user=self.request.user, test=self.object, count_true_answer=count_true_answer,
                                   count_false_answer=count_false_answer)
        finished_test.save()
        return render(self.request, 'tests/done.html', {'finished_test': finished_test})

    def render_goto_step(self, goto_step, **kwargs):
        raise HttpResponseForbidden()


