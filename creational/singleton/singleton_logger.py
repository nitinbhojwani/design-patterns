class Logger:
    only_instance = None

    def __new__(cls, *args, **kwargs):
        if Logger.only_instance is None:
            Logger.only_instance = object.__new__(cls, *args, **kwargs)
            Logger.only_instance._log_lines = []
        return Logger.only_instance

    def log(self, text):
        Logger.only_instance._log_lines.append(str(text))

    def get_logs(self):
        return Logger.only_instance._log_lines
