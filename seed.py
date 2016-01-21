from lequ import db
from lequ.core.models import User, Team, Role, UserTeam

db.session.execute('SET FOREIGN_KEY_CHECKS = 0;')
db.session.execute('truncate table core_user_team;')
db.session.execute('truncate table core_role;')
db.session.execute('truncate table core_user;')
db.session.execute('truncate table core_team;')
db.session.execute('SET FOREIGN_KEY_CHECKS = 1;')
db.session.commit()

user = User('admin', '1234', '8718038@qq.com', '13892091726', '13892091726', 1)
db.session.add(user)
db.session.commit()
team = Team('乐趣OA', user.id)
db.session.add(team)
db.session.commit()
role = Role('管理员', team.id)
db.session.add(role)
db.session.commit()

userTeam = UserTeam(team, user, role, is_owner=True, created_by=user.id)
db.session.add(userTeam)
db.session.commit()
