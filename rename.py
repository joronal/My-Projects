#The script looks at the beginning of the file names (zip, 7z) for the string Sxxx, cuts this string and adds it to the end of the file name
import os
import re

current_dir = 'DIR'
files = os.listdir(current_dir)
for file in files:
    if file.endswith('7z') or file.endswith('zip'):
        match = re.match('S\d{4}', file)
        if match:
            fragment = match.group()
            base, ext = os.path.splitext(file)
            new_name = base.replace(fragment, '')
            new_name = new_name.strip()
            new_name = new_name + ' ' + fragment
            new_name = new_name + ext
            os.rename(os.path.join(current_dir, file), os.path.join(current_dir, new_name))
            print(new_name)


            