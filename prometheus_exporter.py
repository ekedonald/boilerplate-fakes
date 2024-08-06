from prometheus_client import start_http_server, Summary
import time

LEAD_TIME = Summary('lead_time_for_changes', 'Lead time for changes')
MTTR = Summary('mean_time_to_recovery', 'Mean time to recovery')
CHANGE_FAILURE_RATE = Summary('change_failure_rate', 'Change failure rate')

def process_request(t):
    # Simulate lead time for changes
    LEAD_TIME.observe(t)
    # Simulate MTTR
    MTTR.observe(t)
    # Simulate change failure rate
    CHANGE_FAILURE_RATE.observe(t)

if __name__ == '__main__':
    start_http_server(8000)
    while True:
        process_request(time.time() % 10)
        time.sleep(1)
