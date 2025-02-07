import time
import logging
from google.cloud import dataform_v1beta1

logger = logging.getLogger(__name__)
logger.setLevel(10)

def get_workflow_invocation(invocation):
    # Create a client
    client = dataform_v1beta1.DataformClient()

    # Initialize request argument(s)
    request = dataform_v1beta1.GetWorkflowInvocationRequest(
        name=invocation.name
    )

    # Make the request
    max_attempts = 5
    polling_interval = 15

    for attempts in range(max_attempts):
        response = client.get_workflow_invocation(request=request)

        #logger.debug(f"{attempts+1}/{max_attempts}: Workflow invocation {response.state.name}")

        if response.state == dataform_v1beta1.WorkflowInvocation.State.SUCCEEDED:
            #logger.info("Workflow invocation SUCCEEDED")
            break
        elif response.state == dataform_v1beta1.WorkflowInvocation.State.FAILED:
            raise Exception("Workflow invocation FAILED")
        else:
            time.sleep(polling_interval)
    else:
        raise Exception(f"Workflow invocation FAILED after {max_attempts} attempts")

    response = client.get_workflow_invocation(request=request)

    return response
