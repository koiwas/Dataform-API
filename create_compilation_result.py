from google.cloud import dataform_v1beta1

project = "{}"
location = "{}"
repository = "{}"

git_commitish = "main"
parent = f"projects/{project}/locations/{location}/repositories/{repository}"

def create_compilation_result(git_commitish, parent):
    # Create a client
    client = dataform_v1beta1.DataformClient()

    # Initialize request argument(s)
    compilation_result = dataform_v1beta1.CompilationResult()
    compilation_result.git_commitish = git_commitish

    request = dataform_v1beta1.CreateCompilationResultRequest(
        parent=parent,
        compilation_result=compilation_result
    )

    # Make the request
    response = client.create_compilation_result(request=request)

    return response
