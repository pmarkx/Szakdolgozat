from aws_cdk import App, Stack

from constructs import Construct


class SzakdolgozatStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)


if __name__ == '__main__':
    app = App()
    SzakdolgozatStack(app)
    app.synth()
