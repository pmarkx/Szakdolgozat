#!/usr/bin/env python3

from aws_cdk import core

from szakdolgozat.szakdolgozat_stack import SzakdolgozatStack


app = core.App()
SzakdolgozatStack(app, "szakdolgozat")

app.synth()
