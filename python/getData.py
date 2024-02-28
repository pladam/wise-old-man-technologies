#!/usr/bin/env python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import os

def get_filing_data(filing_url):

    # Define headers with user-agent, accept-encoding, and host
    headers = {
        'User-Agent': 'Sample Company Name AdminContact@samplecompany.com',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }

    try:
        # Send a GET request to the filing URL with headers
        response = requests.get(filing_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse HTML response
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Find all tables in the HTML
            tables = soup.find_all('table')
            
            # Initialize a flag to check if the table containing both "revenue" and "research and development" has been found
            found_table = False

            # Iterate over each table and look for income table
            for i, table in enumerate(tables):
                # Check if the table contains both "revenue" and "research and development"
                if "net income" in table.get_text().lower() and "basic" in table.get_text().lower() and "diluted" in table.get_text().lower():
                    # Read HTML table into DataFrame
                    df = pd.read_html(str(table))[0]  # Convert the BeautifulSoup table to HTML string and read it into DataFrame
                    
                    # Print table number
                    #print(f"Table {i + 1}:")
                    
                    # Print the DataFrame
                    print(df)
                    print()  # Add a newline between tables
                    
                    # Set the flag to True to indicate that the table has been found
                    found_table = True
                    
                    # Break out of the loop since we found the desired table
                    break
            
            # Check if the desired table was not found
            #if not found_table:
            #    print("No table containing both 'net income' and 'basic' and 'diluted' found.")

            # Iterate over each table and look for balance sheet table
            for i, table in enumerate(tables):
                # Check if the table contains both "revenue" and "research and development"
                if "total assets" in table.get_text().lower() and "total liabilities" in table.get_text().lower():
                    # Read HTML table into DataFrame
                    df = pd.read_html(str(table))[0]  # Convert the BeautifulSoup table to HTML string and read it into DataFrame
                    
                    # Print table number
                    #print(f"Table {i + 1}:")
                    
                    # Print the DataFrame
                    print(df)
                    print()  # Add a newline between tables
                    
                    # Set the flag to True to indicate that the table has been found
                    found_table = True
                    
                    # Break out of the loop since we found the desired table
                    break
            
            # Check if the desired table was not found
            #if not found_table:
            #    print("No table containing both 'net income' and 'basic' and 'diluted' found.")

            # Iterate over each table and look for cashflow table
            for i, table in enumerate(tables):
                # Check if the table contains both "revenue" and "research and development"
                if "operating" in table.get_text().lower() and "investing" in table.get_text().lower() and "financing" in table.get_text().lower():
                    # Read HTML table into DataFrame
                    df = pd.read_html(str(table))[0]  # Convert the BeautifulSoup table to HTML string and read it into DataFrame
                    
                    # Print table number
                    #print(f"Table {i + 1}:")
                    
                    # Print the DataFrame
                    print(df)
                    print()  # Add a newline between tables
                    
                    # Set the flag to True to indicate that the table has been found
                    found_table = True
                    
                    # Break out of the loop since we found the desired table
                    break
            
            # Check if the desired table was not found
            #if not found_table:
            #    print("No table containing both 'net income' and 'basic' and 'diluted' found.")

        else:
            print(f"Failed to fetch filing document. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_10k_filings_urls(stock_ticker):

    # Define headers with user-agent, accept-encoding, and host
    headers = {
        'User-Agent': 'Sample Company Name AdminContact@samplecompany.com',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }

    base_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={stock_ticker}&type=10-K&dateb=&owner=exclude&count=100"
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    filing_urls = []

    for link in soup.find_all('a', href=True):
        pattern = '<a href="\/Archives\/edgar\/data\/\d+\/\d+\/\d+-\d+-\d+-index.htm" id="documentsbutton"> Documents<\/a>'
        if bool(re.search(pattern, str(link))):
            extract_pattern = r'href="([^"]+)"'
            match = re.search(extract_pattern, str(link))
            if match:
                href_url = match.group(1)
                L1_url = "https://www.sec.gov" + href_url
                #print(L1_url)
                get_form_htm_url(L1_url)
    return(filing_urls)
    
def get_10q_filings_urls(stock_ticker):

    # Define headers with user-agent, accept-encoding, and host
    headers = {
        'User-Agent': 'Sample Company Name AdminContact@samplecompany.com',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }

    base_url = f"https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK={stock_ticker}&type=10-Q&dateb=&owner=exclude&count=100"
    response = requests.get(base_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    filing_urls = []

    for link in soup.find_all('a', href=True):
        pattern = '<a href="\/Archives\/edgar\/data\/\d+\/\d+\/\d+-\d+-\d+-index.htm" id="documentsbutton"> Documents<\/a>'
        if bool(re.search(pattern, str(link))):
            extract_pattern = r'href="([^"]+)"'
            match = re.search(extract_pattern, str(link))
            if match:
                href_url = match.group(1)
                L1_url = "https://www.sec.gov" + href_url
                #print(L1_url)
                get_form_htm_url(L1_url)
    return(filing_urls)

def get_form_htm_url(form_url):

    # Define headers with user-agent, accept-encoding, and host
    headers = {
        'User-Agent': 'Sample Company Name AdminContact@samplecompany.com',
        'Accept-Encoding': 'gzip, deflate',
        'Host': 'www.sec.gov'
    }
    
    response = requests.get(form_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
        
    htm_url = None
    for link in soup.find_all('a', href=True):
        pattern = r'<a\s+href="[^"]+\.htm">([^<]+)</a>'

        if bool(re.search(pattern, str(link))):
        #if bool(re.search(pattern, str(link))):
            # Define the regex pattern
            pattern_href = r'<a\s+href="([^"]+)">'
            
            # Find the URL using regex
            match = re.search(pattern_href, str(link))

            # Extract the URL if match is found
            if match:
                url = str(match.group(1))
                filing_url = "https://www.sec.gov" + url
                filing_url = filing_url.replace("/ix?doc=","")
                #print(filing_url)
                get_filing_data(filing_url)
            else:
                print("No URL found for input:", link)


stock_ticker = "SPGI"  # Example stock ticker
filings_urls = get_10k_filings_urls(stock_ticker)
#filings_urls = get_10q_filings_urls(stock_ticker)
