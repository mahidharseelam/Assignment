from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import *
# Create your views here.
@csrf_exempt
def contest_input(request):
    if request.method=='POST':
        contest_id=request.POST.get('contest_id')
        hacker_id=request.POST.get('hacker_id')
        name=request.POST.get('name')
        contest_in=Contests(contest_id=contest_id,hacker_id=hacker_id,name=name)
        contest_in.save()
        return render(request, 'input_contests.html')
    else:
        return render(request,'input_contests.html')
@csrf_exempt
def colleges_input(request):
    if request.method=='POST':
        college_id=request.POST.get('college_id')
        contest_id=request.POST.get('contest_id')
        colleges_in=Colleges(college_id=college_id,contest_id=contest_id)
        colleges_in.save()
        return render(request, 'input_colleges.html')
    else:
        return render(request,'input_colleges.html')

@csrf_exempt
def challenges_input(request):
    if request.method=='POST':
        challenge_id=request.POST.get('challenge_id')
        college_id=request.POST.get('college_id')
        challenges_in=Challenges(challenge_id=challenge_id,college_id=college_id)
        challenges_in.save()
        return render(request, 'input_challenges.html')
    else:
        return render(request,'input_challenges.html')

@csrf_exempt
def view_stats_input(request):
    if request.method=='POST':
        challenge_id=request.POST.get('challenge_id')
        total_views=request.POST.get('total_views')
        total_unique_views=request.POST.get('total_unique_views')
        view_stats_in=View_Stats(challenge_id=challenge_id,total_views=total_views,total_unique_views=total_unique_views)
        view_stats_in.save()
        return render(request, 'input_view_stats.html')
    else:
        return render(request,'input_view_stats.html')

@csrf_exempt
def submission_stats(request):
    if request.method=='POST':
        challenge_id = request.POST.get('challenge_id')
        total_submission=request.POST.get('total_submission')
        total_accepted_submissions=request.POST.get('total_accepted_submissions')
        submission_stats_in=Submission_Stats(challenge_id=challenge_id,total_submission=total_submission,total_accepted_submissions=total_accepted_submissions)
        submission_stats_in.save()
        return render(request, 'input_submission_stats.html')
    else:
        return render(request,'input_submission_stats.html')
