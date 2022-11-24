#!/env/bin/python

import yaml
import time
from git import Repo


def get_credentials(filename: str="env.yml"):
    try:
        with open(filename, "r") as stream:
            return yaml.safe_load(stream)
    except Exception as e:
        print(e)
        return False


##
# save the link as a page with the filename as the unix timestamp
##
def save_as_page(link: str, tags: str):
    try:
        timestamp = str(int( time.time() ))
        new_page_name = "./docs/{}".format(timestamp)
        page_content = """
# {0}

[{0}]({0})


## Tags
- {1}
    """.format(link,tags)
        with open(new_page_name+".md", "w") as f:
            f.write(page_content)
    except Exception as e:
        print(e)



def list_to_string(s: str):
    temp = ""
    for char in s:
        temp += (char + ",")
    return temp[:-1] # remove last comma



def save_link(link: str, tags: str):
    try:
        save_as_page(link, tags)
    except Exception as e:
        print("Couldn't make page", link, tags)
        print(e)






def update_github_pages(commit_msg: str=""):
    PATH_OF_GIT_REPO = './.git'  # make sure .git folder is properly configured
    if commit_msg == "":
        commit_msg = "new page added " + str(int( time.time() )) 
    try:
        time.sleep(5) # wait for file to be made
        repo = Repo(PATH_OF_GIT_REPO)
        repo.git.add(update=True)
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')  