from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
from ..plots import plots

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
  def deselect_all_links(self):
    """Reset all the roles on the navbar links."""
    for link in self.link_1, self.link_2, self.link_3:
      link.role = ''
      

  def link_3_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(plots())
    self.deselect_all_links()
    self.link_3.role = 'selected'
