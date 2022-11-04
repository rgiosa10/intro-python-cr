# Code Review: Intro to Python

#### By Ruben Giosa

#### This repo includes several functions that illustrates skills using dictionaries, loops, lists, and strings. 

<br>

## Technologies Used

* Python
* Git
* Markdown
* Jupyter Notebooks
* `.gitignore`
* `requirements.txt`

</br>

## Description

This repo includes several functions that illustrates skills using dictionaries, loops, lists, and strings. There are four different functions: 1) `list_sayer()` 2) `dict_sayer()` 3) `greatest()` and 4) `zipper()` that leverage either lists or dictionaries as parameters to run according to specific specs.

Added additional functionality to `greatest()` that in the instance that multiple keys share the greatest value, it will pick the key who's first letter come first in the alphabet, instead of the order in which it is found in the dictionary (i.e. `{'cat': 8, 'zebra': 10, 'dog': 10}` it returns the `(10 , 'dog')` instead of `(10 , 'zebra')`).

<br>

## Setup/Installation Requirements

* Go to https://github.com/rgiosa10/intro-python-cr.git to find the specific repository for this website.
* Then open your terminal. I recommend going to your Desktop directory:
    ```bash
    cd Desktop
    ```
* Then clone the repository by inputting: 
  ```bash
  git clone https://github.com/rgiosa10/intro-python-cr.git
  ```
* Go to the new directory or open the directory folder on your desktop:
  ```bash
  cd intro-python-cr
  ```
* Once in the directory you will need to set up a virtual environment in your terminal:
  ```bash
  python3.7 -m venv venv
  ```
* Then activate the environment:
  ```bash
  source venv/bin/activate
  ```
* Install the necessary items with requirements.txt:
  ```bash
    pip install -r requirements.txt
  ```
* With your virtual environment now enabled with proper requirements, open the directory:
  ```bash
  code .
  ```

</br>

## Known Bugs

* No known bugs

<br>

## License

MIT License

Copyright (c) 2022 Ruben Giosa

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

</br>