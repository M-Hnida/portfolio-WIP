import json
import os

log_path = r"C:\Users\got\.gemini\antigravity\brain\d0b0b87c-9fe1-4b8f-b992-038b9baf5d02\.system_generated\logs\transcript.jsonl"
if not os.path.exists(log_path):
    print("Log path not found")
    exit()

with open(log_path, 'r', encoding='utf-8') as f:
    for line in f:
        try:
            data = json.loads(line)
            step_idx = data.get('step_index')
            if step_idx in [250, 252]:
                print(f"--- STEP {step_idx} RAW START ---")
                content = data.get('content', '')
                lines = content.split('\n')
                for l in lines[:30]:
                    print(l)
                print(f"--- STEP {step_idx} RAW END (Total lines: {len(lines)}) ---")
        except Exception as e:
            pass
