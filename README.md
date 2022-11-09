# data_warehouse_v2
**(Remake of week 5 challenge)**

## Tech stack with PostgreSql, DBT, Airflow
* This project aims to build a fully dockerized data warehousing tech stack. It utilizes different data engineering tools like PostgreSQL, Airflow, DBT and Redash. PostgreSql is used for data ware house, DBT for data transforming and airflow for automation and orchestrations. Finally, a redash dashboard will be built by connecting it to our data warehouse.
* The Data used for this project is from open-source dataset called PNeuma which is an open large-scale dataset of naturalistic trajectories of half a million vehicles that have been collected by a one-of-a-kind experiment by a swarm of drones in the congested downtown area of Athens, Greece.

### Apache Airflow
* Apache Airflow is a platform to programmatically author, schedule, and monitor workflows. It is one of the most robust ETL (Extract, Transform, Load) workflow management tools, used by Data Engineers for orchestrating workflows or pipelines. Read more: https://airflow.apache.org/docs/

### PostgreSql
* PostgreSql is a useful and common data warehouse tool maintained by an active community. It can also handle more than just one kind of data processing, which makes it a pretty compelling option. PostgreSQL works with almost any kind of programming language. Read more: https://www.postgresql.org/

### DBT 
* DBT enables analytics engineers to transform data in their warehouses by simply writing select statements. dbt handles turning these select statements into tables and views. DBT is a data transformation tool that does the ‘T’ in ELT. it doesn’t extract or load data, but it’s extremely good at transforming data that’s already loaded into your warehouse. Read more: https://docs.getdbt.com/docs/building-a-dbt-project/documentation

### Redash
* A dashboard building tool. Read more: https://redash.io/

