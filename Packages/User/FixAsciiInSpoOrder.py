import sublime, sublime_plugin
from unidecode import unidecode

class FixAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit, args):
        self.window.show_input_panel('hi!','',self.on_done,None,None)
        for region in self.view.sel():
            if not region.empty():
                text = view.substr(region)
                normalized_text = unidecode(text)
                view.replace(edit,region,normalized_text)
    def on_done(self,text):
        pass