# flask_ticket

Simple dashboard built with Flask and PostgreSQL to see status of bugs tickets.

<!-- TOC -->

- [flask_ticket](#flask_ticket)
  - [Project](#project)
    - [Setting up PostgreSQL server](#setting-up-postgresql-server)
    - [Installing PostgreSQL 9.6 client](#installing-postgresql-96-client)
    - [Testing connection from Workstation](#testing-connection-from-workstation)
    - [Creating the Virtualenv](#creating-the-virtualenv)
  - [Project Structure](#project-structure)
  - [Usage](#usage)
    - [Workstation](#workstation)
  - [References](#references)

<!-- /TOC -->

## Project

Create a dashboard that we can use to query a PostgreSQL database to see the status of various bug tickets that exists in your system. The fields are:

1. Name (required)
2. Status (required), available options are:
   - 0 (Reported)
   - 1 (In Progress)
   - 2 (In Review)
   - 3 (Resolved)
3. URL (optional)

With this information you'll need to do a few things:

* Render a listing view at `/tickets`
* Render an individual ticket at `/tickets/:id`
* Provide a JSON API for `/api/tickets` and `/api/tickets/:id` that returns the JSON serialized ticket information.

### Setting up PostgreSQL server

Before we begin, we're going to need a PostgreSQL database to work with. The data folder contains a `dump.sql` file that is the output of `pg_dump` that we'll use on a CentOS 7 cloud server to create and run our database.

The PostgreSQL database that runs on a separate server is accessible using the default port (5432). These are the database details that you'll need.

1. user - `dashboard`
2. database - `dashboard`
3. password - `secure_password`
4. table - `ticket`
   * id - (UUID, required, automatic) unique identifier
   * name - (string, 100 character limit, required) name of ticket
   * status - (integer, required, default 0) state of ticket (see info above)
   * url - (string, 100 character limit, optional)

### Installing PostgreSQL 9.6 client

On our development machine, we'll need to make sure that we have the Postgres client installed. The version needs to be 9.6.6.

On Red-hat and CentOS systems we'll use the following:

```bash
$ wget https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-redhat-repo-latest.noarch.rpm
$ sudo yum install -y pgdg-redhat-repo-latest.noarch.rpm
$ sudo yum update -y
$ sudo yum autoremove -y postgresql
$ sudo yum install -y postgresql96
```

On Debian systems, the equivalent would be:

```bash
$ sudo apt-get install postgres-client-9.6
```

### Testing connection from Workstation

Let's make sure that we can connect to the PostgreSQL server from our development machine by running the following command:

*Note: You'll need to substitute in your database values for [USERNAME], [PASSWORD] and [SERVER_IP].*

```bash
$ psql postgres://[USERNAME]:[PASSWORD]@[SERVER_IP]:5432/dashboard -c "SELECT count(id) FROM ticket;"
```

### Creating the Virtualenv

We'll start by cloning this repository to our workstation. Then, we'll install `pipenv` and create a Python 3 virtualenv for this project.

```bash
$ git clone https://github.com/dennislwm/flask_ticket
$ cd flask_ticket
$ pip3.6 install --user pipenv
$ pipenv --python $(which python3.6) install flask psycopg2 Flask-SQLAlchemy
```

To activate our new virtualenv, we use the command `pipenv shell`, and to deactivate it we use `exit`.

---
## Project Structure

     flask_ticket/                    <-- Root of your project
       |- __init__.py                 <-- Python module to create Flask app
       |- .gitignore                  <-- GitHub ignore 
       |- config.py                   <-- Python module to configure database
       |- models.py                   <-- Python module to create ORM
       |- Pipfile                     <-- Pipenv 
       |- Pipfile.lock                <-- Pipenv lock 
       |- README.md                   <-- GitHub README markdown 
       +- data/
          |- dump.sql                 <-- Sample database
       +- static/
       +- templates/                  <-- Jinja templates

---
## Usage

### Workstation

Before we can test the Flask application, we need to configure environment variables.

```bash
(flask_ticket) $ export FLASK_ENV=development
(flask_ticket) $ export FLASK_APP="."
```

We'll run the application in a separate terminal instance so that we can keep it running, and it will auto reload any code changes that we make.

```bash
(flask_ticket) $ flask run --host=0.0.0.0 --port=3000
```

---
## References

* [How to Dump and Restore PostgreSQL Database](https://www.netguru.com/blog/how-to-dump-and-restore-postgresql-database)