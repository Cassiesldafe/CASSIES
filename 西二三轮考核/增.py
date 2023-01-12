from 初学1 import db, TODOLIST

#增
s1 = TODOLIST(title="number1", content="123", completion_status="已完成", add_time=20230105, deadline=20230105)
db.session.add(s1)
db.session.commit()
