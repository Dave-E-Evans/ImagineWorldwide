
All commands in this file assume that you are in the directory containing this README.md file.

# Setup

## MacBook setup
This code was developed on a MacBook, so instructions are only verified for that platform.
Everything is written in Python3
```bash
brew install python3
python3 -m pip install bottle "grpclib[protobuf]" grpcio-tools requests timeloop
```

The code does not need compiling, although changes to the .proto file will require recompiling.
```bash
python3 -m grpc_tools.protoc -I. --python_out=. --grpclib_python_out=. hitchhiker_source.proto
```
TODO: Add this to some kind of Makefile


## OpenWRT setup
This assumes a fresh install of an OpenWRT image, reachable on 10.0.2.2 with passwordless root ssh.

Install python and make a directory for the server to run in.
```bash
ssh root@10.0.2.2
opkg update && opkg install python3 python3-pip openssh-sftp-server
python3 -m pip install bottle "grpclib[protobuf]" timeloop
mkdir server
exit
```

Copy our server files from the client into the OpenWRT server directory.
```bash
scp serverMetricsLocal.py serverHitchhikerLocal.py hitchhiker_source_pb2.py hitchhiker_source_grpc.py root@10.0.2.2:/server
```

Ports 3000 and 3001 need to be exposed on the router.

## To install supplied APK in Android Emulator
~/Library/Android/sdk/platform-tools/adb install countly_test.apk

# Running the servers

There are two server processes:
* `serverMetricsLocal.py` - collects metrics from the countly API
* `serverHitchhikerLocal.py` - serves metrics to the caller over gRPC

Run each of these in a separate terminal window. To open a terminal
onto the OpenWRT device, run `ssh root@10.0.2.2`

## Run the server which will collect metrics over the countly API
```bash
$ cd server
$ LOG_PATH=`pwd`/test_data \
  LOG_PATH_MAX_SIZE=600 \
  LOG_PATH_TARGET_SIZE=350 \
  LOG_PATH_GC_INTERVAL=10 \
  python3 serverMetricsLocal.py
```

## Run the server which will allow fetching of stored metrics over gRPC
```bash
$ cd server
$ LOG_PATH=`pwd`/test_data/countly \
  SOURCE_ID="pilot_01" \
  python3 serverHitchhikerLocal.py
```

# Manual test commands

Some small Python scripts have been written to help test all of the endpoints.
Things which tend to be fixed for the lifetime of the device are passed via environment variables.
Things which change call by call are passed by command line parameters.

## Exercise sending countly events to the server
```bash
$ COUNTLY_HOST=10.0.2.2 \
  python3 countlySendEvent.py
```

## Exercise the gRPC GetSourceId API
```bash
$ GRPC_HOST=10.0.2.2 \
  python3 grpcGetSourceId.py
```

## Exercise the gRPC GetDownloads API
```bash
$ GRPC_HOST=10.0.2.2 \
  CLIENT_ID="tablet_1" \
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
$ GRPC_HOST=10.0.2.2 \
  CLIENT_ID="tablet_1" \
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
$ GRPC_HOST=10.0.2.2 \
  CLIENT_ID="tablet_1" \
  python3 grpcDownloadFile.py \
  3f371b6f6eeea52d6d9bbb309bd4c7b8 log-2024-01-11-device_id.json \
  e2c2e5cb838128768519173afa85df9f log-2024-01-12-device_id.json
```

## Exercise the gRPC MarkDelivered API
Get some file information from GetDownloads.
```bash
$ GRPC_HOST=10.0.2.2 \
  CLIENT_ID="tablet_1" \
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
$ GRPC_HOST=10.0.2.2 \
  CLIENT_ID="tablet_1" \
  DESTINATION_ID="befit_1" \
  python3 grpcMarkDelivered.py \
  3f371b6f6eeea52d6d9bbb309bd4c7b8 log-2024-01-11-device_id.json \
  e2c2e5cb838128768519173afa85df9f log-2024-01-12-device_id.json
```

# Automated test command
An automated test has been written which will start the servers and exercise
a number of the APIs and assert the expected behaviour.

```bash
$ python testIntegration.py
```

TODO: Write unit tests. Given the amount of access to the filesystem, I felt
that writing unit tests requiring an abstraction over the filesystem would
obfuscate the code. Given the time available, I opted for an integration test.

# Code structure
TODO 
The code is currently not structured in a manner which would be suitable for
re-use. Moving some code into modules would be a good next step.