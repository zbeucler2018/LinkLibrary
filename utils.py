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
        link_domain = get_domain_from_url(link)
        page_content = """
# {link_domain}

[{link_domain}]({0})


## Tags
- {1}
    """.format(link,link_domain,tags)
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
        #repo.fetch()
        repo.git.add(update=True)
        repo.index.commit(commit_msg)
        origin = repo.remote(name='origin')
        origin.push()
    except:
        print('Some error occured while pushing the code')


# https://hostname/idk/idk --> hostname/idk/idk
# www.hostname/idk         --> hostname/idk
def get_domain_from_url(url: str):
    if url[:8] == "https://":
        url = url[8:]
    if url[:4] == "www.":
        url = url[4:]
    return url





h = "https://github.com/facebook/memlab"
print(get_domain_from_url(h))