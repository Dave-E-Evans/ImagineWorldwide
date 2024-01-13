import bottle
from bottle import request, route, run, template, HTTPError
from datetime import timedelta
import json
import logging
import os
from timeloop import Timeloop

logging.basicConfig(level=logging.INFO)

# This is where the files are stored
log_path = os.environ.get('LOG_PATH')
if log_path is None:
    logging.error('LOG_PATH environment variable is not set!')
    exit(1)
else:
    logging.info(f'LOG_PATH: {log_path}')

# These are the sub-directories within LOG_PATH that represent the state of the file
countly_dir = 'countly'
received_dir = 'received'

try:
    # This is the maximum amount of storage we should use (in bytes) before discarding files
    log_path_max_size = os.environ.get('LOG_PATH_MAX_SIZE')
    if log_path_max_size is None:
        logging.error('LOG_PATH_MAX_SIZE environment variable is not set!')
        exit(1)
    else:
        log_path_max_size = int(log_path_max_size)
        logging.info(f'LOG_PATH_MAX_SIZE: {log_path_max_size} bytes')

    # This is the amount of storage we should target to use (in bytes) when discarding files
    log_path_target_size = os.environ.get('LOG_PATH_TARGET_SIZE')
    if log_path_target_size is None:
        logging.error('LOG_PATH_TARGET_SIZE environment variable is not set!')
        exit(1)
    else:
        log_path_target_size = int(log_path_target_size)
        logging.info(f'LOG_PATH_TARGET_SIZE: {log_path_target_size} bytes')

    # This is the frequency (in seconds) to garbage collect
    log_path_gc_interval = os.environ.get('LOG_PATH_GC_INTERVAL')
    if log_path_gc_interval is None:
        logging.error('LOG_PATH_GC_INTERVAL environment variable is not set!')
        exit(1)
    else:
        log_path_gc_interval = int(log_path_gc_interval)
        logging.info(f'LOG_PATH_GC_INTERVAL: {log_path_gc_interval} seconds')

except Exception as e:
    logging.error(f'Exception: {e}')
    exit(1)


PATH_MAP = {"i": countly_dir}
JSON_VALUES = ["events"]

app = bottle.default_app()

# We use this to periodically check the disk usage is within limits
tl = Timeloop()
@tl.job(interval=timedelta(seconds=log_path_gc_interval))
def check_disk_usage():
    # Sum all of the files in the log_path
    log_path_size = 0
    for file in os.listdir(os.path.join(log_path, countly_dir, received_dir)):
        try:
            file_path = os.path.join(log_path, countly_dir, received_dir, file)
            # Skip unless it is a file
            if not os.path.isfile(file_path):
                continue

            # Get the size of the file
            size = os.path.getsize(file_path)
            # logging.debug(f'File {file_path} size is {size} bytes')
            log_path_size += size
        except Exception as e:
            logging.error(f'Exception: {e}')
            continue

    logging.info(f"Checking disk usage (current = {log_path_size}, max = {log_path_max_size})")

    # If the current size is greater than the max size, then delete files until we are below the target size
    if log_path_size > log_path_max_size:
        logging.info(f"Removing files to reduce disk usage to below {log_path_target_size} bytes")

        # Go through all of the files again. Because they are named starting with timestamp YYYY-MM-DD, 
        # then the default alphabetic return order is also the oldest files first.
        for file in sorted(os.listdir(os.path.join(log_path, countly_dir, received_dir))):
            try:
                file_path = os.path.join(log_path, countly_dir, received_dir, file)
                # Skip unless it is a file
                if not os.path.isfile(file_path):
                    continue

                # Get the size of the file
                size = os.path.getsize(file_path)

                # Delete the file
                logging.info(f"Removing {file_path}")
                os.remove(file_path)

                # Subtract the size of the deleted file from the total
                log_path_size -= size

                # If we are below the target size, then stop deleting files
                if log_path_size < log_path_target_size:
                    logging.info(f"Disk usage should now be {log_path_size} bytes")
                    break
                
            except Exception as e:
                logging.error(f'Exception: {e}')
                continue


def save_request(path, req):
    # TODO: Read the api_key and ensure that the request is authorised

    app_dir = PATH_MAP.get(path)
    if not app_dir:
        return False
    
    logging.info("Saving new request: " + app_dir)
    
    for key in JSON_VALUES:
        value = req.params.get(key)
        if value is not None:
            # TODO Replace with a try/catch
            req.params.replace(key, json.loads(value))

    timestamp = req.params.get("timestamp", default="UNKNOWN_TIMESTAMP")
    device_id = req.params.get("device_id", default="UNKNOWN_DEVICE")

    filename = "log-{timestamp}-{device_id}".format(
        timestamp=timestamp, device_id=device_id)
    # TODO Replace with a try/catch
    output = json.dumps(dict(req.params.items()))
    
    log_path_initial = os.path.join(log_path, app_dir, received_dir)
    os.makedirs(log_path_initial, exist_ok=True)
    file_path_initial = os.path.join(log_path_initial, filename)
    file_path = file_path_initial + ".json"
    count = 0
    
    while os.path.exists(file_path):
        file_path = file_path_initial + "-" + str(count) + ".json"
        count += 1

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(output)
    
    return True

# Remote config not supported
@app.route('/o/sdk', method='GET')
def index():
    return json.dumps({"result": "success"})

@app.route('/<path>', method='GET')
def index(path=None):
    logging.info("GET: " + path)
    if save_request(path, request):
        return json.dumps({"result": "success"})
    raise HTTPError(404, "Not found")

if __name__ == "__main__":
    tl.start(block=False)

    port = os.environ.get('PORT', 3000)
    app.run(port=port)

#TODO: Unit tests
