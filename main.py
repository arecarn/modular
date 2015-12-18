import argparse

import git
import os


def module(url, directory):
    if os.path.isdir(directory):
        try:
            test2 = git.repo.base.Repo(directory)
        except git.exc.InvalidGitRepositoryError:
            print("can't clone repo at {directory} since it already exists").format(directory=directory)
    else:
        print("cloning")
        git.Repo.clone_from(url, directory)
        # print "I need to sync"
        # subprocess.call(["git", "clone", "--recursive",  url, loc])
        # subprocess.call(["git", "submodule", "update", "--init", "--recursive"])

# if 0:
#     # update
#     for repo in repos
#         if can be updated cleanly:
#             git pull
#         else
#           # error: can not be cleanly updated push changes?
#
#   # remove

def main():
    """
    update modes by priority
    - git - fetches and see's if it's up to date
    - curl - version does some sort of checksum to see if it's the same as the
      stored one
    - wget - like curl?
    - mecurial - like git?
    - svn ??

    look here for curl timestamp: http://blog.yjl.im/2012/03/downloading-only-when-modified-using.html
    os.stat()

    module
    check to see if all the modules, or list of modules exits

    module update
    update all modules that are out of date
    check that this can be done cleanly

    module clean
    if files haven't been changed, removes modules
    --force
    """
    url = "https://github.com/dcestari/git-external.git"
    location1 = os.path.join(os.path.expanduser("~"), "test1")
    location2 = os.path.join(os.path.expanduser("~"), "test2")
    location3 = os.path.join(os.path.expanduser("~"), "test3")

    module(url=url, location=location1)
    module(url=url, location=location2)
    module(url=url, location=location3)





# does git repository match
if __name__ == '__main__':
    main()
