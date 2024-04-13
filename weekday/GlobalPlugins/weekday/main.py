import addonHandler
import globalPluginHandler
import scriptHandler

import ui

from .actions import Solver


addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Weekday"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.solver: Solver = Solver()

    @scriptHandler.script(
        description=_("main action"),
        gesture="kb:NVDA+W"
    )
    def script_weekday(self, gesture):
        text = self.solver.get(scriptHandler.getLastScriptRepeatCount() + 1)
        ui.message(text)

    @scriptHandler.script(
        description=_("change mode"),
        gesture="kb:NVDA+ALT+W"
    )
    def script_change_mode(self, gesture):
        text = self.solver.change_mode()
        ui.message(text)

    @scriptHandler.script(
        description=_("additional function"),
        gesture="kb:NVDA+SHIFT+W"
    )
    def script_additional(self, gesture):
        text = self.solver.additional()
        if text:
            ui.message(text)

    @scriptHandler.script(
        description=_("additional 2 action"),
        gesture="kb:NVDA+SHIFT+ALT+W"
    )
    def script_additional2(self, gesture):
        self.solver.additional2(scriptHandler.getLastScriptRepeatCount() + 1)
