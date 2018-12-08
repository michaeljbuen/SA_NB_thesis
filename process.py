import pandas as pd
import email
from csv_splitter import split


#split(open('static/imdb_csv/imdb_master.csv', 'r'))
#split(open('static/enron_csv/original_enron/emails.csv', 'r'))
df = pd.read_csv('static/enron_csv/split_enron/output_35.csv')
rf = pd.read_csv ('static/imdb_csv/split_imdb/output_1.csv', encoding = "ISO-8859-1")


def get_text_from_email(msg):
    parts = []
    for part in msg.walk():
        if part.get_content_type() == 'text/plain': #extracting text data
            parts.append(part.get_payload())
    return ''.join(parts)

def split_email_adds(line): #splitting email addresses
    if line:
        addrs = line.split(',')
        addrs = frozenset(map(lambda x : x.strip(), addrs))
    else:
        addrs = None
    return addrs


msgs = list(map(email.message_from_string, df['message']))
df.drop('message', axis=1, inplace=True)  # axis = 1 used to apply a method across each row
# Get all fields from the email objects
fields = msgs[0].keys()
for field in fields:
    df[field] = [doc[field] for doc in msgs]

# parse content from emails
df['content'] = list(map(get_text_from_email, msgs))
    # Split email address
#df['From'] = df['From'].map(split_email_adds)
#df['To'] = df['To'].map(split_email_adds)

    # Extract the root of file as user
df['user'] = df['file'].map(lambda x: x.split('/')[0])
del msgs

