from django.shortcuts import render, redirect
from django.contrib import messages
from work.models import Student_Notification,Student,Student_Feedback_Save,Student_leave,Subject,Attendance,Attendance_report,StudentResult


def HOME(request):
    return render(request,'student/home.html')


def STUDENT_NOTIFICATION(request):
    student = Student.objects.filter(admin = request.user.id)
    for i in student:
        student_id = i.id
        notification = Student_Notification.objects.filter(student_id = student_id)

        context = {
            'notification':notification,
        }
        return render(request,'student/notification.html',context)


def NOTIFICATION_MARK(request,status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('student_notification')


def STUDENT_FEEDBACK(request):
    student_id = Student.objects.get(admin = request.user.id)
    feedback_history = Student_Feedback_Save.objects.filter(student_id = student_id)

    context = {
        'feedback_history':feedback_history
    }
    return render(request,'student/student_feedback.html',context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')
        student = Student.objects.get(admin = request.user.id)
        feedbacks = Student_Feedback_Save(
            student_id = student,
            feedback = feedback,
            feedback_reply = ""
        )
        feedbacks.save()
    return redirect('student_feedback')


def APPLY_LEAVE(request):
    student = Student.objects.get(admin = request.user.id)
    student_leave_history = Student_leave.objects.filter(student_id = student)

    context = {
        'student_leave_history':student_leave_history
    }

    return render(request,'student/student_leave.html',context)


def STUDENT_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        leave_message = request.POST.get('leave_message')

        student_id = Student.objects.get(admin = request.user.id)

        student_leave = Student_leave (
            student_id = student_id,
            date = leave_date,
            message = leave_message,
        )
        student_leave.save()
        messages.success(request,'YOUR LEAVE APPLIED SUCCESSFULLY')
    return redirect('Student_leave_application')


def VIEW_ATTENDANCE(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course = student.course_id)
    action = request.GET.get('action')

    get_subject = None
    attendance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            get_subject = Subject.objects.get(id = subject_id)

            attendance_report = Attendance_report.objects.filter(student_id = student,attendance_id__subject_id = subject_id)

    context = {
        'subjects':subjects,
        'action':action,
        'get_subject':get_subject,
        'attendance_report':attendance_report,
    }
    return render(request,'student/view_attendance.html',context)


def VIEW_RESULT(request):
    mark = None
    student = Student.objects.get(admin = request.user.id)
    result = StudentResult.objects.filter(student_id = student)

    for i in result:
        assignment_mark = i.assignment_mark
        exam_mark = i.exam_marks

        mark = i.exam_marks + i.assignment_mark

    context = {
        'result':result,
        'mark':mark,
    }

    return render(request,'student/view_result.html',context)