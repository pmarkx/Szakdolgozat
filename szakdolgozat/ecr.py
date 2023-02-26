from aws_cdk import aws_ecr as ecr

from constructs import Construct


class Ecr(ecr.Repository):
    def __int__(self, scope: Construct, construct_id: str, repository_name: str, **kwargs):
        super().__init__(scope, construct_id, repository_name=repository_name, **kwargs)
