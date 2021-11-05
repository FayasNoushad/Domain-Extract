import string_extract


def domain(url):
    if url.startswith("http://") or url.startswith("https://"):
        domain = url.split("://", 1)[-1].split("/", 1)[0]
    else:
        domain = ""
    return domain


def domains(urls):
    domains = []
    for url in urls:
        domains.append(domain(url))
    return domains


def string_domains(string):
    urls = string_extract.urls(string)
    return domains(urls)
