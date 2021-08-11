from pip._internal.cli.base_command import Command
from pip._internal.cli.status_codes import ERROR, SUCCESS
from pip._internal.metadata import BaseDistribution, get_environment

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
            '-o', '--outdated',
            action='store_true',
            default=False,
            help='List outdated packages')
        self.cmd_opts.add_option(
            '-u', '--uptodate',
            action='store_true',
            default=False,
            help='List uptodate packages')
        self.cmd_opts.add_option(
            '-f', '--files',
            dest='files',
            action='store_true',
            default=False,
            help='Show the full list of installed files for each package.')

        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options, args):   #args type -> list of stings
        owning_package = False
        for filename in args:
            owning_package = get_owning_pacakge(filename) #apackage name or none
            if owning_package:
                print("file is owned by {}".format(filename, owning_package)
        return SUCCESS
    

def get_owning_package(filename):  #still need to get owning pacakge
    
    packages = [        #gets name of all packages installed
            d           #from show.py
            for d in get_environment(options.path).iter_installed_distributions(
                local_only=options.local,
                user_only=options.user,
                editables_only=options.editable,
                include_editables=options.include_editable,
                skip=skip,
            )
        ]

    for package in packages:
        package_info = search_package_info([package])
        for filename in package_info["Files"]:
        if filename == pacakge_info["Files"]:
            return package
    return None


def search_package_info(package):
    return files  


