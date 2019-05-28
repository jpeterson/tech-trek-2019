__version__ = "1.0.0"
import os
import sys
import logging
import argparse
import datetime
from logging.handlers import RotatingFileHandler

from arcgis.gis import GIS, UserManager, User
import pandas as pd

module = sys.modules['__main__'].__file__
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG,
                    format='%(name)s (%(levelname)s): %(message)s')
log = logging.getLogger(module)

def parse_command_line(argv):
    """Parse command line argument. See -h option

    :param argv: arguments on the command line must include caller file name.
    """
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(description=module,
                                     formatter_class=formatter_class)
    parser.add_argument('-p', '--profile',
                       required=True,
                       help='Name of the login profile')
    parser.add_argument('-csv', '--csv',
                       required=True,
                       help='The CSV file containing the users to update.')
    parser.add_argument('-r', '--role',
                       required=True,
                       help='Name of the role to switch the users to.')
    parser.add_argument("--version", action="version",
                        version="%(prog)s {}".format(__version__))
    parser.add_argument("-v", "--verbose", dest="verbose_count",
                        action="count", default=0,
                        help="increases log verbosity for each occurence.")
    parser.add_argument('-o', help="(optional) writes output to a file")
    arguments = parser.parse_args(argv[1:])
    if arguments.o:
        fh = RotatingFileHandler(arguments.o, mode='a', maxBytes=2*1024*1024,
                            backupCount=2, encoding=None, delay=0)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        fh.setLevel(logging.DEBUG)
        log.addHandler(fh)
    # Sets log level to WARN going more verbose for each new -v.
    log.setLevel(max(3 - arguments.verbose_count, 0) * 10)
    return arguments

def main(argv):
    fp = argv.csv
    new_role = argv.role
    gis = GIS(profile=argv.profile)
    df = pd.read_csv(fp)
    um = gis.users
    for ud in df['username'].tolist():
        user = um.get(username=ud)
        log.info("... {user} has the role: {role}".format(user=ud,
                                                          role=user.role))
        if user.role != new_role:
            user.update_role(role=new_role)
            log.info("... {user} has the new role of: {role}".format(user=ud,
                                                                     role=user.role))
        del ud
    log.info("Finished Updating the Users")

if __name__ == "__main__":
    argv = parse_command_line(argv=sys.argv)
    main(argv)


