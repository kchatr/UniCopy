from flask import Flask

def create_app():
    app = Flask(__name__, template_folder="template")

    # Uncomment the line below if you want to enable Flask's debug mode
    # app.debug = True

    # from .views import main
    from views import main 

    app.register_blueprint(main)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
