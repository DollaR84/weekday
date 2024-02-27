import addonHandler
import globalPluginHandler
import scriptHandler

import ui

from .actions import SolverAction


addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Weekday"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.actions: SolverAction = SolverAction()

    @scriptHandler.script(
        # Translators: description say day of of the week
        description=_("Says the day of the week"),
        gesture="kb:NVDA+W"
    )
    def script_weekday(self, gesture):
        text = self.actions.get(scriptHandler.getLastScriptRepeatCount() + 1)
        ui.message(text)
