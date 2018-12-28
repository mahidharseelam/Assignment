from django.conf.urls import url
from . import views

urlpatterns = [
    url('contest/',views.contest_input),
    url('college/',views.colleges_input),
    url('challenges/',views.challenges_input),
    url('viewstats/',views.view_stats_input),
    url('submissionstats/',views.submission_stats),
]