
All commands in this file assume that you are in the directory containing this README.md file.

## Install pre-requisites
Install python3
python3 -m pip install bottle "grpclib[protobuf]" grpcio-tools requests timeloop

## Generate gRPC code
TODO: Add this to a Makefile
python3 -m grpc_tools.protoc -I. --python_out=. --grpclib_python_out=. hitchhiker_source.proto

## To install APK in Android Emulator
~/Library/Android/sdk/platform-tools/adb install countly_test.apk

curl -d '{"key1":"value1", "key2":"value2"}' -H "Content-Type: application/json" -X POST http://localhost:8080/data

curl -d '{"events":}' -H "Content-Type: application/json" -X POST http://localhost:8080/data

curl --request GET \
     --url http://localhost:8080/i?app_key=1234&device_id=device1&events=[{"key": "level_success","count": 4},{"key": "level_fail","count": 2}] \
     --header 'Accept: application/json' 


Things which tend to be fixed for the lifetime of the device are stored in environment variables.
Things which change call by call are passed in as parameters.

## Run the server which will collect metrics over the countly API
```bash
$ LOG_PATH=`pwd`/test_data \
  LOG_PATH_MAX_SIZE=600 \
  LOG_PATH_TARGET_SIZE=350 \
  LOG_PATH_GC_INTERVAL=10 \
  python3 serverMetricsLocal.py
```

## Run the server which will allow fetching of stored metrics over gRPC
```bash
$ LOG_PATH=`pwd`/test_data/countly \
  SOURCE_ID="pilot_01" \
  python3 serverHitchhikerLocal.py
```

## Exercise sending countly events to the server
```bash
$ python3 countlySendEvent.py
```

## Exercise the gRPC GetSourceId API
```bash
$ python3 grpcGetSourceId.py
```

## Exercise the gRPC GetDownloads API
```bash
$ CLIENT_ID="tablet_1" \
  DESTINATION_ID="befit_1" \
  python3 grpcGetDownloads.py
```

To verify the MD5 hash of the downloaded file:
```bash
$ md5 data/countly/received/log-2024-01-12-device_id.json
```

## Exercise the gRPC DownloadFile API
Get some file information from GetDownloads.
```bash
$ CLIENT_ID="tablet_1" \
  DESTINATION_ID="befit_1" \
  python3 grpcGetDownloads.py

CLIENT_ID: tablet_1
DESTINATION_ID: befit_1
[file_id: "3f371b6f6eeea52d6d9bbb309bd4c7b8"
file_name: "log-2024-01-11-device_id.json"
, file_id: "e2c2e5cb838128768519173afa85df9f"
file_name: "log-2024-01-12-device_id.json"
]
```

Download the files by passing that information into DownloadFile
```bash
$ CLIENT_ID="tablet_1" \
  python3 grpcDownloadFile.py \
  3f371b6f6eeea52d6d9bbb309bd4c7b8 log-2024-01-11-device_id.json \
  e2c2e5cb838128768519173afa85df9f log-2024-01-12-device_id.json
```

## Exercise the gRPC MarkDelivered API
Get some file information from GetDownloads.
```bash
$ CLIENT_ID="tablet_1" \
  DESTINATION_ID="befit_1" \
  python3 grpcGetDownloads.py

CLIENT_ID: tablet_1
DESTINATION_ID: befit_1
[file_id: "3f371b6f6eeea52d6d9bbb309bd4c7b8"
file_name: "log-2024-01-11-device_id.json"
, file_id: "e2c2e5cb838128768519173afa85df9f"
file_name: "log-2024-01-12-device_id.json"
]
```

Delete the files by passing that information into MarkDelivered
```bash
$ CLIENT_ID="tablet_1" \
  DESTINATION_ID="befit_1" \
  python3 grpcMarkDelivered.py \
  3f371b6f6eeea52d6d9bbb309bd4c7b8 log-2024-01-11-device_id.json \
  e2c2e5cb838128768519173afa85df9f log-2024-01-12-device_id.json
```