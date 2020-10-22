#! /bin/bash
sudo apt-get update -y
sudo apt-get install -y wget 
sudo apt-get install -y git-all 
sudo apt-get install -y bzip2 libxml2-dev
# wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
# bash ~/miniconda.sh -b -p $HOME/miniconda
# sudo wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
# bash Miniconda3-latest-Linux-x86_64.sh
sudo wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh
bash ~/anaconda.sh -b 
# bash Anaconda3-2020.07-Linux-x86_64.sh
printf "export PATH="~/anaconda3/bin:$PATH"\n" >> ~/.bashrc
. ~/.bashrc
conda init

# conda install -y scikit-learn pandas jupyter ipython
# conda install -c conda-forge xgboost -y
# conda install -c conda-forge matplotlib -y
# conda install -c conda-forge seaborn -y
# conda install -c conda-forge flask -y
# conda install -c conda-forge flask-restful -y


# jupyter notebook --generate-config