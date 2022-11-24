import ezgmail
import time
import utils







while True:

    unread_emails = ezgmail.unread()

    secrets = utils.get_credentials()
    white_list = secrets.get("email_whitelist")

    for threads in unread_emails:
        thread = threads.messages
        for email in thread:
            if (email.sender in white_list):
                print(email.subject, email.body)
                utils.save_link(email.subject, email.body)
                time.sleep(1)
        threads.markAsRead()

    time.sleep(60*5)





# page_content = """
# # {0}

# [{0}]({0})

# <div style=" display: block; margin: 0 auto;">
#     <iframe src="{0}"></iframe>
# </div>

# ## Tags
# - {1}
#     """.format(link,tags)