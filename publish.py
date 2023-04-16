'''
Publish drafts folder by moving files to /posts

Open index.html and search for {{POSTS}} and insert link to new post below
'''
import os
import shutil
import sys
from datetime import date
from pathlib import Path

if len(sys.argv) < 1:
    exit(1)

POST_INSERT_TAG = '<!-- {{POSTS}} -->'

post_name = sys.argv[1]
post_path_source = f'drafts/{post_name}.html'
post_path_target = f'posts/{post_name}.html'

p = Path(post_path_source)
if not p.is_file():
    print('File not found')
    exit(1)

today = date.today()

'''
Brand post with date created
'''
with open(post_path_source, 'r') as f:
    html = f.readlines()

    idx = 0
    for i, c in enumerate(html):
        if c.strip().startswith('<h1>'):
            idx = i
            break

    content = f'        <i>Date created: {today}</i> <br />'

    if idx > 0:
        html.insert(idx + 1, content)

with open(post_path_source, 'w') as f:
    f.writelines(html)


'''
Move post to posts folder
'''
shutil.move(post_path_source, post_path_target)


'''
Add anchor link to post on startpage
'''
with open('index.html', 'r') as f:
    html = f.readlines()

    idx = 0
    for i, c in enumerate(html):
        if c.strip().startswith(POST_INSERT_TAG):
            idx = i
            break

    content = f'''<i>{today}</i> / <br />
    <a href="{post_path_target}">{post_name}</a> <br />
    '''

    if idx > 0:
        html.insert(idx + 1, content)

with open('index.html', 'w') as f:
    f.writelines(html)

