 #!/usr/bin/env python3

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

import argparse

import git
import os

import util

parser = argparse.ArgumentParser(description='setup dotfiles')
parser.add_argument(
        "--file",
        default="./modules.py",
        help="path of the module file")

args = parser.parse_args()
# ============================================================================

modules = util.dynamic_import(args.file, "")

def main():
    for module in modules.MODULES:
        Module(
            module["url"],
            util.resolve_path_absolute(module["directory"]),
            module["rev"]).update()

class Module():
    def __init__(self, url, directory, rev='master'):
        self.url = url
        self.directory = directory
        self.rev = rev
        self.repo = git.Git(self.directory)

        if not os.path.isdir(self.directory): # TODO is this redundant considering the try?
            print("cloning {url} to {directory}".format(url=self.url,
                directory=self.directory))
            self.repo.clone_from(self.url, self.directory, "--recursive")
            self.repo.submodule("update", "--init", "--recursive")
            self.repo.checkout(self.rev)

        try:
            self.repo = git.Git(self.directory)
        except git.exc.InvalidGitRepositoryError:
            print("{directory} already exits and is not a git "
                    "repo".format(directory=self.directory))

    def update(self):
        self.repo.fetch()
        try:
            if int(self.repo.rev_list("HEAD...@{u}", "--count")):
                print("pulling updates from {url} to "
                        "{directory}".format(url=self.url, directory=self.directory))
                self.repo.pull("--ff", "--ff-only")
                self.repo.submodule("update", "--init", "--recursive")
        except git.exc.GitCommandError as exception_message:
            print("for: {directory} \n"
                    "{exception_message}".format(
                        directory=self.directory,
                        exception_message=exception_message)
            )
        else:
            self.repo.checkout(self.rev)


# does git repository match
if __name__ == '__main__':
    main()
