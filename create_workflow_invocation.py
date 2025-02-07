from google.cloud import dataform_v1beta1

tag = "{}"

project = "{}"
location = "{}"
repository = "{}"

parent = f"projects/{project}/locations/{location}/repositories/{repository}"

def create_workflow_invocation(tag, compilation_result):
    # Create a client
    client = dataform_v1beta1.DataformClient()

    # Initialize request argument(s)
    invocation_config = dataform_v1beta1.InvocationConfig(
        # included_targets=[]
        included_tags=tag,
        transitive_dependencies_included=False,
        transitive_dependents_included=False,
        fully_refresh_incremental_tables_enabled=False
        # service_account=""
    )

    workflow_invocation = dataform_v1beta1.WorkflowInvocation(
        compilation_result=compilation_result.name,
        invocation_config=invocation_config
    )

    request = dataform_v1beta1.CreateWorkflowInvocationRequest(
        parent=parent,
        workflow_invocation=workflow_invocation,
    )

    # Make the request
    response = client.create_workflow_invocation(request=request)

    return response
