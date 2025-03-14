from flask import Flask

class EasyOIDCFlow(Flask):
  def __init__(self, context):
    super().__init__(context.import_name)