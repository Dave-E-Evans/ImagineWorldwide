import asyncio
import logging
import os

from grpclib.client import Channel

# generated by protoc
from hitchhiker_source_pb2 import GetDownloadsRequest, GetDownloadsReply
from hitchhiker_source_grpc import HitchhikerSourceStub

async def main(grpc_host, grpc_port, client_id, destination_id):
    async with Channel(grpc_host, grpc_port) as channel:
        hitchhiker = HitchhikerSourceStub(channel)

        # Call the gRPC
        reply = await hitchhiker.GetDownloads(GetDownloadsRequest(client_id=client_id, destination_id=destination_id))

        # Print the results
        print(reply.file_list)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    # This is the GRPC host that the client will connect to.
    grpc_host = os.environ.get('GRPC_HOST', '127.0.0.1')
    grpc_port = int(os.environ.get('GRPC_PORT', '3001'))

    # This is the client id that the server will use to identify the client.
    client_id = os.environ.get('CLIENT_ID')
    if client_id is None:
        logging.error('CLIENT_ID environment variable is not set!')
        exit(1)
    else:
        logging.info(f'CLIENT_ID: {client_id}')

    # This is the destination id.
    destination_id = os.environ.get('DESTINATION_ID')
    if destination_id is None:
        logging.error('DESTINATION_ID environment variable is not set!')
        exit(1)
    else:
        logging.info(f'DESTINATION_ID: {destination_id}')

    asyncio.run(main(grpc_host=grpc_host, grpc_port=grpc_port, client_id=client_id, destination_id=destination_id))