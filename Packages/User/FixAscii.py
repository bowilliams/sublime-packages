import sublime, sublime_plugin
from unidecode import unidecode

class FixAsciiCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        regions = view.sel()
        # if there are more than 1 region or region one and it's not empty
        if len(regions) > 1 or not regions[0].empty():
                for region in view.sel():
                    if not region.empty():
                        s = view.substr(region)
                        s = unidecode(s)
                        view.replace(edit, region, s)
        else:   #format all text
                alltextreg = sublime.Region(0, view.size())
                s = view.substr(alltextreg)
                s = unidecode(s)
                view.replace(edit, alltextreg, s)