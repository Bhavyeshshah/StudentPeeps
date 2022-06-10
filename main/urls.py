
from django.contrib import admin
from django.urls import path
from . import views

admin.site.site_header = " login to Student Peeps"
admin.site.site_title = "Dashboard"
admin.site.index_title = "Welcome to Student Peeps Dashboard"

urlpatterns = [
    path('',views.home,name="Home"),
    path('about/',views.about,name="About"),
    path('blog/',views.blog,name="Blog"),
    path('verification-message/',views.verificationmsg,name="Verificationmsg"),
    path('upload-message/',views.uploadmsg,name="Uploadmsg"),
    path('contactus/',views.contactus,name="ContactUs"),

    path('whole-truth-food/',views.wtf,name='Wtf'),
    path('student-discount-whole-truth-food/',views.codewtf,name='CodeWtf'),

    path('avni-by-giva/',views.avni,name='Avni'),
    path('student-discount-avni/',views.codeavni,name='CodeAvni'),

    path('naagin/',views.naagin,name='Naagin'),
    path('student-discount-naagin/',views.codenaagin,name='CodeNaagin'),

    path('pee-safe/',views.peesafe,name='PEESAFE'),
    path('student-discount-pee-safe/',views.codepeesafe,name='CodePEESAFE'),

    path('propshop/',views.propshop,name='Propshop'),
    path('student-discount-propshop/',views.codepropshop,name='CodePropshop'),

    path('trib/',views.trib,name='TRIB'),
    path('student-discount-trib/',views.codetrib,name='CodeTRIB'),

    path('to-be-honest/',views.tbh,name='TBH'),
    path('student-discount-to-be-honest/',views.codetbh,name='CodeTBH'),

    path('unlu-class/',views.unlu,name='Unlu'),
    path('student-discount-unlu-class/',views.codeunlu,name='CodeUnlu'),

    path('unlu-shoutout/',views.unlu2,name='Unlu2'),
    path('student-discount-unlu-shoutout/',views.codeunlu2,name='CodeUnlu2'),

    path('yes-done/',views.yesdone,name='YesDone'),
    path('student-discount-yes-done/',views.codeyesdone,name='CodeYesDone')
    
]
