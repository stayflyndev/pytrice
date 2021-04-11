from ipstack import GeoLookup
geo_lookup = GeoLookup("acecac3893c90871c3")
location = geo_lookup.get_location("github.com")
print(location)



# Lookup a location for an IP Address
# and catch any exceptions that might
# be thrown
try:
    # Retrieve the location information for 
    # github.com by using it's hostname.
    # 
    # This function will work with hostnames
    # or IP addresses.
    location = geo_lookup.get_location("github.com")

    # If we are unable to retrieve the location information
    # for an IP address, null will be returned.
    if location is None:
        print("Failed to find location.")
    else:
        # Print the Location dictionary.
        print(location)
except Exception as e:
    print(e)