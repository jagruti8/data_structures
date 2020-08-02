# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 23:55:18 2020

@author: JAGRUTI
"""


import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    # for maintaning the list of paths ending with the particular suffix
    list_path_main = []
    
    # if no path is given
    if path == "":
        print("Please enter some path")
        return
        
    # if the current path is a file 
    if os.path.isfile(path):
        # if no suffix means we can append the file irrespective of it's ending
        if suffix == "":
            list_path_main.append("./" + path)
            return list_path_main
        # check if it ends with that suffix
        last_extension = "." + path.split(".")[1]
        if last_extension == suffix:
            list_path_main.append("./" + path)
        return list_path_main
        
    # if the current path is a directory
    elif os.path.isdir(path):
        for item in os.listdir(path):   
            # add content of the directory to the present path
            subpath = os.path.join(path, item)
            # search the subpath
            list_from_recursion = find_files(suffix, subpath)
            # add list of paths obtained from recursion to the list in the present activation function
            list_path_main += list_from_recursion
    
    # if the path is invalid
    else:
        print("path: {} does not exist".format(path))
        return
    
    return list_path_main

## Examples
    
# Normal Cases:

print(find_files(".c","testdir")) 
# ['./testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir1/a.c']
print(find_files(".c","testdir/subdir1"))
# ['./testdir/subdir1/a.c']
print(find_files(".c","testdir/subdir2"))
# []
print(find_files(".c","testdir/subdir3"))
# ['./testdir/subdir3/subsubdir1/b.c']
print(find_files(".c","testdir/subdir4"))
# []
print(find_files(".c","testdir/subdir5"))
# ['./testdir/subdir5/a.c']

# Edge Cases:

print(find_files(".c","")) # Please enter some path | None
print(find_files("","testdir"))
# ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir3/subsubdir1/b.c', './testdir/subdir5/a.h', 
# './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir4/.gitkeep', './testdir/subdir1/a.h', 
# './testdir/subdir1/a.c', './testdir/t1.h', './testdir/subdir2/.gitkeep']
print(find_files("",""))   # Please enter some path | None
print(find_files("","testdir1")) # path: testdir1 does not exist | None
print(find_files(".c","subdir5")) # path: subdir5 does not exist | None (it exists inside testdir)
