#!/usr/bin/env python3
import nvidia_smi
import time
import sys
import os
import pyfiglet


def main():
    try:
        nvidia_smi.nvmlInit()
        handle = nvidia_smi.nvmlDeviceGetHandleByIndex(0)
        device_name = nvidia_smi.nvmlDeviceGetName(handle).decode('utf-8')
        
        while True:
            os.system('clear')
            temp = nvidia_smi.nvmlDeviceGetTemperature(handle, nvidia_smi.NVML_TEMPERATURE_GPU)
            
            banner = pyfiglet.figlet_format("   GPU Temp")
            print(f"\033[1;32m{banner}\033[0m")
            print("\033[46;3;30m                      848YF4LK                      \033[0m")
            print("\033[44m=\033[0m"*52)
            print(f"\033[1m                GPU MONITORING TOOL                \033[0m")
            print("\033[44m=\033[0m"*52)
            print(f"\033[1mDevice: {device_name}\033[0m")
            print(f"\033[1mTemp:   {temp}°C\033[0m")
            
            bar = "█" * (temp // 2) + "-" * (50 - (temp // 2))
            print(f"\033[1m[{bar}]\033[0m")
            
            if temp > 80:
                print("\nWARNING: OVERHEAT!")
            
            print("\n\033[1m(Press Ctrl+C to exit)\033[0m")
            time.sleep(1)
            
    except KeyboardInterrupt:
        print("\n[!] Exiting...")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        nvidia_smi.nvmlShutdown()

if __name__ == "__main__":
    main()
