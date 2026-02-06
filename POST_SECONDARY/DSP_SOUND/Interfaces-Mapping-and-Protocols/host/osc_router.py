#!/usr/bin/env python3
"""Minimal OSC sender scaffold (optional lane)."""
import argparse
from pythonosc.udp_client import SimpleUDPClient

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ip", default="127.0.0.1")
    ap.add_argument("--port", type=int, default=8000)
    ap.add_argument("--address", default="/knob/1")
    ap.add_argument("--value", type=float, default=0.0)
    args = ap.parse_args()

    client = SimpleUDPClient(args.ip, args.port)
    client.send_message(args.address, args.value)
    print("Sent", args.address, args.value)

if __name__ == "__main__":
    main()
