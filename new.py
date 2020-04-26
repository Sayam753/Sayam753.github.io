import json
import os
from shutil import copy, rmtree


with open('Trading App.postman_collection.json', 'r') as f:
    data = json.load(f)

with open(f"_data/navigation.yml", "a") as f:
    f.write("\napis:\n")
    f.write("  - title: APIs for Trading App\n")
    f.write("    children:\n")

codes = ["OK", "Unauthorized", "Forbidden",
         "Not Found", "Unprocessable Entity"]

dir_name = "_apis"
if os.path.isdir("_apis"):
    rmtree("_apis")
os.mkdir(dir_name)

for file_index, item in enumerate(data["item"], 1):
    low = item["name"].lower()
    file_name = str(file_index).zfill(2) + "-" + low + ".md"
    start_url = "/apis/" + low

    with open(f"_data/navigation.yml", "a") as f:
        f.write(f'      - title: {item["name"]}\n')
        f.write(f"        url: {start_url}\n")

    with open(f"{dir_name}/{file_name}", "w") as f:
        f.write("---\n")
        f.write(f'title: APIs for {item["name"]}\n')
        f.write(f'permalink: {start_url}\n')
        f.write("toc: true\n")
        f.write("---\n\n")

        for api in item["item"]:

            # From request
            request = api["request"]
            request_type = request["method"]
            url = request["url"]["raw"]
            url = "/" + "/".join(url.split("/")[3:])
            content = request["description"].split("\n")
            title = content[1].split(".")[1].strip()

            # Writing request
            f.write(f"\n## {title}\n\n")
            f.write(f"**{request_type} Request** - `{url}`\n")
            f.write("{: .notice--info}\n\n")
            f.write("```bash\ncurl\n```\n\n")

            # From response
            f.write("### Sample Responses\n\n")
            response = api["response"]
            example_responses = [n["name"].split(
                "-")[1].strip() for n in response]
            count = 1
            for code in codes:
                index = None
                try:
                    index = example_responses.index(code)
                except ValueError:
                    pass
                else:
                    example = response[index]
                    body = response[index]["body"].replace("\n", "\n    ")
                    body = body.replace("\t", "  ")
                    f.write(f"{count}. Response - {code}\n\n")
                    f.write(f"    ```json\n    {body}\n    ```\n")
                    count += 1
