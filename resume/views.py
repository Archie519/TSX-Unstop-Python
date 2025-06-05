from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.
def home(request):
    return render (request,"home.html")
def about(request):
    return render(request,"about.html")
def projects(request):
    projects_show=[
        {
         "title":"Online JobPortal",
         "path":"https://tse3.mm.bing.net/th?id=OIP.sK2yMDu-OUFu7TNw_DVoxAAAAA&pid=Api&P=0&h=180",
         "desc": """A platform that bridges the gap between job seekers and recruiters.
It allows users to register, create resumes, apply for jobs, and receive updates.
Recruiters can post job openings, browse resumes, and shortlist candidates.
The system offers filters by location, job type, and experience.
It also provides application tracking and notification systems.
Secure authentication and user roles make it scalable and reliable.
Built with Django and Bootstrap for responsive UI."""
        },
        {
            "title":"Restaurant Management",
            "path":"https://tse3.mm.bing.net/th?id=OIP.D6wcjp3OgjooMWuHkaEfuwHaFj&pid=Api&P=0&h=180",
             "desc":"""A web-based system for managing restaurant operations digitally.
Includes modules for menu management, table booking, and billing.
Staff can handle orders, update menu items, and generate bills.
Customers can book tables and place online orders.
Real-time dashboard for inventory and sales tracking.
Designed to improve efficiency and reduce manual errors.
Built using Django, HTML/CSS, and SQLite database."""
        }
    ]
    return render(request,"projects.html",{"project_show": projects_show})

def experience(request):
    experience=[
        {"company":"ABC",
         "position":"python developer",
         "tenure": "Jan 2023 – May 2024",
 "summary": """Worked as a backend Python developer responsible for building RESTful APIs using Django and Django REST Framework.
Developed scalable and secure web applications, integrating third-party services and payment gateways.
Designed and optimized relational databases using  MySQL.
Collaborated with frontend developers to ensure smooth API integration and seamless user experience.
Maintained code versioning and collaboration using Git and GitHub, following best branching strategies.
Participated in Agile sprints, daily standups, and code reviews to maintain high code quality.
Created technical documentation, automated deployment scripts, and conducted unit testing.
Continuously improved system performance and contributed innovative solutions for faster delivery."""
         }
    ]
    return render (request,"experience.html",{"experience":experience})


def certificate(request):
    return render(request,"certificate.html")

def contact(request):
    return render(request,"contact.html")

def resume(request):
    resume_path="myapp/RESUME.pdf"
    resume_path=staticfiles_storage.path(resume_path)
    if staticfiles_storage.exists(resume_path):
        with open(resume_path,"rb") as resume_file:
            response=HttpResponse(resume_file.read(),content_type="application/pdf")
            response['Content-Disposition']='attachment';filename="RESUME.pdf"
            return response
    else:
        return HttpResponse("resume not found",status=404)