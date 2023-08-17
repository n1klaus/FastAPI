# Alembic initialization
```
alembic init alembic
```

# Alembic migrations
```
alembic revision --autogenerate -m "create user and blog table migrations"  #analyzes tables and creates a migration file
alembic upgrade head  #executes the migration files to make actual changes in db
```
