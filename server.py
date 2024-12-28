import socket
from routes import routes


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


def handle_request(request: str) -> str:
    parsed_request = parse_request(request)
    path = parsed_request["path"]

    return str(routes.get(path, routes["/404"]))


if __name__ == "__main__":
    PORT = 8080
    ADDRESS = "localhost"

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ADDRESS, PORT))
    server.listen(1)
    print(f"Server listening on {ADDRESS}:{PORT}")
    while True:
        client_socket, client_address = server.accept()
        request = client_socket.recv(1024).decode()
        response = handle_request(request)
        print("response:", response)
        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()
