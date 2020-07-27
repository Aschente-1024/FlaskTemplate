from . import create_app

# if using socketio
# from flask_socketio import SocketIO

if __name__ == '__main__':
    # socket_io = SocketIO(app=create_app())
    # socket_io.run(host='0.0.0.0', debug=True)
    app = create_app()
    app.run(host='0.0.0.0', debug=True)
