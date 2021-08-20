from pathlib import Path
from pip._vendor import pkg_resources

from pip._internal.cli import cmdoptions
from pip._internal.cli.base_command import Command
from pip._internal.cli.status_codes import ERROR, SUCCESS
from pip._internal.metadata import BaseDistribution, get_environment
from pip._internal.utils.misc import get_file_list

class ProvidesCommand(Command):
    """
    Given a package name or file name, show all the files associated with
    that package, or given and absolute path, show which package provided
    that file.

    """
    
    def add_options(self):
        # type: () -> None
        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options, args):   #args type -> list of stings
        for arg in args: #args -> list of filename or absolute path
            for dist in pkg_resources.working_set:
                installed_file_list = get_file_list(dist)
                if installed_file_list:
                    for filename in installed_file_list:
                        path = Path(dist.location).joinpath(filename)
                        abs_path = path.resolve()
                        if arg == str(abs_path):
                            print(arg, "comes from the", dist.project_name, "package")
                        elif arg in filename:
                            print(arg, "is in", abs_path)                    
                    return SUCCESS
