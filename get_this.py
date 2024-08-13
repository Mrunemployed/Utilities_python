import os
import re

def get_this(**kwargs):
    if kwargs.keys():
        check = os.path.abspath(os.path.curdir)
        all = [os.path.abspath(x) for x in os.listdir(check) if ".git" not in x]
        all_dirs = [x for x in all if os.path.isdir(x)]
        file_map = ([(root,files) for tree in all_dirs for root,dirs,files in os.walk(os.path.abspath(tree),topdown=True)])
        complete_paths = [f"{x}\\{y}" for x,i in file_map for y in i]
        all.extend(complete_paths)
        print(all)
        if 'ext' in kwargs.keys():
            check = [x for x in all if re.search(f"{kwargs['file_like']}\.({kwargs['ext']})$",x)]
        else:
            check = [x for x in all if re.search(f"{kwargs['file_like']}",x)]

        if len(check) > 0:
            return check
        else:
            return False
    else:
        raise Exception("Invalid arguments")
    
# Example:
foo = get_this(file_like="readme",ext='md')
print(foo)