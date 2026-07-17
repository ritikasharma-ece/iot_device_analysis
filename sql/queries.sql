-- OPERATIONAL EFFICIENCY
-- #1 top 3 engineers who have completed most maintenance tasks?
select engineer,count(status) as tasks_completed from maintenance
where status ='Completed' 
group by engineer order by tasks_completed desc;

-- CRITICAL ASSET TRACKING
-- #2 Identify all unique device IDs that have experienced an issue related to 'Antenna Replacement'
select distinct device_id from maintenance where issue = 'Antenna Replacement' group by device_id order by device_id asc;

-- COST AND RISK ANALYSIS 
-- #3 Calculate the total number of failures per factory.
select count(f.failure_id) as failure_count from failures f 
join devices d on f.device_id = d. device_id 
group by d.factory_id order by failure_count asc;

-- PROACTIVE ALERTS
-- #4 list all devices that have had MORE THAN 2 maintenance records
select device_id from maintenance
group by device_id
having count(maintenance_date)>2
order by device_id asc;

-- PRODUCT PRIORITIZATION
-- #5 List all distinct issues handled by 'Rohit Singh' or 'Rahul Sharma'
select distinct issue from maintenance
where engineer in ('Rohit Singh','Rahul Sharma') ;

-- ADVANCED BENCHMARKING
-- #6 Find all factories that have a total failure count HIGHER than the average failure count across all factories in the system.
WITH FactoryFailures AS (
    SELECT 
        fa.factory_name,
        COUNT(f.failure_id) AS total_failures
    FROM failures f
    JOIN devices d ON f.device_id = d.device_id
    JOIN factories fa ON d.factory_id = fa.factory_id
    GROUP BY fa.factory_name
),
AverageSystemFailures AS (
    SELECT AVG(total_failures) AS avg_failures FROM FactoryFailures
)
SELECT factory_name, total_failures
FROM FactoryFailures
WHERE total_failures > (SELECT avg_failures FROM AverageSystemFailures);

-- Predictive Downtime Tracking (Window Functions)
-- #calculate the exact number of days that passed between its current maintenance date and its previous maintenance date.
SELECT 
    device_id,
    maintenance_date,
    issue,
    LAG(maintenance_date) OVER (PARTITION BY device_id ORDER BY maintenance_date) AS previous_maintenance_date,
    maintenance_date - LAG(maintenance_date) OVER (PARTITION BY device_id ORDER BY maintenance_date) AS days_between_repairs
FROM maintenance;



