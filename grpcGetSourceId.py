import asyncio

from grpclib.client import Channel

# generated by protoc
from hitchhiker_source_pb2 import GetSourceIdRequest, GetSourceIdReply
from hitchhiker_source_grpc import HitchhikerSourceStub


async def main():
    async with Channel('127.0.0.1', 3001) as channel:
        hitchhiker = HitchhikerSourceStub(channel)

        reply = await hitchhiker.GetSourceId(GetSourceIdRequest())
        print(reply.source_id)

if __name__ == '__main__':
    asyncio.run(main())