from 初学1 import db, Information
inf1 = Information.query.filter(Information.id == 1).delete()
inf2 = Information.query.filter(Information.completion_status == "已完成").delete()
inf3 = Information.query.filter(Information.completion_status == "待办").delete()
inf4 = Information.query.delete()
db.session.commit()