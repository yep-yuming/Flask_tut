from distutils.dir_util import create_tree
from website import create_app

app = create_app()



if __name__ =='__main__':
    app.run(debug = True)