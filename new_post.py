'''
Create new post and add link to index.md
Exec `python3 new_post <post name>`
'''
import sys
from datetime import date

POSTS_HEADING = '## Posts'

if len(sys.argv) < 1:
    exit(1)

post_name = sys.argv[1]
post_path = f'posts/{post_name}.md'

today = date.today()

'''
Create new post with heading and date
'''
with open('docs/' + post_path, 'x') as f:
    f.write(
        f'''# {post_name}
_{today}_
        ''')

'''
Open index.md and find the index of the "Posts" heading and
insert link to index + 1 to get the most recent post at the top.
'''
with open('docs/index.md', 'r') as f:
    contents = f.readlines()

    idx = 0
    for i, c in enumerate(contents):
        if c.startswith(POSTS_HEADING):
            idx = i
            break

    if idx > 0:
        contents.insert(idx + 1, f'_{today}_ / [{post_name}]({post_path})\n\n')

with open('docs/index.md', 'w') as f:
    f.writelines(contents)