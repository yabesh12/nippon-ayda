from django.contrib import admin
from django.core.files.storage import get_storage_class
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin
from import_export.fields import Field
from register.models import RegisterForm, State, College, upload


class RegisterImportExport(resources.ModelResource):
    states = fields.Field(column_name='state', attribute='states',
                          widget=widgets.ForeignKeyWidget(RegisterForm, 'state'))
    College = fields.Field(column_name='College', attribute='College',
                           widget=widgets.ForeignKeyWidget(RegisterForm, 'College'))

    class Meta:
        model = RegisterForm
        import_id_fields = ['uuid']
        exclude = ('id', 'Date_time')


class RegisterFormAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = RegisterImportExport
    search_fields = ('Phone',)


admin.site.register(RegisterForm, RegisterFormAdmin)


class StateImportExport(resources.ModelResource):
    class Meta:
        model = State
        import_id_fields = ['state']
        exclude = ('id',)


class StateAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = StateImportExport


admin.site.register(State, StateAdmin)


class CollegeImportExport(resources.ModelResource):
    class Meta:
        model = College
        import_id_fields = ['College']
        exclude = ('id',)


class CollegeAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = CollegeImportExport


admin.site.register(College, CollegeAdmin)


class UploadImportExport(resources.ModelResource):
    uuid = fields.Field(column_name='uuid', attribute='uuid',
                        widget=widgets.ForeignKeyWidget(upload, 'uuid'))
    name = fields.Field(column_name='Name', attribute='uuid',
                        widget=widgets.ForeignKeyWidget(upload, 'Name'))
    e_mail = fields.Field(column_name='e-mail', attribute='uuid',
                          widget=widgets.ForeignKeyWidget(upload, 'E_Mail'))
    phone = fields.Field(column_name='mobile_number', attribute='uuid',
                         widget=widgets.ForeignKeyWidget(upload, 'Phone'))
    state = fields.Field(column_name='state', attribute='uuid',
                         widget=widgets.ForeignKeyWidget(upload, 'states'))
    study_year = fields.Field(column_name='study_year', attribute='uuid',
                              widget=widgets.ForeignKeyWidget(upload, 'Study_Year'))
    college = fields.Field(column_name='college', attribute='uuid',
                           widget=widgets.ForeignKeyWidget(upload, 'College'))
    year_of_graduation = fields.Field(column_name='year_of_graduation', attribute='uuid',
                                      widget=widgets.ForeignKeyWidget(upload, 'Year_of_Graduation'))
    category = fields.Field(column_name='category', attribute='uuid',
                            widget=widgets.ForeignKeyWidget(upload, 'Category'))

    form_1 = Field(column_name='form_1_url')
    form_2 = Field(column_name='form_2_url')
    form_3 = Field(column_name='form_3_url')
    form_4 = Field(column_name='form_4_url')
    form_5 = Field(column_name='form_5_url')

    class Meta:
        model = upload
        import_id_fields = ['uuid']
        exclude = ('id',)

    def dehydrate_form_1(self, obj):
        media_storage = get_storage_class()()
        return media_storage.url(name=obj.form_1.name)

    def dehydrate_form_2(self, obj):
        media_storage = get_storage_class()()
        if not obj.form_2:
            return "No File"
        return media_storage.url(name=obj.form_2.name)

    def dehydrate_form_3(self, obj):
        media_storage = get_storage_class()()
        if not obj.form_3:
            return "No File"
        return media_storage.url(name=obj.form_3.name)

    def dehydrate_form_4(self, obj):
        media_storage = get_storage_class()()
        if not obj.form_4:
            return "No File"
        return media_storage.url(name=obj.form_4.name)

    def dehydrate_form_5(self, obj):
        media_storage = get_storage_class()()
        if not obj.form_5:
            return "No File"
        return media_storage.url(name=obj.form_5.name)


class UploadAdmin(ImportExportMixin, admin.ModelAdmin):
    resource_class = UploadImportExport
    search_fields = ('uuid',)


admin.site.register(upload, UploadAdmin)
