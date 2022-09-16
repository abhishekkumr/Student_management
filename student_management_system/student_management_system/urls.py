
from django.contrib import admin
from django.template.defaulttags import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


from .import views,hod_views,Staff_views,student_views

###################################################################################################################################

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

  #Login page
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('dologout',views.dologout,name='logout'),

 #profile_update
    path('Profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),


###################################################################################################################################

 #this is Hod panel url
    path('hod/home',hod_views.Home,name='hod_home'),
    path('hod/student/add',hod_views.ADD_STUDENT,name='add_student'),
    path('hod/student/view',hod_views.VIEW_STUDENT,name='view student'),

    path('hod/student/edit/<str:id>',hod_views.EDIT_STUDENT,name='edit student'),
    path('hod/student/update',hod_views.UPDATE_STUDENT,name='update student'),

    path('hod/student/delete/<str:admin>',hod_views.DELETE_STUDENT,name='delete student'),

  # this part of URL show the staff adding urls and functions.
    path('hod/staff/add',hod_views.ADD_STAFF,name='add staff'),
    path('hod/staff/view',hod_views.VIEW_STAFF,name='view staff'),
    path('hod/staff/edit/<str:id>',hod_views.EDIT_STAFF,name='edit staff'),
    path('hod/staff/update',hod_views.UPDATE_STAFF,name='update staff'),
    path('hod/staff/delete/<str:admin>',hod_views.DELETE_STAFF,name='delete staff'),


 #this part of URL will help to add the courses in the course-panel.
    path('hod/course/Add',hod_views.ADD_COURSE,name='add course'),
    path('hod/course/View',hod_views.VIEW_COURSE,name='view course'),

    path('hod/course/edit/<str:id>',hod_views.EDIT_COURSE,name='edit course'),
    path('hod/course/update',hod_views.UPDATE_COURSE,name='update course'),

    path('hod/course/delete/<str:id>',hod_views.DELETE_COURSE,name='delete course'),

# this part of URL will help us to add/view subject in the dashboard
    path('hod/Subject/add',hod_views.ADD_SUBJECT,name='add subject'),
    path('hod/subject/view',hod_views.VIEW_SUBJECT,name='view subject'),
    path('hod/subject/edit/<str:id>',hod_views.EDIT_SUBJECT,name='edit subject'),
    path('hod/subject/update',hod_views.UPDATE_SUBJECT,name='update subject'),
    path('hod/subject/delete/<str:id>',hod_views.DELETE_SUBJECT,name='delete subject'),


# this part of URL will show how to add sessions in the data and how to remove it.
    path('hod/session/add',hod_views.ADD_SESSION,name='add session'),
    path('hod/session/view',hod_views.VIEW_SESSION,name='view session'),

    path('hod/session/edit/<str:id>',hod_views.EDIT_SESSION,name='edit session'),
    path('hod/session/update',hod_views.UPDATE_SESSION,name='update session'),

    path('hod/session/delete/<str:id>',hod_views.DELETE_SESSION,name='delete session'),


# this part of URL will show how HOD send notifications to staff and students.
    path('hod/staff/Send_Notification',hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('hod/staff/save_notification',hod_views.SAVE_STAFF_NOTIFICATION,name='save_staff_notification'),

    path('hod/student/send_notification',hod_views.STUDENT_NOTIFICATION_SEND,name='send_student_notification'),
    path('hod/student/save_notification',hod_views.SAVE_STUDENT_NOTIFICATION,name='save_student_notification'),

# this part of URL will show how to add sessions in the data and how to remove it.
    path('hod/staff/leave_view',hod_views.STAFF_LEAVE_VIEW,name='staff_leave'),

# this part of URL show's how HOD reply and see student Feedbacks.
    path('hod/student/feedback',hod_views.STUDENT_FEEDBACK,name='getting_student_feedback'),
    path('hod/student/feedback/reply',hod_views.FEEDBACK_REPLY_STUDENT,name='feedback_reply_student'),

#this url is for approval and rejection of applied leaves from staff by HOD
    path('hod/staff/approve_leave/<str:id>',hod_views.STAFF_APPROVE_LEAVE,name='staff_approve_leave'),
    path('hod/staff/rejected_leave/<str:id>', hod_views.STAFF_REJECTED_LEAVE, name='staff_rejected_leave'),

# this part of URL show's how HOD replys the feedback and save the feedback.
    path('hod/staff/feedback',hod_views.STAFF_FEEDBACK,name='staff_feedback_reply'),
    path('hod/staff/feedback/save',hod_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_reply_save'),

# this part of URL show's how HOD View,approve and disapprove the leaves of student.
    path('hod/student/applied/Leave',hod_views.STUDENT_LEAVE_STATUS,name='student_leave_View'),
    path('hod/student/approved_leave/<str:id>',hod_views.STUDENT_LEAVE_APPROVAL,name='student_leave_approved'),
    path('hod/student/disapproved_leave/<str:id>',hod_views.STUDENT_LEAVE_DISAPPROVED,name='student_leave_disapproved'),

# this part of URL show's how HOD View attendance.
    path('hod/view/attendance',hod_views.VIEW_ATTENDANCE,name='hod_view_attendance'),



###################################################################################################################################


#this is the part of staff panel form where teachers are operating.
    path('staff/home',Staff_views.HOME,name='staff_home'),

# this part of URL show's how Staff view notiications and mark them read.
    path('staff/notifications',Staff_views.NOTIFICATOINS,name='notifications'),
    path('staff/mark_as_done/<str:status>',Staff_views.NOTIFICATION_MARK,name='notification_mark'),

# this part of URL show's how Staff apply for the leave and it saves in leave columb.
    path('staff/apply_leave',Staff_views.STAFF_APPLY_LEAVES,name='staff_apply_leave'),
    path('staff/apply_leave_save',Staff_views.APPLY_LEAVE_SAVE,name='apply_leave_save'),

# this part of URL show's how Staff apply for the Feedback and it saves in Feedback columb.
    path('staff/feedback',Staff_views.STAFF_FEEDBACK,name='staff_feedback'),
    path('staff/feedback/save',Staff_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

# this part of URL show's how Staff take attendance.
    path('staff/take/attendance',Staff_views.TAKING_ATTENDANCE,name='student_attendance'),
    path('staff/save/attendance',Staff_views.SAVE_ATTENDANCE,name='save_attendance'),
    path('staff/view_attendance',Staff_views.VIEW_ATTENDANCE,name='staff_view_attendance'),

# this part of URL show's how Staff can publish the attendance.
    path('staff/result/add',Staff_views.ADD_RESULT,name='adding_result'),

#this part of URL show's how result is linking with database
        path('staff/result/save',Staff_views.SAVE_RESULT,name='saving-result'),




###################################################################################################################################



#this is the part of Student panel
    path('student/home',student_views.HOME,name='student_home'),


# this part of URL show's how Student see the Notifications and mark them as read.
    path('student/notification',student_views.STUDENT_NOTIFICATION,name='student_notification'),
    path('student/mark_as_done/<str:status>',student_views.NOTIFICATION_MARK, name='student_notification_mark'),


# this part of URL show's how student send the feedback and how it got saved
    path('student/feedback',student_views.STUDENT_FEEDBACK,name='student_feedback'),
    path('student/feedback/save',student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

# this part of URL show's how student apply for leaves.
    path('student/leave/apply',student_views.APPLY_LEAVE,name='Student_leave_application'),
    path('student/leave/save',student_views.STUDENT_LEAVE_SAVE,name='student_leave_save'),
    path('student/view/attendance',student_views.VIEW_ATTENDANCE,name='view_attendance'),

# this part of URL show's how student apply for leaves.
    path('student/view/result',student_views.VIEW_RESULT,name='view_result'),






] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
