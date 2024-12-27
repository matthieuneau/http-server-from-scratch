import socket

PORT = 8080
ADDRESS = "0:0:0:0"

web_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

web_socket.bind(("localhost", PORT))


def parse_request(request: str) -> dict:
    lines = request.split("\n")
    result = {}
    result["http_version"] = lines[0].split(" ")[2].split("/")[1]
    result["method"] = lines[0].split(" ")[0]

    if "?" in lines[0].split(" ")[1]:
        result["path"] = lines[0].split(" ")[1].split("?")[0]
        query = lines[0].split(" ")[1].split("?")[1]
        query_params = query.split("&")
        result["query_params"] = {
            k: v for k, v in [param.split("=") for param in query_params]
        }
    else:
        result["path"] = lines[0].split(" ")[1]
        result["query_params"] = None

    result["headers"] = {}
    result["headers"]["host"] = lines[1].lower().split(":")[1]
    result["headers"]["user-agent"] = lines[2].lower().split(":")[1]
    result["headers"]["accept"] = lines[3].lower().split(":")[1]

    result["body"] = lines[-1]

    return result


if __name__ == "__main__":
    request = """POST /form HTTP/1.1
Host: localhost:8080
User-Agent: curl/7.68.0
Content-Type: application/x-www-form-urlencoded
Content-Length: 13

name=JohnDoe"""
    print(parse_request(request))
