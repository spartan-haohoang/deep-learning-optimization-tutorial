# Deep Learning Model Optimization and Tuning

A comprehensive tutorial repository for learning deep learning model optimization techniques, including network tuning, backpropagation optimization, overfitting management, and root cause analysis.

## 📚 Learning Objectives

This repository covers essential deep learning optimization topics:

- **Network Architecture Tuning**: Optimizing hidden layers, nodes, and activation functions
- **Backpropagation Optimization**: Learning rate tuning, optimizer selection, and batch size optimization
- **Overfitting Management**: Regularization techniques, dropout, and validation strategies
- **Root Cause Analysis**: Practical application using incident analysis dataset

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip or conda package manager

### Installation

#### Option 1: Using UV (Recommended)
1. Clone or download this repository
2. Install UV package manager:
```bash
make uv-install
```
3. Run the setup script:
```bash
make setup
```

#### Option 2: Using pip
1. Clone or download this repository
2. Install dependencies:
```bash
pip install -r requirements.txt
```

For development dependencies:
```bash
pip install -r requirements-dev.txt
```

#### Option 3: Using Docker
1. Clone or download this repository
2. Build and run with Docker:
```bash
make docker-build
make docker-run
```

### Running the Tutorials

#### Using UV (Recommended)
```bash
make jupyter
```

#### Using pip
```bash
jupyter lab
```

#### Using Docker
```bash
make docker-run
# Then open http://localhost:8888 in your browser
```

2. Open the notebooks in order:
   - `01_common_functions.ipynb` - Common utility functions
   - `02_network_tuning.ipynb` - Network architecture optimization
   - `03_backpropagation_tuning.ipynb` - Backpropagation optimization
   - `04_overfitting_management.ipynb` - Overfitting prevention techniques
   - `05_root_cause_analysis.ipynb` - Practical application exercise

## 📁 Repository Structure

```
├── data/                           # Datasets
│   ├── iris.csv                   # Iris flower classification dataset
│   └── root_cause_analysis.csv    # Incident analysis dataset
├── scripts/                        # Utility scripts
│   ├── setup.sh                   # Environment setup
│   ├── run_notebook.py            # Notebook execution script
│   └── validate_data.py           # Data validation
├── tests/                          # Test files
│   ├── __init__.py
│   ├── test_data_validation.py
│   └── test_model_functions.py
├── docs/                           # Documentation
├── 01_common_functions.ipynb      # Common utility functions
├── 02_network_tuning.ipynb        # Network architecture tuning
├── 03_backpropagation_tuning.ipynb # Backpropagation optimization
├── 04_overfitting_management.ipynb # Overfitting management
├── 05_root_cause_analysis.ipynb   # Root cause analysis exercise
├── requirements.txt               # Core dependencies
├── requirements-dev.txt           # Development dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # This file
```

## 🧪 Datasets

### Iris Dataset
- **Purpose**: Flower classification (setosa, versicolor, virginica)
- **Features**: Sepal length/width, Petal length/width
- **Use Case**: Basic neural network training and optimization

### Root Cause Analysis Dataset
- **Purpose**: Incident analysis and classification
- **Features**: CPU load, memory leak indicators, network delays, error codes
- **Use Case**: Advanced classification and root cause prediction

## 🔧 Key Functions

The `01_common_functions.ipynb` notebook provides essential utilities:

- `get_data()`: Data loading and preprocessing
- `base_model_config()`: Default model configuration
- `create_and_run_model()`: Model creation and training
- `plot_graph()`: Visualization utilities
- `get_optimizer()`: Optimizer selection

## 🧪 Testing

Run the test suite:

```bash
make test
```

Run with coverage:

```bash
make test-cov
```

Run tests in Docker:

```bash
make docker-test
```

## 🚀 CI/CD

This repository includes GitHub Actions workflows for:

- **Continuous Integration**: Automated testing on multiple Python versions
- **Code Quality**: Linting, formatting, and coverage checks
- **Notebook Testing**: Automated execution of all tutorial notebooks
- **Docker Build**: Automated Docker image building and testing
- **Release Management**: Automated releases on version tags

View the workflows in `.github/workflows/` for more details.

## 📊 Learning Path

1. **Start with Common Functions**: Understand the utility functions and data processing
2. **Network Tuning**: Learn about architecture optimization
3. **Backpropagation**: Master learning rate and optimizer tuning
4. **Overfitting Management**: Implement regularization techniques
5. **Root Cause Analysis**: Apply knowledge to real-world scenario

## 🤝 Contributing

This is a learning repository. Feel free to:
- Experiment with different parameters
- Add new optimization techniques
- Improve documentation
- Share your results and insights

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Based on LinkedIn Learning course materials
- Uses standard datasets (Iris, custom incident data)
- Built with TensorFlow/Keras and scikit-learn
