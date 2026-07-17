import pandas as pd

factories = [
    {
        "factory_id":"F001",
        "factory_name":"Factory Alpha",
        "city":"Pune",
        "temp_bias":2,
        "humidity":45,
        "signal_quality":"Excellent"
    },
    {
        "factory_id":"F002",
        "factory_name":"Factory Beta",
        "city":"Chennai",
        "temp_bias":6,
        "humidity":85,
        "signal_quality":"Average"
    },
    {
        "factory_id":"F003",
        "factory_name":"Factory Gamma",
        "city":"Delhi",
        "temp_bias":4,
        "humidity":55,
        "signal_quality":"Good"
    },
    {
        "factory_id":"F004",
        "factory_name":"Factory Delta",
        "city":"Noida",
        "temp_bias":3,
        "humidity":60,
        "signal_quality":"Good"
    },
    {
        "factory_id":"F005",
        "factory_name":"Factory Omega",
        "city":"Bengaluru",
        "temp_bias":1,
        "humidity":40,
        "signal_quality":"Excellent"
    }
]

df = pd.DataFrame(factories)

df.to_csv("data/factories.csv",index=False)

print(df)