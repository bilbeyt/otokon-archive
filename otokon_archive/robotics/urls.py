from django.conf.urls import url
from robotics.views import SeasonListView, CompetitionListView, RobotListView, \
    RoboticsPressDetailView, RoboticsSponsorsDetailView, RobotDetailView, \
    RoboticsPressListView, RoboticsSponsorsListView, SeasonHomeView

urlpatterns = [
    url(r'^$', SeasonListView.as_view(), name="seasons"),
    url(r'^(?P<season>[-_\w]+)/$', SeasonHomeView.as_view(), name="season_home"),
    url(r'^(?P<season>[-_\w]+)/competition/$', CompetitionListView.as_view(), name="competition_list"),
    url(r'^(?P<season>[-_\w]+)/sponsorship/$', RoboticsSponsorsListView.as_view(), name="robotics_sponsorship"),
    url(r'^(?P<season>[-_\w]+)/press/$', RoboticsPressListView.as_view(), name="robotics_press"),
    url(r'^(?P<season>[-_\w]+)/competition/(?P<competition>[-_\w]+)/$',
        RobotListView.as_view(),
        name="robot_list"
    ),
    url(r'^(?P<season>[-_\w]+)/competition/(?P<competition>[-_\w]+)/(?P<slug>[-_\w]+)',
        RobotDetailView.as_view(),
        name="robot_detail"
    ),
    url(r'^(?P<season>[-_\w]+)/sponsorship/(?P<slug>[-_\w]+)',
        RoboticsSponsorsDetailView.as_view(),
        name="robotics_sponsor_detail"
    ),
    url(r'^(?P<season>[-_\w]+)/press/(?P<slug>[-_\w]+)/$',
        RoboticsPressDetailView.as_view(),
        name="robotics_press_detail"
    )
]