# API data for cryptos to graphite and redis for analysis
**Collects data from Crypto sites using their api and sends this data to the graphiteapp/graphite-statsd docker instance running on my machine for crypto data analysis - You may have to create ur own graphana instance to view these graphs.**

### Requirements: ###
1. python3
2. graphitesend and redis pip module
3. graphiteapp/graphite-statsd docker instance running on ur machine at 127.0.0.1
4. supervisord to ensure the script is running 24x7
