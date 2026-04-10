import sys
from PyQt6.QtWidgets import QApplication
from core.assistant import processar
from ui.window import AssistantUI

app = QApplication(sys.argv)

window = AssistantUI(processar)
window.show()

sys.exit(app.exec())