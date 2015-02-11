import argparse
import os
import subprocess


def main():
    """
    - git fetches and see's if it's up to date
    - mecurial like git?
    - svn ??
    - curl version does some sort of checksum to see if it's the same as the
    stored one 
    look here for curl timestamp: http://blog.yjl.im/2012/03/downloading-only-when-modified-using.html
    os.stat()


    module
    check to see if all the modules, or list of modules exits and are up to date

    module update [white space list of module names]
    update all moduls that need it all mode

    module clean [white space list of module names]
    if files haven't been changed, removes modules

    if directory location exists

    if is git repo

    if git repo is up to date
    """
    module(url="https://github.com/dcestari/git-external.git", loc="~/Desktop/modules/test1")
    module(url="https://github.com/dcestari/git-external.git", loc="~/Desktop/modules/test2")
    module(url="https://github.com/dcestari/git-external.git", loc="~/Desktop/modules/test3")


def module(url, loc):
    #TODO strip front and back
    gitpath = os.path.join(loc, ".git")

    if  not os.path.isdir(loc) and not os.path.isdir(gitpath):
        print "I need to sync"
        subprocess.call(["git", "clone", "--recursive",  url, loc])
        subprocess.call(["git", "submodule", "update", "--init", "--recursive"])
    else:
        print "I'm Good Bro"


if __name__ == '__main__':
    main()
