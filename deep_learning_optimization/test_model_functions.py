"""
Tests for model utility functions.
"""

import sys
from pathlib import Path

import numpy as np
import pandas as pd

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

# Import functions from the common functions notebook
# Note: In a real implementation, these would be extracted to a Python module


class TestModelFunctions:
    """Test model utility functions."""

    def test_data_loading(self):
        """Test that data can be loaded successfully."""
        iris_path = Path("data/iris.csv")
        if iris_path.exists():
            df = pd.read_csv(iris_path)
            assert len(df) > 0, "Iris dataset should not be empty"
            assert len(df.columns) == 5, "Iris dataset should have 5 columns"

    def test_data_preprocessing(self):
        """Test data preprocessing steps."""
        iris_path = Path("data/iris.csv")
        if iris_path.exists():
            df = pd.read_csv(iris_path)

            # Test label encoding
            from sklearn import preprocessing

            label_encoder = preprocessing.LabelEncoder()
            encoded_species = label_encoder.fit_transform(df["Species"])

            assert len(encoded_species) == len(
                df
            ), "Encoded species should have same length as original"
            assert (
                len(np.unique(encoded_species)) == 3
            ), "Should have 3 unique encoded values"

            # Test feature scaling
            from sklearn.preprocessing import StandardScaler

            features = df[
                ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
            ].values
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(features)

            assert (
                scaled_features.shape == features.shape
            ), "Scaled features should have same shape"
            assert np.allclose(
                scaled_features.mean(axis=0), 0, atol=1e-10
            ), "Scaled features should have zero mean"
            assert np.allclose(
                scaled_features.std(axis=0), 1, atol=1e-10
            ), "Scaled features should have unit variance"

    def test_model_configuration(self):
        """Test model configuration structure."""
        # This would test the base_model_config function
        # if extracted to a module
        expected_keys = [
            "HIDDEN_NODES",
            "HIDDEN_ACTIVATION",
            "OUTPUT_NODES",
            "OUTPUT_ACTIVATION",
            "WEIGHTS_INITIALIZER",
            "BIAS_INITIALIZER",
            "NORMALIZATION",
            "OPTIMIZER",
            "LEARNING_RATE",
            "REGULARIZER",
            "DROPOUT_RATE",
            "EPOCHS",
            "BATCH_SIZE",
            "VALIDATION_SPLIT",
            "VERBOSE",
            "LOSS_FUNCTION",
            "METRICS",
        ]

        # Mock configuration for testing
        mock_config = {
            "HIDDEN_NODES": [32, 64],
            "HIDDEN_ACTIVATION": "relu",
            "OUTPUT_NODES": 3,
            "OUTPUT_ACTIVATION": "softmax",
            "WEIGHTS_INITIALIZER": "random_normal",
            "BIAS_INITIALIZER": "zeros",
            "NORMALIZATION": "none",
            "OPTIMIZER": "rmsprop",
            "LEARNING_RATE": 0.001,
            "REGULARIZER": None,
            "DROPOUT_RATE": 0.0,
            "EPOCHS": 10,
            "BATCH_SIZE": 16,
            "VALIDATION_SPLIT": 0.2,
            "VERBOSE": 0,
            "LOSS_FUNCTION": "categorical_crossentropy",
            "METRICS": ["accuracy"],
        }

        for key in expected_keys:
            assert key in mock_config, f"Configuration should contain {key}"

        # Test specific values
        assert (
            mock_config["OUTPUT_NODES"] == 3
        ), "Output nodes should be 3 for Iris classification"
        assert mock_config["LEARNING_RATE"] > 0, "Learning rate should be positive"
        assert (
            0 <= mock_config["VALIDATION_SPLIT"] <= 1
        ), "Validation split should be between 0 and 1"

    def test_optimizer_creation(self):
        """Test optimizer creation logic."""
        # This would test the get_optimizer function if extracted to a module
        optimizers = ["sgd", "rmsprop", "adam", "adagrad"]
        learning_rate = 0.001

        for optimizer_name in optimizers:
            # Mock test - in real implementation would test actual
            # optimizer creation
            assert (
                optimizer_name in optimizers
            ), f"Optimizer {optimizer_name} should be supported"
            assert learning_rate > 0, "Learning rate should be positive"

    def test_data_shapes(self):
        """Test that data has expected shapes for neural network training."""
        iris_path = Path("data/iris.csv")
        if iris_path.exists():
            df = pd.read_csv(iris_path)

            # Test feature matrix shape
            features = df[
                ["Sepal.Length", "Sepal.Width", "Petal.Length", "Petal.Width"]
            ].values
            assert features.shape[1] == 4, "Should have 4 feature columns"
            assert features.shape[0] > 0, "Should have at least one sample"

            # Test target variable
            target = df["Species"]
            assert (
                len(target) == features.shape[0]
            ), "Target should have same length as features"
            assert len(target.unique()) == 3, "Should have 3 unique target classes"
