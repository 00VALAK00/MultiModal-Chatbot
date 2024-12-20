# MultiModal LLM powered chatbot

---

This project leverages a MutiModal LLM and prompt engineering to build a chatbot that can perfrom 3 main tasks:
1. Question Answering
2. Optical Character Recognition
3. Information retrieval from images.

 ---

## Table of Contents
1. [Project Overview](#project-overview)
2. [MLLM](#MLLM)
3. [Model Training](#model-training)
4. [Examples of Completions](#Examples-of-Completions )

---

## Project Overview

the application integrates state-of-the-art multimodal model to bridge the gap between visual and
textual data processing. By utilizing OCR techniques, the system extracts text from images, while the
information retrieval module identifies and extracts structured information, such as tables and figures,
from visual content. Additionally, the chatbot functionality uses an LLM to provide natural language
responses to user queries, offering conversational support. The integration of these functionalities into a
single system allows seamless processing of both textual and image-based inputs, enhancing accessibility,
and providing valuable insights from images. This application demonstrates the potential
of combining vision and language models to solve real-world problems, particularly in fields such as
accessibility, document analysis, and general AI assistance. The results seems impressive in each task,
with an efficient and user-friendly interface, which demonstrates the feasibility of multimodal AI systems
in practical applications.

---

## MLLM
 The model is MiniCPMV-2.6, comprising SigLip-400M and Qwen2-7B with a total of 8B parameters. It exhibits a significant performance
 improvement and outperforms GPT-4o mini, GPT-4V, Gemini 1.5 Pro, and Claude 3.5 Sonnet for single image understanding.
 **Perks**:
 1. ** Performace achieving 65.2 on openCompass benchmark**
 2. **Lightweight**
 3. **Efficiency (Memory ususage)**
 4. **Strong OCR capabilities**

## Examples of Completions 

**OCR**: Performs OCR and handles complex layouts such as titles, figure names and tables

![images](https://github.com/00VALAK00/MultiModal-Chatbot/blob/master/images/OCR%20task/Screenshot%202024-12-17%20233750.png)

**Information retrieval**: Given certain features the MLLM extracts relevant information from the images

![images](https://github.com/00VALAK00/MultiModal-Chatbot/blob/master/images/Information%20Retrieval/ir%204.png)


