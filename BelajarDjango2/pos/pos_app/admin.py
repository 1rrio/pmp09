from django.contrib import admin
from pos_app.models import User, TableResto, StatusModel,Category,MenuResto
from import_export.admin import ImportExportModelAdmin

@admin.register(StatusModel)
class StatusAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass

@admin.register(MenuResto)
class MenuAdmin(ImportExportModelAdmin):
    pass