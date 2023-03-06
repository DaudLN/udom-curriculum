import io
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

# from reportlab.pdfbase import pdfmetrics
from reportlab.lib import enums
from reportlab.lib.pagesizes import letter

from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image, Spacer

# Create your views here.

from .models import Program


class ProgramListView(ListView):
    model = Program
    template_name = "program_list.html"
    context_object_name = "program_list"
    paginate_by = 4
    number_in_page = Program.objects.all().count()


def program_detail(request, program):
    program = get_object_or_404(Program, slug=program)
    return render(request, "program_detail.html", {"program": program})


def search_program(request):

    if request.method == "POST":
        search = request.POST["search"]
        programs = Program.objects.filter(name__icontains=search)

        return JsonResponse({"programs": list(programs.values())})
        # return render(request, "program_search.html", {"programs": programs})
    else:
        return render(request, "program_search.html", {})


# def generate_pdf(request, program):
#     # Get the Program object
#     program = get_object_or_404(Program, slug=program)

#     # Create the PDF object
#     response = HttpResponse(content_type="application/pdf")
#     response["Content-Disposition"] = f'attachment; filename="{program.name}.pdf"'
#     buffer = io.BytesIO()
#     doc = SimpleDocTemplate(buffer, pagesize=letter)
#     styles = getSampleStyleSheet()

#     # Create a list of paragraphs to draw on the PDF
#     elements = []
#     university_head = "<a href='https://www.udom.ac.tz'>THE UNIVERSITY OF DODOMA </a>"
#     university_head_style = getSampleStyleSheet()["Heading1"]
#     university_head_style.alignment = enums.TA_CENTER
#     college_head = f"{program.college}"
#     college_head_style = getSampleStyleSheet()["Heading2"]
#     college_head_style.alignment = enums.TA_CENTER
#     paragrap_style = getSampleStyleSheet()["Normal"]
#     paragrap_style.fontSize = 11
#     elements.append(Paragraph(university_head, style=university_head_style))
#     elements.append(Paragraph(college_head, style=college_head_style))
#     elements.append(
#         Image(
#             "https://imgs.search.brave.com/md-s9-5eWujI9NxzCGJxGDSugTfBhqJvsUdta4Xk5kc/rs:fit:319:320:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzYxLzc0/L2Y4LzYxNzRmOGVi/MzQ3MDlmNGQwNWRm/ZWU3NTZiYzA5MTkz/LnBuZw",
#             width=100,
#             height=100,
#         )
#     )
#     elements.append(
#         Paragraph(
#             f"The University of Dodoma Program curriculum", style=college_head_style
#         )
#     )
#     elements.append(Paragraph(f"{program.name}", style=college_head_style))
#     elements.append(Paragraph(f"Description", styles["Heading3"]))
#     elements.append(Paragraph(f"{program.description}", style=paragrap_style))
#     elements.append(Paragraph(f"Program tuition fee", styles["Heading3"]))
#     elements.append(Paragraph(f"Tsh {program.fee}", style=paragrap_style))
#     elements.append(Paragraph(f"College", styles["Heading3"]))
#     elements.append(Paragraph(f"{program.college}", style=paragrap_style))
#     if program.knowledge:
#         elements.append(Paragraph("Knowledge obtained", styles["Heading3"]))

#         elements.append(Paragraph(f"{program.knowledge}", style=paragrap_style))
#     else:
#         pass

#     if program.skills:
#         elements.append(Paragraph("Skills", styles["Heading3"]))
#         elements.append(Paragraph(f"{program.skills}", style=paragrap_style))
#     else:
#         pass
#     elements.append(Paragraph("Competences", styles["Heading3"]))
#     elements.append(Paragraph(f"{program.competences}", style=paragrap_style))
#     elements.append(Paragraph("Special requirements", styles["Heading3"]))
#     elements.append(Paragraph(f"{program.special_requirements}", style=paragrap_style))
#     elements.append(Paragraph("Field of work", styles["Heading3"]))
#     elements.append(Paragraph(f"{program.fields_of_work}", style=paragrap_style))

#     # Draw the PDF
#     doc.build(elements)

#     # Get the value of the BytesIO buffer and write it to the response.
#     response.write(buffer.getvalue())
#     buffer.close()
#     return response


def generate_pdf(request, program):
    # Get the Program object
    program = get_object_or_404(Program, slug=program)

    # Create the PDF object
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = f'attachment; filename="{program.name}.pdf"'
    buffer = io.BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Define custom styles
    university_head_style = ParagraphStyle(
        name="university_head_style",
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=18,
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    program_head_style = ParagraphStyle(
        name="program_head_style",
        fontName="Helvetica-Bold",
        fontSize=14,
        leading=16,
        alignment=TA_CENTER,
        spaceAfter=12,
    )
    section_head_style = ParagraphStyle(
        name="section_head_style",
        fontName="Helvetica-Bold",
        fontSize=12,
        leading=14,
        spaceBefore=8,
        spaceAfter=4,
    )
    paragraph_style = ParagraphStyle(
        name="paragraph_style",
        fontName="Helvetica",
        fontSize=10,
        leading=12,
        spaceAfter=8,
    )

    # Create a list of paragraphs to draw on the PDF
    elements = []
    university_head = "<a href='https://www.udom.ac.tz'>THE UNIVERSITY OF DODOMA </a>"
    elements.append(Paragraph(university_head, style=university_head_style))
    elements.append(Spacer(1, 12))
    elements.append(
        Image(
            "https://imgs.search.brave.com/md-s9-5eWujI9NxzCGJxGDSugTfBhqJvsUdta4Xk5kc/rs:fit:319:320:1/g:ce/aHR0cHM6Ly9pLnBp/bmltZy5jb20vb3Jp/Z2luYWxzLzYxLzc0/L2Y4LzYxNzRmOGVi/MzQ3MDlmNGQwNWRm/ZWU3NTZiYzA5MTkz/LnBuZw",
            width=75,
            height=75,
        )
    )
    elements.append(Spacer(1, 12))
    program_head = f"{program.name} ({program.college})"
    elements.append(Paragraph(program_head, style=program_head_style))
    elements.append(Spacer(1, 24))
    if program.description:
        elements.append(Paragraph("Program Description", style=section_head_style))
        elements.append(Paragraph(program.description, style=paragraph_style))
        elements.append(Spacer(1, 12))
    if program.years_of_study:
        elements.append(Paragraph("Years of Study", style=section_head_style))
        elements.append(
            Paragraph(f"{program.years_of_study} years", style=paragraph_style)
        )
        elements.append(Spacer(1, 12))
    if program.fee:
        elements.append(Paragraph("Tuition Fee", style=section_head_style))
        elements.append(Paragraph(f"Tsh {program.fee:,}", style=paragraph_style))
        elements.append(Spacer(1, 12))
    if program.knowledge:
        elements.append(Paragraph("Knowledge Obtained", style=section_head_style))
        elements.append(Paragraph(program.knowledge, style=paragraph_style))
        elements.append(Spacer(1, 12))

    # Build the PDF document
    doc.build(elements)

    # Get the value of the BytesIO buffer and write it to the response
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)

    return response
