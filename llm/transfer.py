import subprocess
import json
import os

def transfer_eth(to_address: str, amount: float):
    try:
       
        current_dir = os.path.dirname(os.path.abspath(__file__))
        js_path = os.path.join(current_dir, '..', 'web3', 'transfer.js')
        
        print(f"Executing Node script at: {js_path}")
        result = subprocess.run(
            ['node', js_path, to_address, str(amount)],
            capture_output=True,
            text=True
        )
        print(f"Node output: {result.stdout}")
        print(f"Node errors: {result.stderr}")
        return result.stdout
    except Exception as e:
        print(f"Error executing transfer: {e}")