# GmailAnalysis

This is a simple analysis tool to search gmail for all finiacial transactions. In this project uses imaplib and email to get access to gmail and perform pulls necessary data.

## Prerequisites

 - Enable IMAP in Gmail: Open Gmail and go to settings, under settings choose see all settings, go to 'Forwarding and POP/IMAP' and make sure IMAP access is enabled

 - Less Secure app access: To enable this python app to access google, go to gmail and click on your avatar and choose 'Manage your google account' this would open myaccount.google.com, go to security tab from the left side and scroll down to find 'Less secure app access' and turn it on.

First, clone this repto and navigate to folder

```bash
cd gmailanalysis
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate the virtual environment

```bash
source .venv/bin/activate
```
Install all the packages from req.txt file

```bash
pip3 install req.txt
```

Run the app gmailData.py, enter your user credentials when prompted 

```bash
python gmailData.py
```

Once the script is executed you would see inbox_emal.csv generated which would have the date, from email address and subject which is related to financial transaction be captured.