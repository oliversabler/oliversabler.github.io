'''
Create new html file with basic html structure and place it under draft.

Heading -> filename (argv[1])
Date -> Today
'''

import sys

if len(sys.argv) < 1:
    exit(1)

post_name = sys.argv[1]
post_path = f'drafts/{post_name}.html'

template = f'''<!doctype html>
<html>
    <head>
        <title>Oliver Sabler - {post_name}</title>
    <head>
    <body>
        <h1>{post_name}<h1>
        
        <p>Placeholder text</p>
    </body>
</html>
'''

with open(f'{post_path}', 'x') as f:
    f.write(template)
        

