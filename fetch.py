import pyasx.data.companies as pdc
import pyasx.data.securities as pds
import pandas as pd


def setup_DataFrame():
    
    # Get the information on all companies
    companies = pdc.get_listed_companies()
    
    # Create a list of key info
    key_info = ["Stock","Open", "Current", "Bid", "Current Offer", "% Change", "Previous % change", "Our Amount", "Our Value"]
    
    df = pd.DataFrame(columns= key_info)
    
    # Go through each one and obtain critical information and store in a 2d array
    key_data = []
    for company in companies:
        
        # Store data in this array
        curr_data = []
        
        # Try to access stock information if possible
        # try:
        share_info = pds.get_security_info(company["ticker"])
        # print(share_info)
        # return 0,1
        # Add needed items onto the array 
        curr_data.append(company["ticker"])                       # Stock
        curr_data.append(share_info["open_price"])              # Open
        curr_data.append(share_info["last_price"])              # Current
        curr_data.append(share_info["bid_price"])               # Bid
        curr_data.append(share_info["offer_price"])             # Current Offer
        curr_data.append(share_info["day_change_percent"])      # % Change
        curr_data.append(share_info["prev_day_change_percent"])      # % Change
        curr_data.append(0)
        curr_data.append(0)
        
        key_data.append(curr_data)
            
        # Else just skip to the next
        # except Exception: continue    
    
    # Make the dataframe
    for data in key_data:
        df.loc[len(df)] = data
    
    return df, key_data

Frame = setup_DataFrame()

print(Frame)

# results = 
# print(len(results)) # Somewhere around 2k companies
# print(results[1])     # What is available is limitd, and doesn't include stock

# # Found the way to get price of the specific stock and the relevant metadata, including curr price (last_price)
# p = pds.get_security_info(results[0]["ticker"]) 

# print(p)
# print(p["last_price"])  # In $AUD



# for entry in results:
#     try:
#         share_info = pds.get_security_info(entry["ticker"])
#         entry["offer_price"] = share_info["offer_price"]
#     except Exception: continue
    
# print(results[0])