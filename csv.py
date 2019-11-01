import json

with open("report.json") as report:
    data = json.loads(report.read())
    rows = []
    for name, obj in data.items():
        rows.append(",".join([
            obj["title"].replace("\n","").replace(",",""),
            obj["author"].replace("\n","").replace(",",""),
            obj["content"].replace("\n","").replace(",",""),
            str(obj["polarity"]),
            str(obj["subjectivity"]),
            ]))
    report_text = "\n".join(rows)
    with open("report.csv", "w") as csv:
        csv.write(report_text)

