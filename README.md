```
Made with Python3
(C) @FayasNoushad
Copyright permission under MIT License
License -> https://github.com/FayasNoushad/Domain-Extract/blob/main/LICENSE
```

---

## Installation

```
pip install Domain-Extract
```

---

## Usage

```py
import domain_extract
```

### Extract domain from url

```py
url = "https://fayas.me/"

print(domain_extract.domain(url))
```
Response :- `fayas.me`

### Extract domains from urls list

```py
urls = ["https://fayas.me", "https://github.com/FayasNoushad"]

print(domain_extract.domains(urls))
```
Response :- `["fayas.me", "github.com"]`

### Extract domains from a string

```py
string = "Hello [Fayas](https://fayas.me/)"

print(domain_extract.string_domains(string))
```
Response :- `["fayas.me"]`

---

## Credits

- [Fayas Noushad](https://github.com/FayasNoushad)

---
