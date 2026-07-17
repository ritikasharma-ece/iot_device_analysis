# IoT Device Maintenance and Analytics Platform

This project is a data analysis system for tracking enterprise factory machines and electronic devices. It uses sensor logs, plant locations, failure records, and repair histories to help operations teams find equipment problems, fix breakdowns faster, and reduce overall repair costs.

## Technical Stack
* Database: PostgreSQL 18
* Language: SQL
* Methods used: Relational joins, date and time filtering, group by aggregations, case statements, common table expressions (CTEs), and window functions like LAG.

## Business and Operational Problems Solved
The SQL script answers specific questions that help teams manage operations:
1. Engineer Performance: Finds the top 3 repair technicians by counting their completed tasks to help balance workloads.
2. Targeted Asset Tracking: Pinpoints specific technical bugs, like antenna replacements, that happened specifically during January 2026.
3. Factory Risk Analysis: Connects machine failures to their physical factory locations to show which plants have the most downtime.
4. Chronic Problem Alerts: Flags specific machine IDs that have broken down more than twice for the exact same issue.
5. Product Patch Prioritization: Groups historical repair logs so product managers know whether to invest in hardware updates or software patches first.
6. Benchmarking Performance: Uses a CTE to find which individual factories have higher failure rates than the network average.
7. Machine Lifespan Tracking: Uses the LAG window function to calculate the exact number of days a device runs properly between consecutive breakdowns.

## Project Structure
* /data: Folder containing the raw data tables in CSV format (devices, factories, failures, maintenance, sensor logs).
* queries.sql: The main SQL script containing all the baseline and advanced database queries.