from urllib.parse import urlparse

def domain_name(url):
    # Add a scheme if missing to ensure urlparse works correctly
    if not url.startswith(('http://', 'https://')):
        url = 'http://' + url
    
    # Parse the URL
    parsed_url = urlparse(url)
    
    # Extract the netloc (network location part) which includes the domain
    domain = parsed_url.netloc
    
    # Remove 'www.' if it exists
    if domain.startswith('www.'):
        domain = domain[4:]
    
    # Split the domain by '.' and take the first part
    domain_name = domain.split('.')[0]
    
    return domain_name

# Test cases
print(domain_name("http://github.com/carbonfive/raygun"))  # Output: github
print(domain_name("http://www.zombie-bites.com"))          # Output: zombie-bites
print(domain_name("https://www.cnet.com"))                 # Output: cnet
print(domain_name("icann.org"))                            # Output: icann
print(domain_name("www.xakep.ru"))                         # Output: xakep