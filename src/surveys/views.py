from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import ModelForm
from surveys.models import Survey, Question, Choice

class SurveyForm(ModelForm):
    class Meta:
        model = Survey
        fields = ['title']

# Create your views here.
def survey_list(request, template_name='surveys/survey_list.html'):
    surveys = Survey.objects.all()
    data = {}
    data['object_list'] = surveys
    return render(request, template_name, data)

@login_required
def survey_create(request, template_name='surveys/survey_form.html'):
    form = SurveyForm(request.POST or None)
    if form.is_valid():
        
        survey = form.save(commit=False)
        print request.user, request.user.id
        survey.user = request.user
        survey.save()

        if 'add_question' in request.POST:
            return redirect('question_new', survey.id)
        else:
            return redirect('survey_list')

    return render(request, template_name, {'form':form})

def survey_update(request, pk, template_name='surveys/survey_form.html'):
    survey = get_object_or_404(Survey, pk=pk)
    form = SurveyForm(request.POST or None, instance=survey)
    if form.is_valid():
        form.save()
        return redirect('survey_list')
    return render(request, template_name, {'form':form})

def survey_delete(request, pk, template_name='surveys/survey_confirm_delete.html'):
    survey = get_object_or_404(Survey, pk=pk)    
    if request.method=='POST':
        survey.delete()
        return redirect('survey_list')
    return render(request, template_name, {'object':survey})    

def survey_view(request, pk, template_name='surveys/survey_view.html'):
    survey = get_object_or_404(Survey, pk=pk)
    questions = Question.objects.filter(survey=pk)
    return render(request, template_name, {'survey':survey, 'questions':questions})


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ['name']

def question_create(request, survey_id, template_name='questions/question_form.html'):
    survey = get_object_or_404(Survey, pk=survey_id)
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)
        question.survey = survey
        question.save()
        #save anwers
        # print(request.POST)
        choices = request.POST.getlist('choice')
        
        for choice in choices:
            choice_obj = Choice()
            choice_obj.question = question
            choice_obj.choice = choice
            choice_obj.save()

        # form.save()
        if 'add_another' in request.POST:
            return redirect('question_new', survey_id)
        else:
            return redirect('survey_view', survey_id)
    return render(request, template_name, {'form':form, 'survey':survey})

def question_update(request, survey_id, question_id, template_name='questions/question_form.html'):
    
    survey = get_object_or_404(Survey, pk=survey_id)
    question = get_object_or_404(Question, pk=question_id)

    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()

        choices = request.POST.getlist('choice')
        
        for choice in choices:
            choice_obj = Choice()
            choice_obj.question = question
            choice_obj.choice = choice
            choice_obj.save()


        if 'add_another' in request.POST:
            return redirect('question_new', survey_id)
        else:
            return redirect('survey_view', survey_id)
    return render(request, template_name, {'form':form, 'survey':survey})

def question_delete(request, survey_id, question_id, template_name='questions/question_confirm_delete.html'):
    question = get_object_or_404(Question, pk=question_id)    
    if request.method=='POST':
        question.delete()
        return redirect('survey_view', survey_id)
    return render(request, template_name, {'object':question})    

def question_view(request, survey_id, question_id, template_name='questions/question_view.html'):
    
    survey = get_object_or_404(Survey, pk=survey_id)
    question = get_object_or_404(Question, pk=question_id)
    choices = Choice.objects.filter(question=question_id)

    return render(request, template_name, {'question':question, 'choices':choices})