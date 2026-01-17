from app.bootstrap import build_container
from config.load import load_config

def main():
    config = load_config()
    container = build_container(config)
    container["listener"].start()

if __name__ == "__main__":
    main()
