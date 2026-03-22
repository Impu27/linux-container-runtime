import sys
from containerctl.parser import load_config
from containerctl.runner import run_container

def main():
    if len(sys.argv) < 3:
        print("Usage: containerctl run <config.yaml>")
        sys.exit(1)

    action = sys.argv[1]
    config_file = sys.argv[2]

    if action != "run":
        print("Only 'run' command supported")
        sys.exit(1)

    config = load_config(config_file)
    run_container(config)

if __name__ == "__main__":
    main()
