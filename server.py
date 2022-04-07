import tornado.ioloop
import tornado.web

class HomeHandler(tornado.web.RequestHandler):
  def get(self):
    self.render("index.html")

def webapp():
  return tornado.web.Application([
    (r"/", HomeHandler)
  ],
  debug = True,
  autoreload = True
  )


if __name__ == "__main__":
  app = webapp()
  app.listen(3000)
  tornado.ioloop.IOLoop.current().start()