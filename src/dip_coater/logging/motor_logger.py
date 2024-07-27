from logging import Handler

from textual.widgets import RichLog

from TMC_2209._TMC_2209_logger import Loglevel


class MotorLoggerHandler(Handler):
    def __init__(self, logger_widget: RichLog) -> None:
        super().__init__()
        self.logger_widget = logger_widget

    def emit(self, record) -> None:
        self.logger_widget.write(self.colorize(record))

    def colorize(self, record):
        message = self.format(record)
        if record.levelno == Loglevel.ERROR.value:
            return f"[red]{message}[/]"
        elif record.levelno == Loglevel.WARNING.value:
            return f"[dark_orange]{message}[/]"
        elif record.levelno == Loglevel.MOVEMENT.value:
            return f"[cyan]{message}[/]"
        return message