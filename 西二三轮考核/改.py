from 初学1 import db, TODOLIST
inf_1 = TODOLIST.query.filter(TODOLIST.id == 1).update({"completion_status": "待办"})
inf_2 = TODOLIST.query.filter(TODOLIST.id == 2).update({"completion_status": "已完成"})
inf_3 = TODOLIST.query.update({"completion_status": "待办"})
inf_4 = TODOLIST.query.update({"completion_status": "已完成"})
db.session.commit()