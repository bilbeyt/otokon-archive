from django.conf.urls import url
from sponsorship.views import OrganizationListView, CategoryBaseTemplateView, \
    CompanyDetailView, CompanyListView, SponsorListView

urlpatterns = [
    url(r'^$', OrganizationListView.as_view(), name="organization_list"),
    url(r'^(?P<organization>[-_\w]+)/$',
        CategoryBaseTemplateView.as_view(),
        name="company_filter"),
    url(r'^(?P<organization>[-_\w]+)/all_companies/$',
        CompanyListView.as_view(),
        name="company_list"),
    url(r'^(?P<organization>[-_\w]+)/sponsors/$',
        SponsorListView.as_view(),
        name="sponsor_list"),
    url(r'^(?P<organization>[-_\w]+)/(?P<slug>[-_\w]+)/$',
        CompanyDetailView.as_view(),
        name="company_detail"),
]
