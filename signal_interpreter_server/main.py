# main.py
from signal_interpreter_server.routes import signal_interpreter_app


def main():
    signal_interpreter_app.run()


if __name__ == "__main__":
    main()
