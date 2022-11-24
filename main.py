import ezgmail
import time
import utils







while True:

    try:
        unread_emails = ezgmail.unread()
        secrets = utils.get_credentials()
        white_list = secrets.get("email_whitelist")
        wait_time_minutes = int(secrets.get("email_wait_time")[0])
    except Exception as e:
        print("Couldn't init. Check ezgmail or env.yml")

    for threads in unread_emails:
        thread = threads.messages
        for email in thread:
            if (email.sender in white_list):
                print(email.subject, email.body)
                utils.save_link(email.subject, email.body)
                time.sleep(1) # prevents us from overwritting files
        threads.markAsRead()

    time.sleep(60*wait_time_minutes)





# page_content = """
# # {0}

# [{0}]({0})

# <div style=" display: block; margin: 0 auto;">
#     <iframe src="{0}"></iframe>
# </div>

# ## Tags
# - {1}
#     """.format(link,tags)