from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse
from sponsorship.models import Category, Organization, Company


class OrganizationListView(ListView):
    model = Organization
    template_name = "sponsorship/organization_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(OrganizationListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(OrganizationListView, self).get_context_data(**kwargs)
        context["organization_list"] = Organization.objects.all()
        return context


class CategoryBaseTemplateView(TemplateView):
    template_name = "sponsorship/company_filter.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryBaseTemplateView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryBaseTemplateView, self).get_context_data(**kwargs)
        context["organization"] = self.kwargs.get("organization")
        return context


class SponsorListView(ListView):
    model = Company
    template_name = "sponsorship/sponsor_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(SponsorListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(SponsorListView, self).get_context_data(**kwargs)
        organization = self.kwargs.get("organization")
        context["category_list"] = Category.objects.filter(sponsorship=True, organization__slug=organization).order_by("order")
        return context


class CompanyListView(ListView):
    model = Company
    template_name = "sponsorship/category_list.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(CompanyListView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CompanyListView, self).get_context_data(**kwargs)
        organization = self.kwargs.get("organization")
        context["category_list"] = Category.objects.filter(organization__slug=organization).exclude(sponsorship=True)
        return context


class CompanyDetailView(DetailView):
    model = Company
    template_name = "sponsorship/company_detail.html"


def custom_login(request, *args, **kwargs):
    if request.user.is_authenticated():
        raise PermissionDenied
    else:
        return login(request, *args, **kwargs)


def custom_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))
