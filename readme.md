

# Link Library
A single place for me to reference all my links.

### Todo
- [ ] `all.md` page or figure out how to fix table of contents to not show url
- [x] set up github pages
- [ ] docker container
- [ ] set up github actions
    - [x] on link add, commit to repo, trigger mkdocs deploy action
    - [ ] build dockerfile 
- [ ] dont allow duplicate pages
- [ ] auto upload links to internet archive and save archive link in page
- [ ] add logging
- [ ] stronger error handling
- [ ] more stable alternative to email



### Install
```bash
python3 -m venv env
source env/bin/activate

pip install mkdocs mkdocs-material pyyaml ezgmail gitpython
# OR
pip install -r requirements.txt
```


### IOS shortcut
<img src="https://user-images.githubusercontent.com/49871927/203728165-3a58c8c1-1e4d-4b3b-8892-4bf09b718db6.jpg" width="300px" height="500px" />



### Links
- [modifying mkdocs-material](https://squidfunk.github.io/mkdocs-material/customization/#overriding-blocks)
- [ezgmail](https://github.com/asweigart/ezgmail)


### mkdocs
```bash
# new project
mkdocs new .
# start dev server
mkdocs serve
```

