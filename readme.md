# GREASE
###### Event Driven Python Execution Engine

[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://travis-ci.org/target/grease)
[![AppVeyor](https://img.shields.io/appveyor/ci/lemoney/grease.svg)](https://ci.appveyor.com/project/lemoney/grease)
[![Current Version](https://badge.fury.io/py/tgt-grease.svg)](https://pypi.python.org/pypi/tgt-grease)
[![Read the Docs](https://img.shields.io/readthedocs/pip.svg)](https://grease.readthedocs.io/)
[![License](https://img.shields.io/badge/license-MIT-brightgreen.svg)](https://github.com/target/grease/blob/master/LICENSE)


## GREASE
  * Guest
  * Reliability
  * Engineering
  * Automation
  * Solution
  * Engine
  
## What it does

GREASE is a system to enable automation via configuration for events
and executing related commands (via a regular python class)

## How it works

GREASE runs 24/7/365 monitoring events you define and 
based on configuration can act on these sources. These actions
can be anything you can do in python.

Out of the box GREASE is very minimal, it is but an engine. Similar
to Django, you write your application, GREASE just serves it. 

## Getting the Docs

  1. Install sphinx `pip install sphinx`
  2. generate the docs by running `make html`
  3. Use a web browser to read the docs starting at `<project root>/docs/_build/index.html`
     
## Installing

Python 3.7+ required!
  
### Via PIP

Simply run `pip install tgt_grease`

### Manually

  1. Clone this repo to your machine
  2. from the created directory run `python setup.py install`
