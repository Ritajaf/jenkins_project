import argparse
import shutil
from pathlib import Path


def deploy(destination):
    source = Path(__file__).resolve().with_name("app.py")
    destination = Path(destination)
    destination.mkdir(parents=True, exist_ok=True)
    deployed_file = destination / "app.py"
    shutil.copy2(source, deployed_file)
    if deployed_file.read_bytes() != source.read_bytes():
        raise RuntimeError("Deployment verification failed.")
    print(f"Deployed application to {deployed_file}")
    return deployed_file


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Deploy the Python application."
    )
    parser.add_argument("--destination", required=True)
    args = parser.parse_args()
    deploy(args.destination)
