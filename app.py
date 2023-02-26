import json

from aws_cdk import App
from szakdolgozat.szakdolgozat_stack import SzakdolgozatStack

if __name__ == '__main__':
    app = App()
    SzakdolgozatStack(app)
    with open("stack.json", "w") as outfile:
        for stack in app.synth().stacks:
            outfile.write(json.dumps(stack.template, indent=4, sort_keys=True))
    print("done")
