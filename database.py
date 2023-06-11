from sqlalchemy import create_engine , text

engine = create_engine("mysql+pymysql://sunday:2023Sunday.@localhost/Personality_System?charset=utf8mb4")

with engine.connect() as conn:
  result = conn.execute(text("select * from jobs"))
  print(result.all())