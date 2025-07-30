import requests
import time
import random
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to send a request
def send_request(combo, base_url, headers):
    # Replace '*' in the URL with the actual query string
    url = base_url.replace('*', combo)
    retries = 2  # Set the maximum number of retries
    for _ in range(retries):
        try:
            # Send GET request with a 20-second timeout
            response = requests.get(url=url, headers=headers, timeout=20)
            if response.status_code == 200:
                # If the request is successful, sleep for a random time between 1 and 5 seconds
                time.sleep(random.randint(1, 5))
                return response.content
            else:
                # Print the error message if the status code is not 200
                print(response.text)
                print(f"Request for {combo} failed with status code {response.status_code}")
                # Wait for a random time before retrying
                time.sleep(random.randint(1, 5))
        except Exception as e:
            # Catch exceptions and print the error message
            print(f"Request for {combo} failed with exception: {e}")
            # Wait for a random time before retrying
            time.sleep(random.randint(1, 5))
    return None

# Function to write results to a file
def write_to_file(data_list, output_file):
    # Open the file in binary append mode
    with open(output_file, 'ab') as out_file:
        # Write each piece of data to the file with a newline
        for data in data_list:
            out_file.write(data)
            out_file.write(b'\n')

# Function to process requests in batches
def batch_process(file_path, base_url, headers, output_file):
    # Read the query combinations from the input file
    with open(file_path, 'r', encoding='utf-8') as file:
        combinations = file.read().splitlines()

    results = []  # List to store successful request results
    count = 0  # Counter to control when to write data to the file
    index = 0  # Total number of requests
    # Use ThreadPoolExecutor to create a thread pool with a maximum concurrency of 6
    with ThreadPoolExecutor(max_workers=50) as executor:
        # Submit all request tasks to the thread pool
        future_to_combo = {executor.submit(send_request, combo, base_url, headers): combo for combo in combinations}
        # Process the results as they complete
        for future in as_completed(future_to_combo):
            combo = future_to_combo[future]
            # Get the result of the request
            data = future.result()
            if data:
                # If the request is successful, add the data to the results list
                results.append(data)
                index += 1
                print(f"{index}: Response content for {combo} saved")
                count += 1

                # When 100 results are collected, write them to the file
                if count >= 100:
                    write_to_file(results, output_file)
                    results.clear()  # Clear the results list
                    count = 0

    # If there are any remaining results, write them to the file
    if results:
        write_to_file(results, output_file)

# Define the URL and headers for the requests
web = 'https://chatgpt.com/backend-api/gizmos/search?q=*'
headers = {
    'Accept':'',  # Accept header specifies the media type that is acceptable for the response
    'Accept-Encoding':'',  # Specifies the acceptable encoding types for the response
    'Accept-Language':'',  # Specifies the acceptable languages for the response
    'Authorization': '',  # Authorization token
    'Referer':'',  # Referrer header to indicate the origin of the request
    'Sec-Ch-Ua':'',  # Client information for security headers
    'Sec-Ch-Ua-Mobile':'',  # Mobile device information
    'Sec-Ch-Ua-Platform':'',  # Platform information
    'Sec-Fetch-Dest':'',  # Indicates the destination of the request
    'Sec-Fetch-Mode':'',  # Indicates the mode of the request
    'Sec-Fetch-Site':'',  # Specifies the origin of the request
    'User-Agent': ''  # User agent string indicating the client making the request
}

# Set the input file path and output file path
file_path = 'name.txt'
output_file = 'response.json'

# Execute the batch processing function
batch_process(file_path, web, headers, output_file)
