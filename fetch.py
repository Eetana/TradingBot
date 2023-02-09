import pyasx.data.companies as pdc
import pyasx.data.securities as pds

results = pdc.get_listed_companies()
print(len(results)) # Somewhere around 2k companies
print(results[1])     # What is available is limitd, and doesn't include stock

# Found the way to get price of the specific stock and the relevant metadata, including curr price (last_price)
p = pds.get_security_info(results[0]["ticker"]) 

print(p)
print(p["last_price"])  # In $AUD