# Personal Spy

## Setup Process
### Create ```.env``` file and add the following environment variables:
```dotenv
SECRET_KEY=secret_key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
CSRF_TRUSTED_ORIGINS=http://localhost:5420
ALLOWED_ORIGINS=http://localhost:5420

# Database Config
DB_ENGINE=django.db.backends.postgresql
DB_NAME=personal_spy
DB_USER=personal_spy
DB_PASSWORD=db_password
DB_HOST=db
DB_PORT=5432
```
Change the values of the environment variables according to your setup.

### To run the project:
1. **Build the Docker containers**:
    If you are using ```Makefile``` then run the following command:
    ```bash
    make build
    ```
   **OR** build by using following command:
    ```bash
    docker-compose -f docker-compose.yml up -d --build
    ```
2. **Once the project is successfully build you can use following commands to run the project**:
   - **To run the**:
     If you are using ```Makefile``` then run the following command:
     ```bash
     make up
     ```
     **OR**
     ```bash
     docker-compose -f docker-compose.yml up -d
     ```
   - **To Stop The Project**:
     If you are using ```Makefile``` then run the following command:
     ```bash
     make down
     ```
     **OR**
     ```bash
     docker-compose -f docker-compose.yml down
     ```
   
