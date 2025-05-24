# nord_health Challenge

This is for the NorthHealth challenge. 

## NOTES
* I took an OOP approch.  
* In the challenge is shown only examples with more than 2 tupples, as I was not sure if it was a requirement or not I added an optional parameter to choose from.
* In example the array is a set but I added a clean in case a list is sent.   
* The app had 0 libraries to work, the only things to install were standar quality code libraries. 
* did not dockerize becuause 

## Prerequisites

- [pyenv](https://github.com/pyenv/pyenv) installed

## Setup

1. **Install Python version:**

    ```sh
    pyenv install 3.11.8
    ```

2. **Set local Python version:**

    ```sh
    pyenv local 3.11.8
    ```

3. **Create and activate virtual environment:**

    ```sh
    pyenv virtualenv north_venv
    pyenv activate north_venv
    ```

4. **Install dependencies:**

    ```sh
    pip install -r requirements-dev.txt
    ```

## Usage

You can ether run  
    ```sh
    python main.sh
    ```
or run the tests. 

    ```sh
    pytest
    ```
