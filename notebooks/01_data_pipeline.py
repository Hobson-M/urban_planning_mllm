import sys
import os

# 1. Dynamically find the project root based on this file's location
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

from src.geo_utils import format_qwen_vl_record, write_jsonl

# Sample training data simulating East African micro-development constraints
training_examples = [
    {
        "image_path": "file://data/raw/satellite_parcel_001.png",
        "location": "Ruiru, Kiambu County, Kenya",
        "layout_config": "Mixed multi-unit: 20 bedsitters, 10 1-bedroom, 10 2-bedroom using traditional concrete and quarry stone.",
        "assistant_response": "Feasibility Report:\n\n1. Transportation: The parcel borders a 9-meter unpaved access road. Turning radius is sufficient for 10-ton quarry stone delivery trucks.\n2. Water & Topography: Gentle 3-degree slope towards the south. Permeable surface will drop by 65%. On-site storm drainage required.\n3. Human Settlements: Bounded by high-density plots to the east. 2-meter boundary wall recommended for security and structural integrity.\n4. Layout: The mixed configuration of bedsitters, 1-bed, and 2-bed units is spatially viable. Recommend stacking the 2-bedroom units on the western axis for optimal load distribution."
    },
    {
        "image_path": "file://data/raw/satellite_parcel_002.png",
        "location": "Eldoret, Uasin Gishu County, Kenya",
        "layout_config": "High-density residential: 40 bedsitters.",
        "assistant_response": "Feasibility Report:\n\n1. Transportation: Proximity to arterial road allows excellent heavy machinery access. Minor traffic bottlenecks expected during concrete pouring phases.\n2. Water & Topography: Flat terrain with high seasonal water table. Deep trenching required for foundation stability.\n3. Human Settlements: Minimal encroachment risk; well-defined cadastral boundaries.\n4. Layout: Efficient spatial use. High bedsitter density will require optimized centralized plumbing shafts to reduce material costs."
    }
]

# Process the records through our formatting pipeline
processed_records = []
for item in training_examples:
    record = format_qwen_vl_record(
        image_path=item["image_path"],
        location=item["location"],
        layout_config=item["layout_config"],
        assistant_response=item["assistant_response"]
    )
    processed_records.append(record)

# 2. Save using an absolute path so it always writes to the right place
output_file = os.path.join(project_root, "data", "processed", "train.jsonl")
write_jsonl(processed_records, output_file)
