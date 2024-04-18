from flask import Flask, request, jsonify
import json
import os
import psutil
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


# Retrieve client's IP address
def get_client_ip():
    if request.environ.get('HTTP_X_FORWARDED_FOR'):
        return request.environ['HTTP_X_FORWARDED_FOR']
    else:
        return request.environ['REMOTE_ADDR']


# Endpoint for server load and disk space
@app.route('/server-status', methods=['GET'])
def server_status():
    client_ip = get_client_ip()
    logging.info(f"Accessed /server-status endpoint by {client_ip}")

    try:
        load_avg = os.getloadavg()
        disk_usage = psutil.disk_usage('/')
        return jsonify({
            'average_load': load_avg,
            'disk_space': {
                'total': disk_usage.total,
                'used': disk_usage.used,
                'free': disk_usage.free,
                'percent': disk_usage.percent
            }
        })
    except PermissionError:
        logging.error(f'PermissionError accessing system metrics by {client_ip}')
        return jsonify({'error': 'Permission denied accessing system metrics'}), 403
    except FileNotFoundError:
        logging.error(f'FileNotFoundError for disk usage statistics by {client_ip}')
        return jsonify({'error': 'Invalid path for disk usage statistics'}), 404
    except OSError as e:
        logging.error(f'OSError occurred: {str(e)} by {client_ip}')
        return jsonify({'error': f'OS error occurred: {str(e)}'}), 500
    except psutil.Error as e:
        logging.error(f'psutil error occurred: {str(e)} by {client_ip}')
        return jsonify({'error': f'psutil error occurred: {str(e)}'}), 500
    except Exception as e:
        # Catch any other exceptions
        logging.error(f'Unexpected error: {str(e)} by {client_ip}')
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


# Endpoint to get the 'return_value' from the tech_assess.json file
@app.route('/get-return-value', methods=['GET'])
def get_return_value():
    client_ip = get_client_ip()
    logging.info(f"Accessed /get-return-value endpoint by {client_ip}")

    try:
        # Attempt to open and read the JSON file
        with open('tech_assess.json', 'r') as file:
            data = json.load(file)

        # Extract the return_value
        return_value = data.get('tech', {}).get('return_value', 'Key not found')

        return jsonify({'return_value': return_value})

    except json.JSONDecodeError:
        logging.error(f'Invalid JSON in the file by {client_ip}')
        return jsonify({'error': 'Invalid JSON in the file'}), 500
    except FileNotFoundError:
        logging.error(f'File not found by {client_ip}')
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        # Catch any other exceptions
        logging.error(f'Unexpected error: {str(e)} by {client_ip}')
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


# Endpoint to set the 'return_value' in the tech_assess.json file
@app.route('/set-return-value', methods=['POST'])
def set_return_value():
    client_ip = get_client_ip()
    logging.info(f"Accessed /set_return_value endpoint by {client_ip}")

    # Limit for the size of the incoming data (in bytes)
    MAX_CONTENT_LENGTH = 1024  # 1KB

    if request.content_length > MAX_CONTENT_LENGTH:
        return jsonify({'error': 'Payload too large'}), 413

    try:
        # Ensure the request contains JSON
        request_data = request.get_json()
        if request_data is None:
            return jsonify({'error': 'Invalid JSON or Content-Type'}), 400

        # Check if 'return_value' is present in the JSON
        if 'return_value' not in request_data:
            return jsonify({'error': 'Missing return_value in JSON payload'}), 400

        # TODO: Check for the datatype of 'return_value'

        # Read the existing data
        with open('tech_assess.json', 'r+') as file:
            data = json.load(file)

            # Check if 'tech' key exists and is a dictionary
            if not isinstance(data.get('tech'), dict):
                data['tech'] = {}

            # Update the return_value
            data['tech']['return_value'] = request_data['return_value']

            # Go back to the start of the file and overwrite
            file.seek(0)
            json.dump(data, file, indent=4)
            # Truncate the file to the current file cursor position to remove any excess data after rewriting
            file.truncate()

        return jsonify({'message': 'return_value updated successfully'})

    except json.JSONDecodeError:
        logging.error(f'Invalid JSON in the file by {client_ip}')
        return jsonify({'error': 'Invalid JSON in the file'}), 500
    except FileNotFoundError:
        logging.error(f'File not found by {client_ip}')
        return jsonify({'error': 'File not found'}), 404
    except Exception as e:
        # Catch any other exceptions
        logging.error(f'Unexpected error: {str(e)} by {client_ip}')
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


if __name__ == '__main__':
    app.run(debug=False)
