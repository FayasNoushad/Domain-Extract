# Domain Extract

Domain extract from url or urls or string

## Installation

```
pip install Domain-Extract
```

## Usage

```py
import domain_extract
```

### Extract domain from url

```py
url = "https://github.com/FayasNoushad"

print(domain_extract.domain(url))
# => github.com
```

### Extract domains from urls list

```py
urls = [
    "https://twitter.com/FayasNoushad",
    "https://github.com/FayasNoushad"
]

print(domain_extract.domains(urls))
# => ["twitter.com", "github.com"]
```

### Extract domains from a string

```py
string = "Hello [Fayas](https://github.com/FayasNoushad)"

print(domain_extract.string_domains(string))
# => ["github.com"]
```
