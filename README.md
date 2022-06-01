[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# API Ingestion Pipeline

This repository is responsible for ingest data from an external API, here I'm using [Faker API](https://fakerapi.it/en), anonymize the data, store it in a database and generate a report.
The database used is [SQLite](https://www.sqlite.org/index.html)

## Getting Started

Before you start getting your hands dirty it's important that you learn the concepts behind the code structure.

Our architecture is based on `Clean Architecture`, if you want to get into the details about this architecture
you can take a look at [Robert C. Martin's blog post](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

As mentioned, our architecture is _based_ on `Clean Architecture` so there are some minor differences, this is how the files should be organized:

```
src/
    commom/
    extractor/
    handlers/
    loader/
    transformer/
tests/
    unit/
```

## Prerequisites

These instructions will get you a copy of the service up and running on your local machine for development and testing purposes.

Make sure you have all the following prerequisites:

### Python

This service uses Python version 3.8. To download and install the version got to the python page [here](https://www.python.org/downloads/).


## How to execute

After cloning this repository, on the root folder just type `make`
The Makefile will install the dependencies and execute the pipeline and the report

### The report

This repository execute three queries to retrieve and print the result to answer the questions below
```
1- Which percentage of users live in Germany and use Gmail as an email provider?
2- Which are the top three countries in our database that use Gmail as an email
provider?
3- How many people over 60 years use Gmail as an email provider?
```