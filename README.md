# Recruitment Task

## Requirements

`python 3.8.10`

## Installation

1. Create virtual environment and activate it

    ```
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   
   # Windows
   py -m venv venv
   .\venv\Scripts\activate
    ```

2. Install packages

    `pip install -r requirements.txt`
    
(if you want to deactivate virtual environment use `deactivate` command)

## Running project

First make sure that you have activated virtual environment (if you are new to this topic please refer to [docs](https://docs.python.org/3/tutorial/venv.html)) and also change directory to `cd recruitment_task`:

- If running project for the first time you should migrate:
    
    `python manage.py migrate`

- Running project:

    `python manage.py runserver`
    
- Running tests, there are two possibilities:

    - `python manage.py test`: using standard Django test mechanism
    
    - `pytest`: using pytest - recommended only if you are familiar with that testing library

## Project introduction

Application which you maintain is about finding investment possibilities for Investors and Projects.

Investor can view a list of Projects that match his criteria and then he can choose which ones he would like to invest into, assuming that he has enough funds.

## Task

1. Add the following API endpoints:
    - list matching projects for investors `/investors/<id>/matches/`
     
    - list matching investors for project `/projects/<id>/matches/`

2. Add field with list of ids of matching investors/matching projects to details view of Project/Investor respectively.

3. Logic of investing into projects is not complete - finish it.

When doing above tasks keep in mind that the **performance** of your solution is important.

### Rules of matchmaking logic

`Project` and `Investor` should be matched when all of the following are true:

1. `Project` will be delivered within `Investor`'s deadline

2. `Investor` has enough funds to invest into `Project`

3. `Investor`'s per project funding amount is greater or equal to amount needed by `Project`

4. `Project` is not already funded


-
forked by Sbtah.
