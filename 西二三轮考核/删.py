from 初学1 import db, TODOLIST
inf1 = TODOLIST.query.filter(TODOLIST.id == 1).delete()
inf2 = TODOLIST.query.filter(TODOLIST.completion_status == "已完成").delete()
inf3 = TODOLIST.query.filter(TODOLIST.completion_status == "待办").delete()
inf4 = TODOLIST.query.delete()
db.session.commit()