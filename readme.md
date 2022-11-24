

# Link Library
A single place for me to reference all my links.

### Todo
- [ ] `all.md` page or figure out how to fix table of contents to not show url
- [ ] set up github pages
- [ ] docker container
- [ ] set up github actions
    - [ ] on link add, commit to repo, trigger mkdocs deploy action
    - [ ] build dockerfile 



### Install
```bash
python3 -m venv env
source env/bin/activate
pip install mkdocs mkdocs-material pyyaml ezgmail
```


### mkdocs
```bash
# new project
mkdocs new .
# start dev server
mkdocs serve
```