import os.path
import tornado.ioloop
import tornado.web
from pathlib import Path
import datetime

def data():
  base_time = datetime.datetime(2023,11, 10, 12 ,00 ,00)
  tasks = [
    { "id":1, "title":"ネギを買う", "created_at":base_time },
    { "id":2, "title":"山田と飯", "created_at":base_time + datetime.timedelta(3) },
    { "id":3, "title":"豊島園に行く", "created_at":base_time - datetime.timedelta(2) },
    { "id":4, "title":"面接", "created_at":base_time + datetime.timedelta(5) },
    { "id":5, "title":"美容室に行く", "created_at":base_time - datetime.timedelta(6) }
  ]
  return tasks

class MainHandler(tornado.web.RequestHandler):

  def get(self):
    taskss = data()
    q = ""
    self.render("index.html", taskss=taskss, q=q)

  def post(self):
    tasks = data()
    taskss = []
    q = self.get_argument('q')
    print(q)
    if q == "desc":
      taskss = sorted(tasks, key=lambda o:o['created_at'])
    elif q == "asc":
      #tasksをcreated_atの値をキーとして降順に並べる
      taskss = sorted(tasks, key=lambda o:o['created_at'], reverse=True)
    self.render("index.html", taskss=taskss, q=q)

application = tornado.web.Application([
  (r"/", MainHandler),
  ],
  template_path=os.path.join(os.path.dirname(__file__), 'templates')
)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
