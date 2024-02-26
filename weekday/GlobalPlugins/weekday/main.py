import addonHandler
import globalPluginHandler
import scriptHandler

import ui

from .timer import Timer

from .weekday import Weekday


addonHandler.initTranslation()


class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    scriptCategory = "Weekday"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.timer: Timer | None = None

    @scriptHandler.script(
        # Translators: description say day of of the week
        description=_("Says the day of the week"),
        gesture="kb:NVDA+W"
    )
    def script_weekday(self, gesture):
        if scriptHandler.getLastScriptRepeatCount() == 1:
            if self.timer:
                last_time = self.timer.get()
                self.timer = None
                text = "\n".join([_("The timer is disabled. Working hours:"), last_time])
            else:
                self.timer = Timer()
                text = _("Timer started")

        else:
            if self.timer:
                text = self.timer.get()
            else:
                text = Weekday.get_week_day()

        ui.message(text)
