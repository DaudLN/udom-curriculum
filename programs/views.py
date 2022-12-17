import io
from django.http import HttpResponse, FileResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from reportlab.pdfgen import canvas
# from reportlab.pdfbase import pdfmetrics
from reportlab.lib import enums
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from .models import Program
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image
# Create your views here.


class ProgramListView(ListView):
    model = Program
    template_name = 'program_list.html'
    context_object_name = 'program_list'
    paginate_by = 4
    number_in_page = Program.objects.all().count()


class ProgramDetailView(DetailView):
    model = Program
    template_name: str = 'program_detail.html'

    def generate_pdf(request):
        programs = Program.objects.all()
        # Create a file-like buffer to receive PDF data.
        buffer = io.BytesIO()

        # Create the PDF object, using the buffer as its "file."
        p = canvas.Canvas(buffer, pagesize=letter)

        textobj = p.beginText()
        textobj.setTextOrigin(inch, inch)
        textobj.setFont("Helvetica", 14)
        # Draw things on the PDF. Here's where the PDF generation happens.
        # See the ReportLab documentation for the full list of functionality.
        lines = []
        for program in programs:
            lines.append(program.name)
            lines.append(program.college)
            lines.append(program.description)
            lines.append(str(program.fee))

        for line in lines:
            textobj.textLine(line)

        # Close the PDF object cleanly, and we're done.
        p.drawText(textobj)
        p.showPage()
        buffer.seek(0)
        # FileResponse sets the Content-Disposition header so that browsers
        # present the option to save the file.
        # buffer.seek(0)
        return FileResponse(buffer,
                            as_attachment=True,
                            filename='programs.pdf')


def search_program(request):

    if request.method == "POST":
        search = request.POST['search']
        programs = Program.objects.filter(name__icontains=search)
        return render(request, "program_search.html", {"programs": programs})
    else:
        return render(request, "program_search.html", {})



def program_pdf(request):
    programs = Program.objects.all()
    #Create bystream buffer
    buff = io.BytesIO()
    #Create canvas
    canv = canvas.Canvas(buff, pagesize=letter, bottomup=0)
    #create text object
    textobj = canv.beginText()
    textobj.setTextOrigin(inch, inch)
    textobj.setFont("Helvetica", 14)

    # Add some lines

    lines = []
    for program in programs:
        lines.append(program.name)
        lines.append(program.college)
        lines.append(program.description)
        lines.append(program.years_of_study)

    for line in lines:
        textobj.textLine(line)
    #finish up

    canv.drawText(textobj)
    canv.showPage()
    buff.seek(0)

    return FileResponse(buff, as_attachment=True, filename="program.pdf")


def generate_pdf(request, pk):
    # Get the Program object
    program = get_object_or_404(Program, pk=pk)

    # Create the PDF object
    response = HttpResponse(content_type='application/pdf')
    response[
        'Content-Disposition'] = f'attachment; filename="{program.name}.pdf"'
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create a list of paragraphs to draw on the PDF
    elements = []
    university_head = "<a href='https://www.udom.ac.tz'>THE UNIVERSITY OF DODOMA </a>"
    university_head_style = getSampleStyleSheet()['Heading1']
    university_head_style.alignment = enums.TA_CENTER
    college_head = f"{program.college}"
    college_head_style = getSampleStyleSheet()['Heading2']
    college_head_style.alignment = enums.TA_CENTER
    paragrap_style = getSampleStyleSheet()['Normal']
    paragrap_style.fontSize = 11
    elements.append(Paragraph(university_head, style=university_head_style))
    elements.append(Paragraph(college_head, style=college_head_style))
    elements.append(
        Image(
            "https://imgs.search.brave.com/md-s9-5eWujI9NxzCGJxGDSugTfBhqJvsUdta4Xk5kc/rs:fit:319:320:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzYxLzc0/L2Y4LzYxNzRmOGVi/MzQ3MDlmNGQwNWRm/ZWU3NTZiYzA5MTkz/LnBuZw",
            width=100,
            height=100))
    elements.append(
        Paragraph(f"The University of Dodoma Program curriculum",
                  style=college_head_style))
    elements.append(Paragraph(f"{program.name}", style=college_head_style))
    elements.append(Paragraph(f"Description", styles['Heading3']))
    elements.append(Paragraph(f"{program.description}", style=paragrap_style))
    elements.append(Paragraph(f"Program tuition fee", styles['Heading3']))
    elements.append(Paragraph(f"Tsh {program.fee}", style=paragrap_style))
    elements.append(Paragraph(f"College", styles["Heading3"]))
    elements.append(Paragraph(f"{program.college}", style=paragrap_style))
    if program.knowledge:
        elements.append(Paragraph("Knowledge obtained", styles["Heading3"]))

        elements.append(Paragraph(f"{program.knowledge}",
                                  style=paragrap_style))
    else:
        pass

    if program.skills:
        elements.append(Paragraph("Skills", styles["Heading3"]))
        elements.append(Paragraph(f"{program.skills}", style=paragrap_style))
    else:
        pass
    if program.competences:
        elements.append(Paragraph("Competences", styles["Heading3"]))
        elements.append(Paragraph(f"{program.competences}", style=paragrap_style))
    else:
        pass
    elements.append(Paragraph("Special requirements", styles["Heading3"]))
    elements.append(
        Paragraph(f"{program.special_requirements}", style=paragrap_style))
    elements.append(Paragraph("Field of work", styles["Heading3"]))
    elements.append(
        Paragraph(f"{program.fields_of_work}", style=paragrap_style))

    # Draw the PDF
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response.
    response.write(buffer.getvalue())
    buffer.close()
    return response
