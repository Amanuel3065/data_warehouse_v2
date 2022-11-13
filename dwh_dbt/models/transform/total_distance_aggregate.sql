with source_data as (
    select *
    from {{ref('feature_casting')}}
),
final as (
    select 
    vehicle_type,
    SUM(traveled_d)
    from feature_casting
    group by
    vehicle_type 

)
SELECT *
FROM final