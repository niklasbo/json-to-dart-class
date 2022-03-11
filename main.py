import json

INPUT_CLASS_NAME = "MyObjectRepresentedAsJSON"
INPUT_JSON = """
{
    "id": 14,
    "accountId": 4,
    "syncTime": "2022-03-08T15:31:13.627",
    "title": "book of the books",
    "amount": 1495,
    "valueTime": "2022-02-18T00:00:00.000",
    "bookingTime": "2022-02-18T00:00:00.000"
}
"""

input = json.loads(INPUT_JSON)

# imports
output = "import 'package:equatable/equatable.dart';\n"

# constants
for key in input.keys():
    output += f"const _{key.upper()}='{key}';\n"

# class and constructor
output += f"class {INPUT_CLASS_NAME} extends Equatable {{\nconst {INPUT_CLASS_NAME}("
for key in input.keys():
    output += f"this.{key},"
output += ");\n"


def pythonTypeToDartType(type) -> str:
    if type is int:
        return "int"
    elif type is str:
        return "String"
    elif type is bool:
        return "bool"
    elif type is list:
        return "List<String>"


# fromJson constructor
output += f"{INPUT_CLASS_NAME}.fromJson(Map<String, dynamic> json) : "
for key in input.keys():
    output += f"{key} = json[_{key.upper()}] as {pythonTypeToDartType(type(input[key]))},\n"
output += ";\n"

# toJson method
output += f"Map<String, dynamic> toJson() => <String, dynamic>{{\n"
for key in input.keys():
    output += f"_{key.upper()}: {key},\n"
output += "};\n\n"

# class variables
for key in input.keys():
    output += f"final {pythonTypeToDartType(type(input[key]))}  {key};\n"

# toString method
output += f"\n@override\nString toString() {{\nreturn '{INPUT_CLASS_NAME}: ${{toJson()}}';\n}}\n"

# equatable props method
output += "@override List<Object?> get props => [\n"
for key in input.keys():
    output += f"{key},\n"
output += "];\n}\n"

print(output)
