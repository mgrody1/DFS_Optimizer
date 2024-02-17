# DFS Optimizer Project

The DFS Optimizer project is designed to analyze and optimize Daily Fantasy Sports (DFS) lineups for baseball, with a focus on DraftKings contests. It involves scraping historical and live data, storing it in a SQL database, and using optimization techniques to generate winning lineups.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9 or higher
- Pipenv for dependency management
- MySQL installed and running on your local machine or accessible remotely
- Git for version control

### Installation

1. **Clone the Repository**

2. **Set Up the Virtual Environment and Install Dependencies**

    ```
    pip install pipenv
    pipenv install
    ```

    This command reads the `Pipfile` and installs the required dependencies into a new virtual environment.

3. **Activate the Virtual Environment**

    ```
    pipenv shell
    ```

    This command activates the virtual environment, ensuring that you're using the project's specific Python interpreter and dependencies.

4. **Set Up the Database Configuration**

    - Copy the `db_config_template.yml` to a new file named `db_config.yml` and fill in your database credentials:
        ```
        cp sql/db_config_template.yml sql/db_config.yml
        ```
    - Edit `sql/db_config.yml` with your MySQL user, password, host, and database name.

### Setting Up in VS Code

1. **Open the Project in VS Code**

    Open the root folder of the project in VS Code.

2. **Select the Python Interpreter**

    - Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P` on macOS).
    - Type and select "Python: Select Interpreter".
    - Choose the interpreter that matches the virtual environment created by Pipenv. It should look something like `.venv` or `pipenv` in the path.

## Versioning

We use Git for version control. For the versions available, see the [tags on this repository](https://github.com/yourusername/dfs_optimizer/tags).

## License

This project is licensed under the MIT License - see the LICENSE.md file for details.
