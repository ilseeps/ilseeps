import json

inputv=dbutils.widgets.get("adf_input_value")

if inputv=="1":
  outputv="2"
else:
  outputv="1" 
  
dbutils.notebook.exit(json.dumps({
    "adf_output_value" : outputv
}))
