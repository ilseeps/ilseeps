import json

#fetch the value from data factory trigger
inputv=dbutils.widgets.get("adf_input_value")

#execute some logic
if inputv=="1":
  outputv="2"
else:
  outputv="1" 

#return a variable on notebook exit
dbutils.notebook.exit(json.dumps({
    "adf_output_value" : outputv
}))
