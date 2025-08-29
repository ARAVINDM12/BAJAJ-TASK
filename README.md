
# BAJAJ-TASK API
A REST API for the VIT Full Stack Question Paper task.

## Setup
1. Install dependencies: `pip install -r requirements.txt`
2. Run locally: `python app.py`
3. Deployed at: https://bajaj-task-am12.onrender.com/bfhl

## Endpoint
- POST `/bfhl`: Processes an array and returns categorized data, sum, and concatenated string.

## Example
```json
POST /bfhl
{"data": ["a","1","334","4","R","$"]}

## Response
{
  "is_success": true,
  "user_id": "aravind_m_12122003",
  "email": "aravind.m2022a@vitstudent.ac.in",
  "roll_number": "22BCT0024",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}

## ⚙️ Tech Stack

  Backend: Python + Flask

  Hosting: (Vercel / Railway / Render / any provider of choice)

  JSON-based REST API
