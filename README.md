# globat_challenge

To run this api you need to install Docker and build an image with the project.

- If you need to build the image follow this instructions
    - cd repository cloned
    - docker build -t globant_coding_challenge .
    - In docker run the image with another port diferent of the native confirguration, this is with the objetive to test other port different of 5000
    - After that, test the api uploading data or searching in the data base though the api connection 


Name of image: "globant_coding_challenge"

To upload data in the some of the three tables you can use this sentense

curl -X POST -F 'jobs=@/to/path/jobs.csv' http://127.0.0.1:5000/upload
curl -X POST -F 'departments=@/to/path/departments.csv' http://127.0.0.1:5000/upload
curl -X POST -F 'hired_employees=@/to/path/hired-employees.csv' http://127.0.0.1:5000/upload

Only need to take in consideration, change "/to/path/" for the route where you have stored the csv files

About the Data Base.
- This was created in https://api.elephantsql.com/ with a free plan
- The name of the instance id "api_test"