from django.conf.urls import patterns, include, url, handler404, handler500
from django.contrib import admin
from views import index, contact, student_list, student_detail
from feedbacks.views import FeedbackView

handler404 = 'pybursa.views.page_not_found_custom'    
handler500 = 'pybursa.views.page_error_found_custom'

urlpatterns = patterns('',
    # Examples:
    url(r'^$', index, name='index'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^feedback/$', FeedbackView.as_view(), name='feedback'),
    url(r'^student_list/$', student_list, name='student_list'),
    url(r'^student_detail/$', student_detail, name='student_detail'),
    url(r'^quadratic/', include('quadratic.urls'), name='results'),
    url(r'^courses/', include('courses.urls', namespace="courses")),
    url(r'^students/', include('students.urls', namespace="students")),
    url(r'^coaches/', include('coaches.urls', namespace="coaches")),
    # url(r'^blog/', include('blog.urls')),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
)
