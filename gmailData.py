import imaplib
import email
import getpass
import pandas as pd
import re
import urllib

username = input("Enter gmail address: ")
password = getpass.getpass("Enter password: ")
mail = imaplib.IMAP4_SSL('imap.gmail.com')
mail.login(username,password)

#Selecting the mail box
mail.select("INBOX")

# Searching gmail for Transaction details
result, numbers = mail.uid('search', None, 'X-GM-RAW "subject:invoice OR subject:bill OR subject:statement OR subject:(payment receipt) OR subject:(transaction alert) OR subject:(subscriptions alert) OR subject:(your balance) OR (Transaction receipt)"')
uids = numbers[0].split()
uids = [id.decode('utf-8') for id in uids]
result, messages = mail.uid('fetch', ','.join(uids), '(BODY[HEADER.FIELDS (SUBJECT FROM DATE)])')

date_list = []
from_list = []
subject_text = []
for i, message in messages[::2]:
    msg = email.message_from_bytes(message)
    decode = email.header.decode_header(msg['Subject'])[0]
    # print(msg)
    if isinstance(decode[0],bytes):
        decoded = decode[0].decode()
        subject_text.append(decoded)
    else:
        subject_text.append(decode[0])
    date_list.append(msg.get('date'))
    fromlist = msg.get('FROM')
    fromlist = re.sub('[<>]', '',fromlist)
    parsed = urllib.parse.urlparse(fromlist)
    from_address = parsed.path
    from_list.append(from_address)

date_list = pd.to_datetime(date_list)
date_list1 = []
for item in date_list:
    date_list1.append(item.isoformat(' ')[:-6])
# Generate CSV file 
df = pd.DataFrame(data={'Date':date_list1, 'Sender':from_list, 'Subject':subject_text})
df.to_csv('inbox_email.csv',index=False)
