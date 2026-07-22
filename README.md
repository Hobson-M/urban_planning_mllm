# Mwewe-VLM: Multimodal Vision-Language Model for East African Micro-Development

## Overview
Current state-of-the-art Multimodal Large Language Models (MLLMs) in remote sensing excel at macro-level global land-use classification (e.g., GeoLLaVA-8K, RSGPT), but frequently fail when deployed in rapidly urbanizing, unstructured environments. Specifically, they lack the regional and engineering heuristics required to evaluate micro-development feasibility in East African urban centers (Kenya, Uganda, Tanzania, Rwanda, Burundi, South Sudan, DRC, and Somalia).

This repository houses the code, dataset formatting pipelines, and QLoRA fine-tuning workflows for **Mwewe-VLM**, a specialized vision-language model fine-tuned to analyze 1-acre land parcels and assess their spatial capacity to support dense, multi-unit concrete residential developments (e.g., configurations mixing 40 units of bedsitters, 1-bedroom, and 2-bedroom layouts).

## Core Architectural Pillars
1. **Transportation & Infrastructure:** Assessing road network widths, turning radii for construction vehicles, and localized traffic bottlenecks.
2. **Water Resources & Topography:** Evaluating permeable surface area reduction, runoff coefficients, and flood risk given local topological constraints.
3. **Human Settlements & Encroachment:** Analyzing boundary integrity, informal settlement proximity, and high-density plot layout efficiency.
4. **Decentralized Compute (DePIN):** Utilizing memory-efficient parameter-efficient fine-tuning (PEFT) pipelines designed to run across distributed GPU frameworks.

## Technical Stack
* **Base Architecture:** `Qwen2.5-VL-2B-Instruct` (leveraging dynamic-resolution M-RoPE).
* **Optimization Framework:** Unsloth & QLoRA (4-bit quantization) for low-overhead training.
* **Dataset Pipeline:** Conversational multi-turn instruction tuning pairs mapped to regional Earth Observation imagery (Digital Earth Africa sources).
* **Deployment:** Gradio web interface hosted on Hugging Face Spaces.

## Roadmap & Progress Tracking
- [ ] Phase 1: Repository initialization and problem statement architecture
- [ ] Phase 2: East African geospatial dataset ingestion and JSONL formatting
- [ ] Phase 3: QLoRA training loop execution via Unsloth
- [ ] Phase 4: Model evaluation on unseen regional parcels
- [ ] Phase 5: Gradio UI wrapper and web deployment
