from prefect.deployments import Deployment
from another_prefect_flow import another_flow
from workflows.prefect_flow import my_flow

def deploy():
    deployment = Deployment.build_from_flow(
            name=another_flow.name+"-deployment",
            flow=another_flow,
            work_pool_name="default-agent-pool",
        )
    deployment.apply()
    deployment = Deployment.build_from_flow(
            name=my_flow.name+"-deployment",
            flow=my_flow,
            work_pool_name="default-agent-pool",
        )
    deployment.apply()

if __name__ == "__main__":
    deploy()

pass