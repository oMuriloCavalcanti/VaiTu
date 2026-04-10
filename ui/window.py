from PyQt6.QtWidgets import QWidget, QLineEdit, QLabel, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

class AssistantUI(QWidget):
    def __init__(self, processar_callback):
        super().__init__()

        self.processar = processar_callback

        self.setFixedSize(250, 300)

        # 🔥 ESSENCIAL para transparência
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        # 🔥 Sem borda + sempre no topo
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |
            Qt.WindowType.WindowStaysOnTopHint
        )

        # 🖼️ Personagem (PNG com fundo transparente)
        self.background = QLabel(self)
        self.background.setGeometry(0, 0, 250, 300)

        pixmap = QPixmap("ui/assets/background.png")
        self.background.setPixmap(pixmap)
        self.background.setScaledContents(True)

        # 🧠 Output (balão tipo assistente)
        self.output = QLabel("...")
        self.output.setGeometry(40, 40, 220, 80)
        self.output.setWordWrap(True)
        self.output.setStyleSheet("""
            background-color: rgba(0,0,0,0.6);
            color: white;
            padding: 8px;
            border-radius: 10px;
        """)

        # ⌨️ Input flutuante
        self.input = QLineEdit(self)
        self.input.setGeometry(40, 340, 220, 30)
        self.input.setPlaceholderText("Digite um comando...")
        self.input.returnPressed.connect(self.enviar)

        self.input.setStyleSheet("""
            background-color: rgba(255,255,255,0.9);
            padding: 6px;
            border-radius: 10px;
            border: none;
        """)

        self.posicionar_canto()

    def posicionar_canto(self):
        screen = QApplication.primaryScreen().geometry()
        self.move(10, screen.height() - self.height() - 10)

    def enviar(self):
        comando = self.input.text()
        self.output.setText("Processando...")

        resposta = self.processar(comando)

        self.output.setText(resposta)
        self.input.clear()