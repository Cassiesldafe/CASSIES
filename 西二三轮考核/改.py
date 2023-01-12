from 初学1 import db, Information
inf_1 = Information.query.filter(Information.completion_status == "已完成").update({"completion_status": "待办"})
inf_2 = Information.query.filter(Information.completion_status == "待办").update({"completion_status": "已完成"})
inf_3 = Information.query.update({"completion_status": "待办"})
inf_4 = Information.query.update({"completion_status": "已完成"})
db.session.commit()