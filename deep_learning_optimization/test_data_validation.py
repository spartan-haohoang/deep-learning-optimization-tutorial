"""
Tests for data validation functionality.
"""

import sys
from pathlib import Path

import pandas as pd

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from scripts.validate_data import (  # noqa: E402
    validate_iris_data,
    validate_root_cause_data,
)


class TestDataValidation:
    """Test data validation functions."""

    def test_iris_data_exists(self):
        """Test that Iris dataset exists and is accessible."""
        iris_path = Path("data/iris.csv")
        assert iris_path.exists(), "Iris dataset should exist"

    def test_iris_data_structure(self):
        """Test Iris dataset structure and content."""
        iris_path = Path("data/iris.csv")
        if iris_path.exists():
            df = pd.read_csv(iris_path)

            # Check required columns
            required_columns = [
                "Sepal.Length",
                "Sepal.Width",
                "Petal.Length",
                "Petal.Width",
                "Species",
            ]
            for col in required_columns:
                assert col in df.columns, f"Column {col} should exist in Iris dataset"

            # Check data types
            numeric_columns = [
                "Sepal.Length",
                "Sepal.Width",
                "Petal.Length",
                "Petal.Width",
            ]
            for col in numeric_columns:
                assert pd.api.types.is_numeric_dtype(
                    df[col]
                ), f"Column {col} should be numeric"

            # Check species values
            valid_species = {"setosa", "versicolor", "virginica"}
            actual_species = set(df["Species"].unique())
            assert actual_species.issubset(
                valid_species
            ), f"Invalid species found: {actual_species - valid_species}"

            # Check minimum data size
            assert len(df) >= 100, "Iris dataset should have at least 100 rows"

    def test_root_cause_data_exists(self):
        """Test that root cause analysis dataset exists."""
        rca_path = Path("data/root_cause_analysis.csv")
        assert rca_path.exists(), "Root cause analysis dataset should exist"

    def test_root_cause_data_structure(self):
        """Test root cause analysis dataset structure."""
        rca_path = Path("data/root_cause_analysis.csv")
        if rca_path.exists():
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
            for col in required_columns:
                assert (
                    col in df.columns
                ), f"Column {col} should exist in root cause dataset"

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
                assert pd.api.types.is_numeric_dtype(
                    df[col]
                ), f"Column {col} should be numeric"

            # Check root cause values
            valid_causes = {"MEMORY_LEAK", "NETWORK_DELAY", "DATABASE_ISSUE"}
            actual_causes = set(df["ROOT_CAUSE"].unique())
            assert actual_causes.issubset(
                valid_causes
            ), f"Invalid root causes found: {actual_causes - valid_causes}"

            # Check minimum data size
            assert len(df) >= 500, "Root cause dataset should have at least 500 rows"

    def test_validation_functions(self):
        """Test the validation functions directly."""
        # Test Iris validation
        iris_result = validate_iris_data()
        assert isinstance(iris_result, bool), "Iris validation should return boolean"

        # Test root cause validation
        rca_result = validate_root_cause_data()
        assert isinstance(
            rca_result, bool
        ), "Root cause validation should return boolean"
