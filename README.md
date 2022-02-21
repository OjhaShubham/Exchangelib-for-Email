# Exchangelib-for-Email

This module provides an well-performing, well-behaving, platform-independent and simple interface for communicating with a Microsoft Exchange 2007-2016 Server or Office365 using Exchange Web Services (EWS). It currently implements autodiscover, and functions for searching, creating, updating, deleting, exporting and uploading calendar, mailbox, task, contact and distribution list items.

Here's a short example of how exchangelib works. Let's print the first 100 inbox messages in reverse order:

from exchangelib import Credentials, Account

credentials = Credentials('shubhamojha@gmail.com', 'topsecret')
account = Account('john@example.com', credentials=credentials, autodiscover=True)

for item in account.inbox.all().order_by('-datetime_received')[:100]:
    print(item.subject, item.sender, item.datetime_received
