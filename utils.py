#!/env/bin/python

import yaml
import time
from git import Repo
import logging
import sys
import subprocess


logging.basicConfig(
    filename='app.log', 
    filemode='a', 
    format='%(name)s - %(levelname)s - %(message)s',
    level=logging.DEBUG
    )




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
        new_page_name = f"./docs/{timestamp}.md"
        link_domain = get_domain_from_url(link)
        print(type(link_domain))
        logging.info(f"Making page with link: {link_domain} and tags: {tags}")
        page_content = f"\n# {link_domain}\n\n[{link_domain}]({link})\n\n\n## Tags\n- {tags}"
        with open(new_page_name, "w") as f:
            f.write(page_content)
    except Exception:
        logging.error(f"save_as_page got error with link: {link} tags: {tags}")
        sys.exit()



def list_to_string(s: str):
    temp = ""
    for char in s:
        temp += (char + ",")
    result = temp[:-1]
    return result # remove last comma



def update_github_pages(commit_msg: str=""):
    PATH_OF_GIT_REPO = './.git'  # make sure .git folder is properly configured
    if commit_msg == "":
        commit_msg = "new page added " + str(int( time.time() )) 
#    try:
    repo = Repo(PATH_OF_GIT_REPO)
    for remote in repo.remotes:
        remote.fetch()
    repo.git.add(update=True)
    repo.index.commit(commit_msg)
    origin = repo.remote(name='origin')
    origin.push()
    # # except Exception as e:
    #     print('Some error occured while pushing the code')
    #     print(e)
    # git_cmd = f"git fetch && git add *.md && git commit -m '{commit_msg} && git push && git fetch && git pull".split(" ")
    # git_cmd = ['git', 'fetch', 'git', 'add']
    # process = subprocess.Popen(git_cmd, stdout=subprocess.PIPE)
    # output = process.communicate()[0]
    # print(output)


# https://hostname/idk/idk --> hostname/idk/idk
# www.hostname/idk         --> hostname/idk
def get_domain_from_url(url: str):
    if url[:8] == "https://":
        url = url[8:]
    if url[:4] == "www.":
        url = url[4:]
    return url
