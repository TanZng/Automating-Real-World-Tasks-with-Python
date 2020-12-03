#!/usr/bin/env python3
import reports
import os
import glob
import emails
from datetime import date

def main():
    today = date.today()
    title = 'Processed Updated on ' + today.strftime("%B %d, %Y")
    pdf_name = '/tmp/processed.pdf'
    paragraph = get_summary()
    reports.generate_report(pdf_name, title, paragraph)
    send_report(pdf_name)

def get_summary():
    PATH_TXT = 'supplier-data/descriptions/'
    summary = []
    for filename in glob.glob(PATH_TXT + "*.txt"):
        text = ""
        f = open(filename, 'r')
        text += "name: " + f.readline() + '<br/>'
        text += "weight: " + f.readline() + '<br/>'
        summary.append(text)
    return summary

def send_report(pdf_name):
    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email"
    message = emails.generate(sender, receiver, subject, body, pdf_name)
    emails.send(message)


if __name__ == "__main__":
    main()