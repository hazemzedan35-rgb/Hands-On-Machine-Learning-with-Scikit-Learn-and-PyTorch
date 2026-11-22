"""Small environment check before opening the ML learning notebooks."""
from importlib import import_module
import sys

PACKAGES = [
    ("numpy", "numpy"),
    ("sklearn", "scikit-learn"),
    ("matplotlib", "matplotlib"),
    ("jupyterlab", "jupyterlab"),
    ("nbformat", "nbformat"),
    ("nbclient", "nbclient"),
]


def main() -> int:
    print(f"Python {sys.version.split()[0]}")
    if sys.version_info < (3, 10):
        print("Please use Python 3.10 or newer.")
        return 1

    missing = []
    for module_name, display_name in PACKAGES:
        try:
            package = import_module(module_name)
            version = getattr(package, "__version__", "installed")
            print(f"OK  {display_name}: {version}")
        except ImportError:
            missing.append(display_name)
            print(f"MISSING  {display_name}")

    if missing:
        print("\nInstall the dependencies: pip install -r requirements.txt")
        return 1
    print("\nReady to run the starter notebooks!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
