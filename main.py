import ezgmail
import time
import utils
import logging







while True:

    try:
        unread_emails = ezgmail.unread()
        secrets = utils.get_credentials()
        white_list = secrets.get("email_whitelist")
        logging.info('whitelist: ', white_list)
        wait_time_minutes = int(secrets.get("email_wait_time")[0])
        logging.info('waittime: ', wait_time_minutes)

    except Exception as e:
        logging.error("Couldn't init. Check ezgmail or env.yml")
        continue

    new_pages_to_add = False

    for threads in unread_emails:
        thread = threads.messages
        for email in thread:
            if (email.sender in white_list):
                new_pages_to_add = True
                logging.info("got email: ", email.subject, email.body)
                utils.save_link(email.subject, email.body)
                time.sleep(1) # prevents us from overwritting files

        threads.markAsRead()

        if new_pages_to_add:
            utils.update_github_pages()
        

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