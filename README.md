# AWS Simple Web GUI

As name states, this is simple (very simple) Web GUI

The purpose of this is to facilitate my research into building infrastructure in AWS for 2-tier application


## Usage
This application could be spin up locally
1. `conda env create -f conda_env.yml`
2. `conda activate ...`
3. `pip install -r requirements.txt`
4. `uvicorn main:app --reload`


## Notes:
1. This project has Action pipeline that builds Docker image for this application and pushes image into AWS ECR
