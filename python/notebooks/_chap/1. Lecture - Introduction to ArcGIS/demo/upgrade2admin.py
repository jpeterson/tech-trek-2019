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


if __name__ == "__main__":
    fp = "./class.csv"
    new_role = "org_admin"
    gis = GIS(profile='class_profile')
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


