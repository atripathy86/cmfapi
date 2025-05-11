import json 

from cmfapi import cmfClient
client = cmfClient("http://192.168.2.143:8080")

#Get Pipelines in DB
pipelines = client.get_pipelines()
print("Pipelines in DB:")
print(json.dumps(pipelines, indent=4))

if pipelines:  # Check if the list is not empty
    first_pipeline = pipelines[0]
    print(f"First Pipeline: {first_pipeline}")

#Get list of executions for a pipeline
executions_list = client.get_executions_list(first_pipeline)
print(f"Executions List for {first_pipeline}:")
print(json.dumps(executions_list, indent=4))

#Get Execution details for a pipeline
executions = client.get_executions(first_pipeline)
print(f"Executions for {first_pipeline}:")
print(json.dumps(executions, indent=4))

#Get Artifact Types in DB
artifact_types = client.get_artifact_types()
print("Artifact Types in DB:")
print(json.dumps(artifact_types, indent=4))

#Display Artifacts for a pipeline
if artifact_types: 
    first_artifact_type = artifact_types[0]
    print(f"First Artifact Type: {first_artifact_type}")

artifacts = client.get_artifacts(first_pipeline, first_artifact_type)
print(f"Artifacts for {first_pipeline} of type {first_artifact_type}:")
print(json.dumps(artifacts, indent=4))

#Fetch artifact lineage for a pipeline

artifact_lineage_tree = client.get_artifact_lineage_tangled_tree(first_pipeline)
print(f"Artifact Lineage Tree for {first_pipeline}:")
print(json.dumps(artifact_lineage_tree, indent=4))

#Fetch execution lineage for a pipeline

#Select a particular UUID
if "items" in executions and len(executions["items"]) > 0:
    first_execution = executions["items"][0]  # Get the first execution item
    execution_uuid = first_execution["Execution_uuid"]  # Access the Execution_uuid field
    selected_uuid = execution_uuid[:4]  # Slice the first 4 characters
    print(f"Selected Execution UUID (First 4 characters): {selected_uuid}")
else:
    print("No executions found.")
 
uuid = selected_uuid # Example UUID
pipeline_name = first_pipeline  # Use the first pipeline from the pipelines list

execution_lineage_tree = client.get_execution_lineage_tangled_tree(uuid, pipeline_name)
print(f"Execution Lineage Tree for UUID {uuid} and Pipeline {pipeline_name}:")
print(json.dumps(execution_lineage_tree, indent=4))

#Get Model Card
# model_card = client.get_model_card()
# print("Model Card:")
# print(json.dumps(model_card, indent=4))

#Get Python Environment 
# python_env = client.get_python_env()
# print("Python Environment Details:")
# print(python_env)


# payload = {
#     "key": "value",  # Replace with actual metadata fields
#     "pipeline_name": first_pipeline,
#     "execution_uuid": uuid
# }

# response = client.mlmd_push(payload)
# print("MLMD Push Response:")
# print(json.dumps(response, indent=4))

#Get MLMD Metadata for a pipeline
# pipeline_metadata = client.mlmd_pull(first_pipeline)
# print(f"Metadata for Pipeline {first_pipeline}:")
# print(json.dumps(pipeline_metadata, indent=4))


#Close the session
client.close_session()

