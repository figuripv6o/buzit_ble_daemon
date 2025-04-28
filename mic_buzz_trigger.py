import asyncio
import sounddevice as sd
import numpy as np
from bleak import BleakClient

device_address = "XX:XX:XX:XX:XX:XX"  # <-- Replace this with your real BLE MAC
buzz_char_uuid = "0000ffe1-0000-1000-8000-00805f9b34fb"
buzz_data = bytearray([0x01])

async def buzz_device(address):
    try:
        async with BleakClient(address) as client:
            if await client.is_connected():
                await client.write_gatt_char(buzz_char_uuid, buzz_data)
                print("Buzz sent!")
    except Exception as e:
        print("Buzz error:", e)

def listen_for_noise(threshold=0.05):
    print("Listening for noise...")
    def callback(indata, frames, time, status):
        volume_norm = np.linalg.norm(indata) * 10
        if volume_norm > threshold:
            print("Noise detected! Buzzing device...")
            asyncio.run(buzz_device(device_address))
    with sd.InputStream(callback=callback):
        while True:
            sd.sleep(1000)

if __name__ == "__main__":
    listen_for_noise()
