from pathlib import Path
import os
from email.parser import FeedParser
from pip._vendor import pkg_resources
from pip._vendor.packaging.utils import canonicalize_name

from pip._internal.cli import cmdoptions
from pip._internal.cli.base_command import Command
from pip._internal.cli.status_codes import ERROR, SUCCESS
from pip._internal.metadata import BaseDistribution, get_environment
from pip._internal.utils.misc import get_file_list

class ProvidesCommand(Command):
    """
    Show information about one or more installed packages.

    The output is in RFC-compliant mail header format.
    """

    usage = """
      %prog [options] <package> ..."""
    def add_options(self):
        # type: () -> None
 
        self.cmd_opts.add_option(
            '--format',
            action='store',
            dest='list_format',
            default="columns",
            choices=('columns', 'freeze', 'json'),
            help="Select the output format among: columns (default), freeze, "
                 "or json",
            )

        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options, args):   #args type -> list of stings
######HERE

##        package = {
##            'name': dist.project_name,
##            'version': dist.version,
##            'location': dist.location,
##            'requires': [dep.project_name for dep in dist.requires()],
##            'required_by': get_requiring_packages(dist.project_name)
##            'clasifiers': ... 
##            'file': ... maybe
##            'metadata-version
##        }
        for arg in args: #args -> list of filename or absolute 
            for dist in pkg_resources.working_set:
                installed_file_list = get_file_list(dist)
                package = {
                    'name': dist.project_name,
                    'version': dist.version,
                    'location': dist.location,
                    'requires': [dep.project_name for dep in dist.requires()],
                    #'files': get_file_list(dist)
                    #'required_by': get_requiring_packages(dist.project_name)
                    }
                for filename in installed_file_list:
                    path = Path(package['location']).joinpath(filename)
                    abs_path = path.resolve()
                    if arg == str(abs_path):
                        print(arg, "comes from the", package['name'], "package")
                    elif arg in filename:
                        print(arg, "is in", abs_path)                    
        return SUCCESS      
    
