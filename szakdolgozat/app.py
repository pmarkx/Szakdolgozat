import json
import cfn_flip

from aws_cdk import App, Stack

from constructs import Construct

from ecr import Ecr


class SzakdolgozatStack(Stack):
    def __init__(self, scope: Construct, construct_id: str = "Szakdolgozat", **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        self.main_ecr = Ecr(self, construct_id)


if __name__ == '__main__':
    app = App()
    SzakdolgozatStack(app)
    for stack in app.synth().stacks:
        stack_json = json.dumps(stack.template, indent=4, sort_keys=True)
        with open("stack.json", "w") as outfile:
            outfile.write(stack_json)
        with open("stack.yaml", "w") as outfile:
            outfile.write(cfn_flip.to_yaml(stack_json))
    print("done")
