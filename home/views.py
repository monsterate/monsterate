from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
import socket
import threading


import socket
from django.shortcuts import render

def index(request):
    data = {}
    try:
        if request.method == "POST":
            target_host = request.POST.get('dname1')
            start_port = int(request.POST.get('stport'))
            end_port = int(request.POST.get('enport'))
            results = []

            vulnerabilities = {
                
                21: "Potential FTP Vulnerability",
                22: "Potential SSH Vulnerability",
                23: "Potential Telnet Vulnerability",
                25: "Potential SMTP Vulnerability",
                53: "Potential DNS Vulnerability",
                80: "Potential Web Server Vulnerability",
                110: "Potential POP3 Vulnerability",
                143: "Potential IMAP Vulnerability",
                443: "Potential SSL/TLS Vulnerability",
                3389: "Potential Remote Desktop Protocol Vulnerability",
                8080: "Potential Proxy Server Vulnerability"
                
            }

            for port in range(start_port, end_port + 1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    client_socket.settimeout(1)
                    result = client_socket.connect_ex((target_host, port))
                    if result == 0:
                        print(f"Port {port} is open on {target_host}")
                        vulnerability = vulnerabilities.get(port, "No known vulnerability")
                        results.append({"port": port, "status": "Open", "vulnerability": vulnerability})

            data = {'output': results}
    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'index.html', context=data)

def details(request, port):
    # Add logic to fetch detailed information based on the port number
    vulnerability = {
        21: "Potential FTP Vulnerability",
        22: "Potential SSH Vulnerability",
        23: "Potential Telnet Vulnerability",
        25: "Potential SMTP Vulnerability",
        53: "Potential DNS Vulnerability",
        80: "https://www.cloudflare.com/learning/ddos/glossary/hypertext-transfer-protocol-http/#:~:text=The%20Hypertext%20Transfer%20Protocol%20(HTTP,of%20the%20network%20protocol%20stack.",
        110: "Potential POP3 Vulnerability",
        143: "Potential IMAP Vulnerability",
        443: "Potential SSL/TLS Vulnerability",
        3389: "Potential Remote Desktop Protocol Vulnerability",
        8080: "Potential Proxy Server Vulnerability"
        # Add more external links for other ports as needed
    }

    detail_info = vulnerability.get(port, "No details available for this port")

    return render(request, 'details.html', {'port': port, 'detail_info': detail_info})
    
def about(request):
    return render(request, 'about.html')

def service(request):
    return HttpResponse("this is service page!")

def contact(request):
    if (request.method == "POST"):
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        contact = Contact(email=email, comment=comment, date = datetime.today())
        contact.save()
    return render(request, 'contact.html')





"""
def index(request):
    data = {}
    try:
        if request.method == "POST":
            target_host = request.POST.get('dname1')
            start_port = int(request.POST.get('stport'))
            end_port = int(request.POST.get('enport'))
            results = []

            vulnerabilities = {
                
                21: "Potential FTP Vulnerability",
                22: "Potential SSH Vulnerability",
                23: "Potential Telnet Vulnerability",
                25: "Potential SMTP Vulnerability",
                53: "Potential DNS Vulnerability",
                80: "Potential Web Server Vulnerability",
                110: "Potential POP3 Vulnerability",
                143: "Potential IMAP Vulnerability",
                443: "Potential SSL/TLS Vulnerability",
                3389: "Potential Remote Desktop Protocol Vulnerability",
                8080: "Potential Proxy Server Vulnerability"
                
            }

            for port in range(start_port, end_port + 1):
                with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
                    client_socket.settimeout(1)
                    result = client_socket.connect_ex((target_host, port))
                    if result == 0:
                        print(f"Port {port} is open on {target_host}")
                        vulnerability = vulnerabilities.get(port, "No known vulnerability")
                        results.append({"port": port, "status": "Open", "vulnerability": vulnerability})

            data = {'output': results}
    except Exception as e:
        print(f"Error: {e}")

    return render(request, 'index.html', context=data)
"""