#!/usr/bin/env python3
"""
Data validation script for Deep Learning Optimization Tutorial
Validates that all required data files are present and properly formatted.
"""

import os
import sys
from pathlib import Path

import pandas as pd


def validate_iris_data():
    """Validate the Iris dataset."""
    iris_path = Path("data/iris.csv")

    if not iris_path.exists():
        print(f"❌ Iris dataset not found at {iris_path}")
        return False

    try:
        df = pd.read_csv(iris_path)

        # Check required columns
        required_columns = [
            "Sepal.Length",
            "Sepal.Width",
            "Petal.Length",
            "Petal.Width",
            "Species",
        ]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            print(f"❌ Iris dataset missing columns: {missing_columns}")
            return False

        # Check data types and ranges
        numeric_columns = [
            "Sepal.Length",
            "Sepal.Width",
            "Petal.Length",
            "Petal.Width",
        ]
        for col in numeric_columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                print(f"❌ Iris dataset column '{col}' is not numeric")
                return False

        # Check species values
        valid_species = {"setosa", "versicolor", "virginica"}
        actual_species = set(df["Species"].unique())
        if not actual_species.issubset(valid_species):
            print(
                f"❌ Iris dataset contains invalid species: "
                f"{actual_species - valid_species}"
            )
            return False

        print(
            f"✅ Iris dataset validated: {len(df)} rows, " f"{len(df.columns)} columns"
        )
        return True

    except Exception as e:
        print(f"❌ Error validating Iris dataset: {e}")
        return False


def validate_root_cause_data():
    """Validate the root cause analysis dataset."""
    rca_path = Path("data/root_cause_analysis.csv")

    if not rca_path.exists():
        print(f"❌ Root cause analysis dataset not found at {rca_path}")
        return False

    try:
        df = pd.read_csv(rca_path)

        # Check required columns
        required_columns = [
            "ID",
            "CPU_LOAD",
            "MEMORY_LEAK_LOAD",
            "DELAY",
            "ERROR_1000",
            "ERROR_1001",
            "ERROR_1002",
            "ERROR_1003",
            "ROOT_CAUSE",
        ]
        missing_columns = [col for col in required_columns if col not in df.columns]

        if missing_columns:
            print(f"❌ Root cause dataset missing columns: {missing_columns}")
            return False

        # Check data types
        numeric_columns = [
            "ID",
            "CPU_LOAD",
            "MEMORY_LEAK_LOAD",
            "DELAY",
            "ERROR_1000",
            "ERROR_1001",
            "ERROR_1002",
            "ERROR_1003",
        ]
        for col in numeric_columns:
            if not pd.api.types.is_numeric_dtype(df[col]):
                print(f"❌ Root cause dataset column '{col}' is not numeric")
                return False

        # Check root cause values
        valid_causes = {"MEMORY_LEAK", "NETWORK_DELAY", "DATABASE_ISSUE"}
        actual_causes = set(df["ROOT_CAUSE"].unique())
        if not actual_causes.issubset(valid_causes):
            print(
                f"❌ Root cause dataset contains invalid causes: "
                f"{actual_causes - valid_causes}"
            )
            return False

        print(
            f"✅ Root cause analysis dataset validated: {len(df)} rows, "
            f"{len(df.columns)} columns"
        )
        return True

    except Exception as e:
        print(f"❌ Error validating root cause dataset: {e}")
        return False


def main():
    """Main validation function."""
    print("🔍 Validating Deep Learning Optimization Tutorial Data...")
    print("=" * 60)

    # Change to project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)

    # Validate datasets
    iris_valid = validate_iris_data()
    rca_valid = validate_root_cause_data()

    print("=" * 60)

    if iris_valid and rca_valid:
        print("✅ All data validation checks passed!")
        return 0
    else:
        print("❌ Some data validation checks failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())
