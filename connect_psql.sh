#!/usr/bin/bash
psql -d blog_db -U blog_dev -h localhost -p 5432 -L postgres.log -W
