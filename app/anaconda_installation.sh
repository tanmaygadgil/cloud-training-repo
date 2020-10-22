#! /bin/bash
sudo apt-get update -y
sudo apt-get install -y wget 
sudo apt-get install -y git-all 
sudo apt-get install -y bzip2 libxml2-dev
sudo wget https://repo.anaconda.com/archive/Anaconda3-2020.07-Linux-x86_64.sh -O ~/anaconda.sh
bash ~/anaconda.sh -b 
echo "export PATH=~/anaconda3/bin:$PATH" >> ~/.bashrc




# jupyter notebook --generate-config