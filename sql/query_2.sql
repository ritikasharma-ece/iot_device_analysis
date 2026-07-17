-- MTTR (MEAN TIME TO REPAIR) BY ENGINEER
-- #8 Calculates the average number of days it takes each engineer to resolve an issue from the day it failed.
-- QUESTION 8: Mean Time To Repair (MTTR) by Engineer
-- QUESTION 8: Mean Time To Repair (MTTR) by Engineer (Fixed Version)
SELECT 
    m.engineer,
    COUNT(m.maintenance_id) AS total_repairs,
    ROUND(AVG(EXTRACT(EPOCH FROM (m.maintenance_date::TIMESTAMP - f.timestamp)) / 86400)::NUMERIC, 1) AS mean_time_to_repair_days
FROM maintenance m
JOIN failures f ON m.failure_id = f.failure_id
GROUP BY m.engineer
ORDER BY mean_time_to_repair_days ASC;

-- Mean Time Between Failures (MTBF) System Baseline
-- #9 Calculates the average uptime days across the entire device fleet between consecutive breakdowns. 
-- QUESTION 9: Mean Time Between Failures (MTBF) System Baseline
WITH NextFailure AS (
    SELECT 
        device_id,
        timestamp AS failure_timestamp,
        LEAD(timestamp) OVER (PARTITION BY device_id ORDER BY timestamp) AS next_failure_timestamp
    FROM failures
),
UptimeIntervals AS (
    SELECT 
        device_id,
        EXTRACT(EPOCH FROM (next_failure_timestamp - failure_timestamp)) / 86400 AS days_between_failures
    FROM NextFailure
    WHERE next_failure_timestamp IS NOT NULL
)
SELECT 
    COUNT(*) AS total_tracked_intervals,
    ROUND(AVG(days_between_failures)::NUMERIC, 2) AS system_mtbf_days
FROM UptimeIntervals;


-- Financial Impact & Downtime Cost Analysis
-- #10 Calculate the total repair cost and total downtime minutes grouped by failure type.
-- #11 Calculate a "Cost Per Downtime Minute" metric to see which issue type is the most expensive leak for the factory network.
-- QUESTION 13: Financial Impact & Downtime Cost Analysis
-- Calculate the total repair cost and total downtime minutes grouped by failure type.
-- Also, calculate a "Cost Per Downtime Minute" metric to see which issue type is the most expensive leak for the factory network.
SELECT 
    f.failure_type,
    COUNT(f.failure_id) AS total_failures,
    SUM(f.downtime_minutes) AS total_downtime_mins,
    SUM(m.repair_cost) AS total_repair_costs_usd,
    ROUND(AVG(m.repair_cost)::NUMERIC, 2) AS avg_repair_cost_usd,
    ROUND((SUM(m.repair_cost)::NUMERIC / NULLIF(SUM(f.downtime_minutes), 0)), 2) AS cost_per_downtime_minute
FROM failures f
JOIN maintenance m ON f.failure_id = m.failure_id
GROUP BY f.failure_type
ORDER BY total_repair_costs_usd DESC;

-- Cumulative Maintenance Cost & Fleet Downtime Trajectory
-- #12 Calculate the total repair costs and downtime minutes incurred each day,
-- then use an ordered window function to compute a running cumulative total for both metrics.
WITH DailyTotals AS (
    SELECT
        m.maintenance_date::DATE AS operational_date,
        SUM(m.repair_cost) AS daily_cost,
        SUM(f.downtime_minutes) AS daily_downtime
    FROM maintenance m
    LEFT JOIN failures f ON m.failure_id = f.failure_id
    GROUP BY m.maintenance_date::DATE
)
SELECT
    operational_date,
    daily_cost,
    SUM(daily_cost) OVER (ORDER BY operational_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_cost_usd,
    daily_downtime,
    SUM(daily_downtime) OVER (ORDER BY operational_date ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) AS cumulative_downtime_mins
FROM DailyTotals
ORDER BY operational_date ASC;

