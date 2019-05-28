from arcgis.gis import GIS, UserManager, User
import pandas as pd

if __name__ == "__main__":
    fp = "./class.csv"
    role = 'org_publisher'
    ut = "creatorUT"
    gis = GIS(profile='class_profile')
    df = pd.read_csv(fp)
    for ud in df.to_dict(orient='row'):
        user = gis.users.create(username=ud['username'],
                            firstname=ud['FirstName'],
                            lastname=ud['LastName'],
                            email=ud['fakeemail'],
                            role=role,
                            user_type=ut,
                            password=ud['password'])
        user.reset(password=ud['password'],
                   new_password="demo.pass!1",
                   new_security_question=1,
                   new_security_answer="AZ State")
        del ud


