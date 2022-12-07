import ezgmail
import time
import utils
import logging
import sys



logging.basicConfig(
    filename='app.log', 
    filemode='w', 
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
    )




while True:

    try:
        unread_emails = ezgmail.unread()
        secrets = utils.get_credentials()
        white_list = secrets.get("email_whitelist")
        logging.info('whitelist: ' + str(white_list))
        wait_time_minutes = int(secrets.get("email_wait_time")[0])

    except Exception as e:
        logging.error(e)
        sys.exit()

    new_pages_to_add = False

    for threads in unread_emails:
        thread = threads.messages
        for email in thread:
            logging.info(f"Looking at email")
            if (email.sender in white_list):
                new_pages_to_add = True
                logging.info("got link: " + email.subject + " | " + email.body)
                utils.save_as_page(email.subject, email.body)
                if new_pages_to_add:
                    logging.info('Updating github...')
                    utils.update_github_pages()
                sys.exit()
                #time.sleep(1) # prevents us from overwritting files

        #threads.markAsRead()


        
    logging.info("sleeping...")
    sys.exit()
    #time.sleep(60*wait_time_minutes)

