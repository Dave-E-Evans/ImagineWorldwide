import asyncio

from grpclib.client import Channel

# generated by protoc
from hitchhiker_source_pb2 import GetDownloadsRequest, GetDownloadsReply
from hitchhiker_source_grpc import HitchhikerSourceStub


async def main():
    async with Channel('127.0.0.1', 3001) as channel:
        hitchhiker = HitchhikerSourceStub(channel)

        reply = await hitchhiker.GetDownloads(GetDownloadsRequest(client_id='clientid_1', destination_id='destinationid_1'))
        print(reply.file_list)

if __name__ == '__main__':
    asyncio.run(main())