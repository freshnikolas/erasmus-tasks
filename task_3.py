import random
import asyncio

async def send_data():
    loop = asyncio.get_running_loop()
    # creates a UDP Datagram with only the transport as an output
    transport, _ = await loop.create_datagram_endpoint(
        # disregards the protocol
        lambda: None,
        # sets the transport and writes it in the RAM
        local_addr=('localhost', 0)
    )
    while True:
        # encodes the string into a byte-array, needed for transporting data via UDP
        data = str(random.randint).encode()
        # sends the data to the 11234 socket
        transport.sendto(data, ('localhost', 11234))
        # waits for 1 second
        await asyncio.sleep(1)

async def recieve_data():
    loop = asyncio.get_running_loop()
    transport, _ = await loop.create_datagram_endpoint(
        # creates a protocol with help of the DatagramProtocol Class
        asyncio.DatagramProtocol,
        # recieves data via the 11235 socket
        local_addr=('localhost', 11235)
    )
    while True:
        # saves the recieved data and disregards the ip-adress and sockets 
        data, _ = await transport.recvfrom(1024)
        # decodes back into string and prints it
        print("Recieved data: ", data.decode())

async def main():
    # .gather allows to combine severak asynchronous funtions and let them operate at the same time 
    await asyncio.gather(send_data(), recieve_data())

# used to be easier implemented in future projects
if __name__ == '__main__':
    asyncio.run(main())