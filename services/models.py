from django.db import models
 
 
STATUS_CHOICES = [
 
    ('Pending', 'Pending'),
 
    ('Payment Pending', 'Payment Pending'),
 
    ('In Progress', 'In Progress'),
 
    ('Completed', 'Completed'),
]
 
 
# ITR MODEL
class ITRRequest(models.Model):
 
    full_name = models.CharField(max_length=100)
 
    email = models.EmailField()
 
    phone = models.CharField(max_length=15)
 
    message = models.TextField()
 
    pan_card = models.FileField(upload_to='itr_documents/')
 
    aadhaar_card = models.FileField(upload_to='itr_documents/')
 
    
 
    bank_statement = models.FileField(upload_to='itr_documents/')
 
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.full_name
 
 
# GST MODEL
class GSTRequest(models.Model):
 
    full_name = models.CharField(max_length=100)
 
    email = models.EmailField()
 
    phone = models.CharField(max_length=15)
 
    message = models.TextField()
 
    gst_certificate = models.FileField(upload_to='gst_documents/')
 
    sales_report = models.FileField(upload_to='gst_documents/')
 
    purchase_report = models.FileField(upload_to='gst_documents/')
 
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.full_name
 
 
# TDS MODEL
class TDSRequest(models.Model):
 
    full_name = models.CharField(max_length=100)
 
    email = models.EmailField()
 
    phone = models.CharField(max_length=15)
 
    message = models.TextField()
 
    pan_card = models.FileField(upload_to='tds_documents/')
 
    tds_details = models.FileField(upload_to='tds_documents/')
 
    salary_sheet = models.FileField(upload_to='tds_documents/')
 
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.full_name
 
 
# BOOKKEEPING MODEL
class BookkeepingRequest(models.Model):
 
    full_name = models.CharField(max_length=100)
 
    email = models.EmailField()
 
    phone = models.CharField(max_length=15)
 
    message = models.TextField()
 
    bank_statement = models.FileField(upload_to='bookkeeping_documents/')
 
    expense_records = models.FileField(upload_to='bookkeeping_documents/')
 
    sales_records = models.FileField(upload_to='bookkeeping_documents/')
 
    status = models.CharField(
        max_length=30,
        choices=STATUS_CHOICES,
        default='Pending'
    )
 
    created_at = models.DateTimeField(auto_now_add=True)
 
    def __str__(self):
        return self.full_name
    
# =========================
# ITR ADDITIONAL DOCUMENTS
# =========================
 
class ITRAdditionalDocument(models.Model):
 
    itr_request = models.ForeignKey(
        ITRRequest,
        on_delete=models.CASCADE,
        related_name='additional_documents'
    )
 
    document = models.FileField(
        upload_to='itr_additional_documents/'
    )
 
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
 
    def __str__(self):
 
        return self.document.name
 
 
# =========================
# GST ADDITIONAL DOCUMENTS
# =========================
 
class GSTAdditionalDocument(models.Model):
 
    gst_request = models.ForeignKey(
        GSTRequest,
        on_delete=models.CASCADE,
        related_name='additional_documents'
    )
 
    document = models.FileField(
        upload_to='gst_additional_documents/'
    )
 
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
 
    def __str__(self):
 
        return self.document.name
 
 
# =========================
# TDS ADDITIONAL DOCUMENTS
# =========================
 
class TDSAdditionalDocument(models.Model):
 
    tds_request = models.ForeignKey(
        TDSRequest,
        on_delete=models.CASCADE,
        related_name='additional_documents'
    )
 
    document = models.FileField(
        upload_to='tds_additional_documents/'
    )
 
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
 
    def __str__(self):
 
        return self.document.name
 
 
# =========================
# BOOKKEEPING ADDITIONAL DOCUMENTS
# =========================
 
class BookkeepingAdditionalDocument(models.Model):
 
    bookkeeping_request = models.ForeignKey(
        BookkeepingRequest,
        on_delete=models.CASCADE,
        related_name='additional_documents'
    )
 
    document = models.FileField(
        upload_to='bookkeeping_additional_documents/'
    )
 
    uploaded_at = models.DateTimeField(
        auto_now_add=True
    )
 
    def __str__(self):
 
        return self.document.name