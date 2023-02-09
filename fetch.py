import pyasx.data.companies

results = pyasx.data.companies.get_listed_companies()
print(len(results)) # Somewhere around 2k companies