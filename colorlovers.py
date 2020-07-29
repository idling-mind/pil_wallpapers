from xml.etree import ElementTree as et
import requests

def get_top_pallet(rank):
    """Get a top ranked pallete from colorlovers.com

    Args:
        rank (int): The rank of the pallet in the website.
            Starting with 0.

    Returns:
        list: A list of str where each str is a hex representation
            of the color
    """
    # Using requests module to get the top pallets xml
    r = requests.get("https://www.colourlovers.com/api/palettes/top")

    # Parsing the xml to return the pallet based on input rank
    pallets = et.fromstring(r.text)
    
    # Getting the hex tags from a given pallet
    hex_elems = pallets[rank].iter('hex')
    
    return [c.text for c in hex_elems]
