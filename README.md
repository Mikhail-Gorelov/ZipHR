# ZipHR technical interview

### How to use:

#### Clone the repo:

    git clone https://github.com/Mikhail-Gorelov/ZipHR.git ./project_name


#### Before running add your superuser email/password and project name in docker/dev/env/.data.env file

    SUPERUSER_EMAIL=example@email.com
    SUPERUSER_PASSWORD=secretp@ssword
    MICROSERVICE_TITLE=MyProject

#### Run the local develop server:

    docker-compose up -d --build
    docker-compose logs -f
    
##### Server will bind 8008 port. You can get access to server by browser [http://localhost:8008](http://localhost:8008)

#### To run locally module tests from directory project_name/:

    python manage.py test

#### Watch coverage from directory project_name/:

    coverage run manage.py test

    coverage erase

#### If you want to output the results on the command line:

    coverage report
