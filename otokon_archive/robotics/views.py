from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from robotics.models import Season, Competition, Robot, RoboticsSponsors, RoboticsPress


class SeasonHomeView(TemplateView):
    template_name = "robotics/home.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SeasonHomeView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        slug = self.kwargs.get("season")
        context = dict()
        context["slug"] = slug
        return context


class SeasonListView(ListView):
    model = Season
    template_name = "robotics/season_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(SeasonListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = dict()
        context["seasons"] = Season.objects.all().order_by("-name")
        return context


class CompetitionListView(ListView):
    model = Competition
    template_name = "robotics/competition_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CompetitionListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        context = dict()
        context["competitions"] = Competition.objects.filter(season=season).order_by("name")
        return context


class RobotListView(ListView):
    model = Robot
    template_name = "robotics/robot_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RobotListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        competition_slug = self.kwargs.get("competition")
        competition = Competition.objects.get(slug=competition_slug)
        context = dict()
        context["robots"] = Robot.objects.filter(season=season, competition=competition).order_by("name")
        return context


class RoboticsSponsorsListView(ListView):
    model = RoboticsSponsors
    template_name = "robotics/sponsor_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RoboticsSponsorsListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        context = dict()
        context["sponsors"] = RoboticsSponsors.objects.filter(season=season)
        return context


class RoboticsPressListView(ListView):
    model = RoboticsPress
    template_name = "robotics/news_list.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RoboticsPressListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        context = dict()
        context["news_list"] = RoboticsPress.objects.filter(season=season).order_by("-created_at")
        return context


class RoboticsPressDetailView(DetailView):
    model = RoboticsPress
    template_name = "robotics/news_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RoboticsPressDetailView, self).dispatch(*args, **kwargs)

    def get_object(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        slug = self.kwargs.get("slug")
        obj = RoboticsPress.objects.get(slug=slug, season=season)
        return obj


class RoboticsSponsorsDetailView(DetailView):
    model = RoboticsPress
    template_name = "robotics/sponsors_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RoboticsSponsorsDetailView, self).dispatch(*args, **kwargs)

    def get_object(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        slug = self.kwargs.get("slug")
        obj = RoboticsSponsors.objects.get(slug=slug, season=season)
        return obj


class RobotDetailView(DetailView):
    model = Robot
    template_name = "robotics/robot_detail.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RobotDetailView, self).dispatch(*args, **kwargs)

    def get_object(self, **kwargs):
        season_slug = self.kwargs.get("season")
        season = Season.objects.get(slug=season_slug)
        competition_slug = self.kwargs.get("competition")
        slug = self.kwargs.get("slug")
        obj = Robot.objects.get(slug=slug, season=season, competition__slug=competition_slug)
        return obj