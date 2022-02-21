from exchangelib import Credentials, Account

credentials = Credentials('shubhamojha@gmail.com', 'ShuuDonotTry')
account = Account('shubhamojha@gmail.com', credentials=credentials, autodiscover=True)
# print("before loop")
for item in account.inbox.all().order_by('-datetime_received')[:10]:)
    print(item.subject, item.sender, item.datetime_received)
