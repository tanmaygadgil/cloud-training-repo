#! /bin/bash
jupyter notebook --generate-config

printf "c = get_config()
c.NotebookApp.ip = '*'
c.NotebookApp.open_browser = False
c.NotebookApp.port = 8888" >> ~/.jupyter/jupyter_notebook_config.py



