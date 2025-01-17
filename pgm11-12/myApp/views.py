import csv
from django.http import HttpResponse
from django.template.loader import get_template 
from xhtml2pdf import pisa
from .models import Book

def export_books_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="books.csv"' 
    writer = csv.writer(response)
    writer.writerow(['Title', 'Author', 'Publication Date'])
    books = Book.objects.all().values_list('title', 'author', 'publication_date')
    for book in books:
        writer.writerow(book) 
    return response

def export_books_pdf(request):
    books = Book.objects.all() #Step-04: Create a views.py file in your books app and define the views for generating CSV and PDF files

    template_path = 'book_list.html' 
    context = {'books': books}
    response = HttpResponse(content_type='application/pdf') 
    response['Content-Disposition'] = 'attachment; filename="books.pdf"' 
    template = get_template(template_path)
    html = template.render(context) 
    pisa_status = pisa.CreatePDF(html, dest=response) 
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response