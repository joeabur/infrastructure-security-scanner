from scanner.reporters import csv_reporter, html_reporter, json_reporter, terminal_reporter

REPORTERS = {"json": json_reporter.render, "csv": csv_reporter.render, "html": html_reporter.render, "terminal": terminal_reporter.render}
