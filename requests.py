from data.db_session import create_session, global_init
from data.news import News
from data.users import User
from data.jobs import Jobs


name_db = input()
global_init(name_db)
session = create_session()
request = session.query(Jobs).filter(
    (Jobs.job.like('%chief%')) | (Jobs.job.like('%middle%'))).all()
for i in request:
    request_user = session.query(User).filter(User.id == i.team_leader).first()
    print(request_user, i.job)
session.close()