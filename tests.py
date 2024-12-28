from server import parse_request

if __name__ == "__main__":
    request = """POST /form HTTP/1.1
    Host: localhost:8080
    User-Agent: curl/7.68.0
    Content-Type: application/x-www-form-urlencoded
    Content-Length: 13

    name=JohnDoe"""
    print(parse_request(request))
