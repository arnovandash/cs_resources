
# Technical Assessment API Challenge

## Overview
This guide will walk you through setting up a Flask environment and running a Flask application that includes endpoints for retrieving server load and disk space information, as well as interacting with a JSON file.

## Prerequisites
- Python (3.6 or later) installed on your system.

## Installation
1. **Extract the Application Files**:
   Download the necessary files and extract them to your chosen directory.

2. **Navigate to the Project Directory**:
   Open a terminal and navigate to the directory.

3. **Create a Virtual Environment** (Recommended):
   ```bash
   python3 -m venv venv
   ```

4. **Activate the Virtual Environment**:
   - On Windows: `venv\Scripts\activate`
   - On Unix or MacOS: `source venv/bin/activate`

5. **Install Required Packages**:
   ```bash
   pip install -r requirements.txt
   ```

6. **Run the Flask Application**:
   ```bash
   python app.py
   ```

## Testing the Endpoints with cURL
- **Server Load and Disk Space**:
  ```bash
  curl http://localhost:5000/server-status
  ```
- **Get 'return_value' from JSON File**:
  ```bash
  curl http://localhost:5000/get-return-value
  ```
- **Set 'return_value' in JSON File**:
  ```bash
  curl -X POST http://localhost:5000/set-return-value -H "Content-Type: application/json" -d '{"return_value": "New Value"}'
  ```

## API Documentation
Detailed API endpoints are outlined below, including their functionalities, request and response formats, and example curl commands for testing.

### Endpoints
1. **Server Status**
   - **URL:** `/server-status`
   - **Method:** GET
   - **URL Params:** None
   - **Data Params:** None
   - **Success Response:**
     - **Code:** 200
     - **Content:** `{ "average_load": [2.76513671875, 3.1162109375, 3.0888671875], "disk_space": { "free": 94185050112, "percent": 9.5, "total": 371000844288, "used": 9896517632 } }`
   - **Error Response:**
     - **Code:** 403 / 404 / 500
     - **Content:** `{ "error": "Error message" }`

2. **Get Return Value**
   - **URL:** `/get-return-value`
   - **Method:** GET
   - **URL Params:** None
   - **Data Params:** None
   - **Success Response:**
     - **Code:** 200
     - **Content:** `{ "return_value": 1337 }`
   - **Error Response:**
     - **Code:** 404 / 500
     - **Content:** `{ "error": "Error message" }`

3. **Set Return Value**
   - **URL:** `/set-return-value`
   - **Method:** POST
   - **URL Params:** None
   - **Data Params:** Required: `return_value` (e.g., integer or string based on your implementation)
   - **Success Response:**
     - **Code:** 200
     - **Content:** `{ "message": "return_value updated successfully" }`
   - **Error Response:**
     - **Code:** 400 / 413 / 404 / 500
     - **Content:** `{ "error": "Error message" }`

