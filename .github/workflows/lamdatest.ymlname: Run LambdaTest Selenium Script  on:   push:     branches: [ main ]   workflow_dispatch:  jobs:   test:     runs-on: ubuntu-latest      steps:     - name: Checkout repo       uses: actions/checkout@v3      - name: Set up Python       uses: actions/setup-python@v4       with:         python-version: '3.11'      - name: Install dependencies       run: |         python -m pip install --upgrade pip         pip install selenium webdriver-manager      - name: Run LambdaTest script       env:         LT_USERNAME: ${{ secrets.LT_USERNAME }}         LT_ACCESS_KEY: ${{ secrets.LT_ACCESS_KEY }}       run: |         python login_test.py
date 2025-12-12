name: Run LambdaTest Selenium Script

on:
  push:
    branches: [ main ]
  workflow_dispatch:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repo
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.11'

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install selenium webdriver-manager

    - name: Run LambdaTest script
      env:
        LT_USERNAME: ${{ secrets.LT_USERNAME }}
        LT_ACCESS_KEY: ${{ secrets.LT_ACCESS_KEY }}
      run: |
        python login_test.py
