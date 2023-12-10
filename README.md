# AWS Simple Web GUI

As name states, this is simple (very simple) Web GUI

This project is part of one big project where I research how to build infrastructure in AWS for 2-tier application (and application as well, of course) :
1. [Terraform](https://github.com/MikhailMS/aws-2tier-lambda-api) contains all the terraform code to deploy required infra & application code
2. Simple Web GUI (this project) contains code for simple Web GUI to bridge the gap between user and Lambda functions
3. [Lambda functions](https://github.com/MikhailMS/aws-lambda-functions) contain code for 3 Lambda functions that replicate simple backend functions
    1. `return_ip`         - returns IP address of the Lambda function
    2. `fetch_go_versions` - returns JSON with recent 5 Go versions
    3. `custom_auth`       - custom Lambda authorizer (only supports payload format `version 1.0`) that controls access to functions `1 & 2` when calling via API Gateway
    4. `custom_auth_v2`    - custom Lambda authorizer (only supports payload format `version 2.0`) that controls access to functions `1 & 2` when calling via API Gateway


## Usage
This application could be spin up locally
1. `conda env create -f conda_env.yml`
2. `conda activate ...`
3. `pip install -r requirements.txt`
4. `uvicorn main:app --reload`


## Notes:
1. This project has Action pipeline that builds Docker image for this application and pushes image into AWS ECR
