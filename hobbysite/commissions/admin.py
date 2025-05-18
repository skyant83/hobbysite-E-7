from django.contrib import admin

from .models import Commission, Job, JobApplication


class JobInline(admin.TabularInline):
    model = Job
    verbose_name = 'Job'
    verbose_name_plural = 'Jobs'


class JobApplicationInline(admin.TabularInline):
    model = JobApplication
    verbose_name = 'Job Application'
    verbose_name_plural = 'Job Applications'


class JobAdmin(admin.ModelAdmin):
    model = Job
    inlines = [JobApplicationInline,]
    fieldsets = (
        ('Job Details', {
            'fields': (
                'status',
                'role',
                'manpower_required',
            ),
        }),
    )


class CommissionAdmin(admin.ModelAdmin):
    model = Commission
    inlines = [JobInline,]
    search_fields = ('title', 'status')
    list_display = ('title', 'author', 'status', 'created_on', 'updated_on')
    list_filter = ('title', 'author', 'status', 'created_on', 'updated_on')
    fieldsets = (
        ('Commission Details', {
            'fields': (
                ('title', 'author',),
                'description',
            ),
        }),
    )


class JobApplicationAdmin(admin.ModelAdmin):
    model = JobApplication


admin.site.register(Commission, CommissionAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(JobApplication, JobApplicationAdmin)
