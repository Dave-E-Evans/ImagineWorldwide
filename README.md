

## Install pre-requisites
Install python3
python3 -m pip install bottle "grpclib[protobuf]" grpcio-tools requests

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