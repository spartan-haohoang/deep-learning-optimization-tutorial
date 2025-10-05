#!/usr/bin/env python3
"""
Notebook execution script for Deep Learning Optimization Tutorial
Allows running Jupyter notebooks programmatically for automated testing.
"""

import argparse
import sys
from pathlib import Path

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor


def run_notebook(notebook_path, timeout=600, kernel_name="python3"):
    """
    Execute a Jupyter notebook and return success status.

    Args:
        notebook_path (str): Path to the notebook file
        timeout (int): Execution timeout in seconds
        kernel_name (str): Name of the kernel to use

    Returns:
        bool: True if execution successful, False otherwise
    """
    notebook_path = Path(notebook_path)

    if not notebook_path.exists():
        print(f"❌ Notebook not found: {notebook_path}")
        return False

    print(f"🚀 Executing notebook: {notebook_path.name}")

    try:
        # Load the notebook
        with open(notebook_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)

        # Execute the notebook
        ep = ExecutePreprocessor(timeout=timeout, kernel_name=kernel_name)
        ep.preprocess(nb, {"metadata": {"path": notebook_path.parent}})

        print(f"✅ Notebook executed successfully: {notebook_path.name}")
        return True

    except Exception as e:
        print(f"❌ Error executing notebook {notebook_path.name}: {e}")
        return False


def run_all_notebooks():
    """Run all tutorial notebooks in sequence."""
    notebooks = [
        "01_common_functions.ipynb",
        "02_network_tuning.ipynb",
        "03_backpropagation_tuning.ipynb",
        "04_overfitting_management.ipynb",
        "05_root_cause_analysis.ipynb",
    ]

    print("🚀 Running all Deep Learning Optimization Tutorial notebooks...")
    print("=" * 60)

    results = []
    for notebook in notebooks:
        if Path(notebook).exists():
            success = run_notebook(notebook)
            results.append((notebook, success))
        else:
            print(f"⚠️  Notebook not found: {notebook}")
            results.append((notebook, False))

    print("=" * 60)
    print("📊 Execution Summary:")

    successful = 0
    for notebook, success in results:
        status = "✅" if success else "❌"
        print(f"  {status} {notebook}")
        if success:
            successful += 1

    print(
        f"\n📈 Results: {successful}/{len(results)} notebooks " f"executed successfully"
    )

    return successful == len(results)


def main():
    """Main function with command line interface."""
    parser = argparse.ArgumentParser(
        description="Execute Deep Learning Optimization Tutorial notebooks"
    )
    parser.add_argument(
        "notebook",
        nargs="?",
        help="Specific notebook to run (optional, runs all if not specified)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=600,
        help="Execution timeout in seconds (default: 600)",
    )
    parser.add_argument(
        "--kernel",
        default="python3",
        help="Kernel name to use (default: python3)",
    )

    args = parser.parse_args()

    # Use current directory as project root
    # script_dir = Path(__file__).parent
    # project_root = script_dir.parent
    # os.chdir(project_root)

    if args.notebook:
        # Run specific notebook
        success = run_notebook(args.notebook, args.timeout, args.kernel)
        return 0 if success else 1
    else:
        # Run all notebooks
        success = run_all_notebooks()
        return 0 if success else 1


if __name__ == "__main__":
    sys.exit(main())
