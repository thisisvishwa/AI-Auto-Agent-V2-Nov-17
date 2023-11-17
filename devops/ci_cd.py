```python
import os
from github import Github

# CI/CD pipeline setup function
def ci_cd_pipeline():
    # Accessing Github with a personal access token
    g = Github(os.getenv('GITHUB_TOKEN'))

    # Accessing the repository
    repo = g.get_repo("username/repo_name")

    # Creating a new file for the CI/CD pipeline in the repository
    repo.create_file("/.github/workflows/ci_cd.yml", "CI/CD pipeline setup", get_ci_cd_config())

# Function to get the CI/CD configuration
def get_ci_cd_config():
    return """
    name: CI/CD pipeline

    on:
      push:
        branches: [ main ]
      pull_request:
        branches: [ main ]

    jobs:
      build:

        runs-on: ubuntu-latest

        steps:
        - uses: actions/checkout@v2
        - name: Set up Python 3.8
          uses: actions/setup-python@v2
          with:
            python-version: 3.8
        - name: Install dependencies
          run: |
            python -m pip install --upgrade pip
            pip install -r requirements.txt
        - name: Lint with flake8
          run: |
            pip install flake8
            flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        - name: Test with pytest
          run: |
            pip install pytest
            pytest
    """

if __name__ == "__main__":
    ci_cd_pipeline()
```