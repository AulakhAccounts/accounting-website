from django.contrib import admin
from .models import *
 
 
# =========================
# INLINE MODELS
# =========================
 
class ITRAdditionalDocumentInline(admin.TabularInline):
 
    model = ITRAdditionalDocument
 
    extra = 0
 
    fields = ['document']
 
 
class GSTAdditionalDocumentInline(admin.TabularInline):
 
    model = GSTAdditionalDocument
 
    extra = 0
 
    fields = ['document']
 
 
class TDSAdditionalDocumentInline(admin.TabularInline):
 
    model = TDSAdditionalDocument
 
    extra = 0
 
    fields = ['document']
 
 
class BookkeepingAdditionalDocumentInline(admin.TabularInline):
 
    model = BookkeepingAdditionalDocument
 
    extra = 0
 
    fields = ['document']
 
 
# =========================
# ITR ADMIN
# =========================
 
@admin.register(ITRRequest)
class ITRRequestAdmin(admin.ModelAdmin):
 
    list_display = (
        'full_name',
        'phone',
        'status',
        'created_at'
    )
 
    list_filter = (
        'status',
        'created_at'
    )
 
    search_fields = (
        'full_name',
        'phone',
        'email'
    )
 
    inlines = [
        ITRAdditionalDocumentInline
    ]
 
 
# =========================
# GST ADMIN
# =========================
 
@admin.register(GSTRequest)
class GSTRequestAdmin(admin.ModelAdmin):
 
    list_display = (
        'full_name',
        'phone',
        'status',
        'created_at'
    )
 
    list_filter = (
        'status',
        'created_at'
    )
 
    search_fields = (
        'full_name',
        'phone',
        'email'
    )
 
    inlines = [
        GSTAdditionalDocumentInline
    ]
 
 
# =========================
# TDS ADMIN
# =========================
 
@admin.register(TDSRequest)
class TDSRequestAdmin(admin.ModelAdmin):
 
    list_display = (
        'full_name',
        'phone',
        'status',
        'created_at'
    )
 
    list_filter = (
        'status',
        'created_at'
    )
 
    search_fields = (
        'full_name',
        'phone',
        'email'
    )
 
    inlines = [
        TDSAdditionalDocumentInline
    ]
 
 
# =========================
# BOOKKEEPING ADMIN
# =========================
 
@admin.register(BookkeepingRequest)
class BookkeepingRequestAdmin(admin.ModelAdmin):
 
    list_display = (
        'full_name',
        'phone',
        'status',
        'created_at'
    )
 
    list_filter = (
        'status',
        'created_at'
    )
 
    search_fields = (
        'full_name',
        'phone',
        'email'
    )
 
    inlines = [
        BookkeepingAdditionalDocumentInline
    ]