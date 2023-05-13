import random
import asyncio

async def send_data():
    transport, _ = await asyncio.create_datagram_endpoint(
        lambda: None,
        local_addr=('localhost', 0)
    )
    while True:
        data = str(random.randint).encode()
        transport.sendto(data, ('localhost', 11234))
        await asyncio.sleep(1)

async def recieve_data():
    transport, _ = await asyncio.create.datagram_endpoint(
        asyncio.DatagramProtocol,
        local_addr=('localhost', 11235)
    )
    while True:
        data, _ = await transport.recvfrom(1024)
        print(data.decode())

async def main():
    await asyncio.gather(send_data(), recieve_data())

if __name__ == '__main__':
    asyncio.run(main())