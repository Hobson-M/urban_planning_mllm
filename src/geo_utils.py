import json
from src.prompts import SYSTEM_PROMPT, USER_TEMPLATE

def format_qwen_vl_record(image_path: str, location: str, layout_config: str, assistant_response: str) -> dict:
    """
    Formats a single training example into the Qwen2.5-VL JSON structure.
    """
    
    user_text = USER_TEMPLATE.format(location=location, layout_config=layout_config)
    
    record = {
        "messages": [
            {
                "role": "system",
                "content": [{"type": "text", "text": SYSTEM_PROMPT}]
            },
            {
                "role": "user",
                "content": [
                    {"type": "image", "image": image_path},
                    {"type": "text", "text": user_text}
                ]
            },
            {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": assistant_response}
                ]
            }
        ]
    }
    
    return record

def write_jsonl(records: list, output_path: str):
    """
    Writes a list of dictionary records to a JSONL file.
    """
    with open(output_path, 'w', encoding='utf-8') as f:
        for record in records:
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
            
    print(f"Successfully wrote {len(records)} records to {output_path}")