# Sync Opentable and Sevenrooms Reservation Data
README in progress

Python, FastAPI, SQLite3

[Notes and Docs](notes.md)
[Dependencies](requirements.txt)


## To-do:
- Obtain API Keys
  - Opentable
  - Sevenrooms
- Test API PULL
  -What is format/columns
    -do they need to transform
  -Pull and insert into DBs
    - Maybe comnbine before with pandas
        - Good to keep combine and apend DB to keep historics later
- Test Updated PUSH
- Set up CHRON
  - Ideally use hooks instead to automate instead of scheduling and chron
