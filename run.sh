#!/bin/bash

python get_content.py
shiny run --log-level debug --host 0.0.0.0 app.py