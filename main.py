import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout,
    QHBoxLayout, QPushButton, QTextEdit, QLabel,
    QTabWidget, QStatusBar, QMenuBar, QMenu
)
from PyQt6.QtGui import QFont, QColor, QSyntaxHighlighter, QTextCharFormat, QAction
from PyQt6.QtCore import Qt, QRegularExpression
from interpreter import BasicInterpreter
from examples import EXAMPLES

THEMES = {
    "Lovelace": {
        "window": "#0d0d0d", "border": "#8b0000",
        "title": "#0d0d0d", "title_text": "#f5f0e8", "title_sub": "#5a4a3a",
        "menu": "#111111", "menu_border": "#1e1e1e", "menu_text": "#5a4a3a", "menu_active": "#8b0000",
        "toolbar": "#0d0d0d", "toolbar_border": "#1e1e1e",
        "tbtn": "#1a1a1a", "tbtn_text": "#f5f0e8", "tbtn_border": "#2a2a2a",
        "tbtn_prim": "#8b0000", "tbtn_prim_text": "#f5f0e8",
        "badge": "#0d0d0d", "badge_text": "#8b0000", "badge_border": "#8b0000",
        "tab_active": "#111111", "tab_active_text": "#f5f0e8", "tab_text": "#3a3a3a",
        "panel_header": "#111111", "panel_header_text": "#5a4a3a", "panel_dot": "#8b0000",
        "code_bg": "#080808", "code_text": "#f5f0e8", "ln": "#2a2a2a",
        "kw": "#8b0000", "str": "#c8b89a", "num": "#a08060",
        "output_bg": "#050505", "output_text": "#f5f0e8", "output_dim": "#2a2a2a",
        "console": "#0d0d0d", "prompt": "#8b0000",
        "status": "#0a0000", "status_text": "#5a2020", "status_border": "#8b0000",
        "cursor": "#8b0000",
    },
    "Sakura": {
        "window": "#fdf0f3", "border": "#e8a0b0",
        "title": "#c4687a", "title_text": "#fff0f3", "title_sub": "#f2c4ce",
        "menu": "#fce8ed", "menu_border": "#f0b8c4", "menu_text": "#6b2737", "menu_active": "#c4687a",
        "toolbar": "#fdf0f3", "toolbar_border": "#f0b8c4",
        "tbtn": "#fce8ed", "tbtn_text": "#6b2737", "tbtn_border": "#e8a0b0",
        "tbtn_prim": "#c4687a", "tbtn_prim_text": "#fff0f3",
        "badge": "#6b2737", "badge_text": "#f2c4ce", "badge_border": "#6b2737",
        "tab_active": "#fff8fa", "tab_active_text": "#6b2737", "tab_text": "#d4a0a8",
        "panel_header": "#fce8ed", "panel_header_text": "#6b2737", "panel_dot": "#c4687a",
        "code_bg": "#fff8fa", "code_text": "#3d1520", "ln": "#e8a0b0",
        "kw": "#c4687a", "str": "#8a3a4a", "num": "#a04060",
        "output_bg": "#6b2737", "output_text": "#f2c4ce", "output_dim": "#a06070",
        "console": "#fce8ed", "prompt": "#c4687a",
        "status": "#c4687a", "status_text": "#fff0f3", "status_border": "#c4687a",
        "cursor": "#c4687a",
    },
    "Mint": {
        "window": "#c7f0d8", "border": "#43523d",
        "title": "#43523d", "title_text": "#c7f0d8", "title_sub": "#8aab80",
        "menu": "#d8f5e6", "menu_border": "#a8d4b8", "menu_text": "#43523d", "menu_active": "#43523d",
        "toolbar": "#c7f0d8", "toolbar_border": "#a8d4b8",
        "tbtn": "#d8f5e6", "tbtn_text": "#43523d", "tbtn_border": "#8aab80",
        "tbtn_prim": "#43523d", "tbtn_prim_text": "#c7f0d8",
        "badge": "#43523d", "badge_text": "#c7f0d8", "badge_border": "#43523d",
        "tab_active": "#e8faf0", "tab_active_text": "#43523d", "tab_text": "#8aab80",
        "panel_header": "#d8f5e6", "panel_header_text": "#43523d", "panel_dot": "#43523d",
        "code_bg": "#f0fdf4", "code_text": "#43523d", "ln": "#a8d4b8",
        "kw": "#2d5a3d", "str": "#43523d", "num": "#5a7a4a",
        "output_bg": "#43523d", "output_text": "#c7f0d8", "output_dim": "#6a8a6a",
        "console": "#d8f5e6", "prompt": "#43523d",
        "status": "#43523d", "status_text": "#c7f0d8", "status_border": "#43523d",
        "cursor": "#43523d",
    },
    "Military": {
        "window": "#1a2418", "border": "#43523d",
        "title": "#43523d", "title_text": "#c7f0d8", "title_sub": "#8aab80",
        "menu": "#2d3d29", "menu_border": "#43523d", "menu_text": "#8aab80", "menu_active": "#c7f0d8",
        "toolbar": "#1a2418", "toolbar_border": "#2d3d29",
        "tbtn": "#2d3d29", "tbtn_text": "#c7f0d8", "tbtn_border": "#43523d",
        "tbtn_prim": "#43523d", "tbtn_prim_text": "#c7f0d8",
        "badge": "#1a2418", "badge_text": "#c7f0d8", "badge_border": "#43523d",
        "tab_active": "#2d3d29", "tab_active_text": "#c7f0d8", "tab_text": "#43523d",
        "panel_header": "#2d3d29", "panel_header_text": "#8aab80", "panel_dot": "#c7f0d8",
        "code_bg": "#111a10", "code_text": "#c7f0d8", "ln": "#43523d",
        "kw": "#c7f0d8", "str": "#a8d4b8", "num": "#d4f0c7",
        "output_bg": "#0d140c", "output_text": "#c7f0d8", "output_dim": "#43523d",
        "console": "#111a10", "prompt": "#c7f0d8",
        "status": "#43523d", "status_text": "#c7f0d8", "status_border": "#43523d",
        "cursor": "#c7f0d8",
    },
    "iBook": {
        "window": "#e8eef2", "border": "#5b8fa8",
        "title": "#5b8fa8", "title_text": "#ffffff", "title_sub": "#c8dde8",
        "menu": "#f0f4f7", "menu_border": "#c8d8e4", "menu_text": "#2a4a5a", "menu_active": "#2a4a5a",
        "toolbar": "#e8eef2", "toolbar_border": "#c8d8e4",
        "tbtn": "#f0f4f7", "tbtn_text": "#2a4a5a", "tbtn_border": "#a8c4d4",
        "tbtn_prim": "#5b8fa8", "tbtn_prim_text": "#ffffff",
        "badge": "#2a4a5a", "badge_text": "#c8dde8", "badge_border": "#2a4a5a",
        "tab_active": "#f8fafc", "tab_active_text": "#2a4a5a", "tab_text": "#7aaabb",
        "panel_header": "#f0f4f7", "panel_header_text": "#2a4a5a", "panel_dot": "#5b8fa8",
        "code_bg": "#f8fafc", "code_text": "#2a4a5a", "ln": "#a8c4d4",
        "kw": "#1a5a7a", "str": "#2a6a4a", "num": "#5a4a8a",
        "output_bg": "#2a4a5a", "output_text": "#c8dde8", "output_dim": "#4a7a8a",
        "console": "#f0f4f7", "prompt": "#2a4a5a",
        "status": "#5b8fa8", "status_text": "#ffffff", "status_border": "#5b8fa8",
        "cursor": "#5b8fa8",
    },
    "Nokia": {
        "window": "#0a1628", "border": "#0077b6",
        "title": "#1a1f3a", "title_text": "#00b4d8", "title_sub": "#8892a4",
        "menu": "#1a1f3a", "menu_border": "#0077b6", "menu_text": "#8892a4", "menu_active": "#00b4d8",
        "toolbar": "#0a1628", "toolbar_border": "#0077b6",
        "tbtn": "#1a1f3a", "tbtn_text": "#cdd6f4", "tbtn_border": "#0077b6",
        "tbtn_prim": "#00b4d8", "tbtn_prim_text": "#0a1628",
        "badge": "#0a1628", "badge_text": "#00b4d8", "badge_border": "#0077b6",
        "tab_active": "#1a1f3a", "tab_active_text": "#00b4d8", "tab_text": "#0077b6",
        "panel_header": "#1a1f3a", "panel_header_text": "#8892a4", "panel_dot": "#00b4d8",
        "code_bg": "#0d1117", "code_text": "#cdd6f4", "ln": "#0077b6",
        "kw": "#00b4d8", "str": "#00f5d4", "num": "#f4a261",
        "output_bg": "#050a10", "output_text": "#00b4d8", "output_dim": "#0077b6",
        "console": "#0d1117", "prompt": "#00b4d8",
        "status": "#1a1f3a", "status_text": "#8892a4", "status_border": "#0077b6",
        "cursor": "#00b4d8",
    },
}


class BasicHighlighter(QSyntaxHighlighter):
    def __init__(self, parent, theme):
        super().__init__(parent)
        self.theme = theme
        self._build_rules()
        self.current_language = "BASIC"

    def _build_rules(self):
        self.rules = []
        th = self.theme

        kw_fmt = QTextCharFormat()
        kw_fmt.setForeground(QColor(th["kw"]))
        kw_fmt.setFontWeight(700)
        for word in ['PRINT','LET','IF','THEN','GOTO','FOR','NEXT','END','INPUT','REM','TO','STEP','GOSUB','RETURN']:
            self.rules.append((QRegularExpression(f'\\b{word}\\b',
                QRegularExpression.PatternOption.CaseInsensitiveOption), kw_fmt))

        str_fmt = QTextCharFormat()
        str_fmt.setForeground(QColor(th["str"]))
        self.rules.append((QRegularExpression('"[^"]*"'), str_fmt))

        num_fmt = QTextCharFormat()
        num_fmt.setForeground(QColor(th["num"]))
        self.rules.append((QRegularExpression('\\b[0-9]+\\b'), num_fmt))

        ln_fmt = QTextCharFormat()
        ln_fmt.setForeground(QColor(th["ln"]))
        self.rules.append((QRegularExpression('^[0-9]+'), ln_fmt))

    def highlightBlock(self, text):
        for pattern, fmt in self.rules:
            it = pattern.globalMatch(text)
            while it.hasNext():
                m = it.next()
                self.setFormat(m.capturedStart(), m.capturedLength(), fmt)


class ADAWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.interpreter = BasicInterpreter()
        self.current_theme = "Lovelace"
        self.setup_ui()
        self.apply_theme()

    def setup_ui(self):
        self.setWindowTitle("ADA — Legacy Code Interpreter")
        self.setMinimumSize(1100, 700)

        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # Menu bar
        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")
        file_menu.addAction(QAction("New", self))
        file_menu.addAction(QAction("Open", self))
        file_menu.addAction(QAction("Save", self))

        lang_menu = menubar.addMenu("Language")
        for lang in ["BASIC", "Pascal", "COBOL", "Fortran","Ada"]:
            action = QAction(lang, self)
            action.triggered.connect(lambda checked, l=lang: self.switch_language(l))
            lang_menu.addAction(action)

        theme_menu = menubar.addMenu("Theme")
        for name in THEMES:
            action = QAction(name, self)
            action.triggered.connect(lambda checked, n=name: self.switch_theme(n))
            theme_menu.addAction(action)

        # Toolbar
        toolbar_widget = QWidget()
        toolbar_layout = QHBoxLayout(toolbar_widget)
        toolbar_layout.setContentsMargins(12, 8, 12, 8)
        toolbar_layout.setSpacing(8)

        self.run_btn = QPushButton("▶  RUN")
        self.run_btn.setFont(QFont("Courier New", 11, QFont.Weight.Bold))
        self.run_btn.setFixedHeight(36)
        self.run_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.run_btn.clicked.connect(self.run_code)

        self.stop_btn = QPushButton("■  STOP")
        self.stop_btn.setFont(QFont("Courier New", 11))
        self.stop_btn.setFixedHeight(36)
        self.stop_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        self.new_btn = QPushButton("NEW")
        self.new_btn.setFont(QFont("Courier New", 10))
        self.new_btn.setFixedHeight(36)
        self.new_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.new_btn.clicked.connect(lambda: self.editor.clear())

        self.clear_btn = QPushButton("CLEAR OUTPUT")
        self.clear_btn.setFont(QFont("Courier New", 10))
        self.clear_btn.setFixedHeight(36)
        self.clear_btn.setCursor(Qt.CursorShape.PointingHandCursor)
        self.clear_btn.clicked.connect(lambda: self.output.clear())

        self.badge = QLabel("BASIC v1.0")
        self.badge.setFont(QFont("Courier New", 10))
        self.badge.setAlignment(Qt.AlignmentFlag.AlignCenter)

        toolbar_layout.addWidget(self.run_btn)
        toolbar_layout.addWidget(self.stop_btn)
        toolbar_layout.addSpacing(8)
        toolbar_layout.addWidget(self.new_btn)
        toolbar_layout.addWidget(self.clear_btn)
        toolbar_layout.addStretch()
        toolbar_layout.addWidget(self.badge)
        main_layout.addWidget(toolbar_widget)
        self.toolbar_widget = toolbar_widget

        # Editor + Output
        content = QWidget()
        content_layout = QHBoxLayout(content)
        content_layout.setContentsMargins(12, 8, 12, 8)
        content_layout.setSpacing(12)

        # Editor
        editor_container = QWidget()
        editor_layout = QVBoxLayout(editor_container)
        editor_layout.setContentsMargins(0, 0, 0, 0)
        editor_layout.setSpacing(4)
        self.editor_label = QLabel("▸ SOURCE CODE")
        self.editor_label.setFont(QFont("Courier New", 9, QFont.Weight.Bold))
        self.editor = QTextEdit()
        self.editor.setFont(QFont("Courier New", 13))
        self.editor.setText("""10 PRINT "Welcome to ADA!"
20 PRINT "In memory of Ada Lovelace, 1815"
30 LET X = 1
40 FOR I = 1 TO 8
50 LET X = X * 2
60 PRINT X
70 NEXT I
80 PRINT "Done."
90 END""")
        editor_layout.addWidget(self.editor_label)
        editor_layout.addWidget(self.editor)
        content_layout.addWidget(editor_container, 3)

        # Output
        output_container = QWidget()
        output_layout = QVBoxLayout(output_container)
        output_layout.setContentsMargins(0, 0, 0, 0)
        output_layout.setSpacing(4)
        self.output_label = QLabel("▸ OUTPUT")
        self.output_label.setFont(QFont("Courier New", 9, QFont.Weight.Bold))
        self.output = QTextEdit()
        self.output.setFont(QFont("Courier New", 13))
        self.output.setReadOnly(True)
        output_layout.addWidget(self.output_label)
        output_layout.addWidget(self.output)
        content_layout.addWidget(output_container, 2)

        main_layout.addWidget(content)

        # Status bar
        self.status = self.statusBar()
        self.status_label = QLabel("● READY  ·  BASIC  ·  in memory of Ada Lovelace, 1815  ·  ADA v1.0")
        self.status_label.setFont(QFont("Courier New", 9))
        self.status.addWidget(self.status_label)

    def apply_theme(self):
        th = THEMES[self.current_theme]

        self.setStyleSheet(f"""
            QMainWindow {{ background: {th['window']}; }}
            QMenuBar {{ background: {th['menu']}; color: {th['menu_text']}; border-bottom: 1px solid {th['menu_border']}; font-family: 'Courier New'; font-size: 12px; }}
            QMenuBar::item:selected {{ background: {th['tbtn_prim']}; color: {th['tbtn_prim_text']}; }}
            QMenu {{ background: {th['menu']}; color: {th['menu_text']}; border: 1px solid {th['menu_border']}; font-family: 'Courier New'; }}
            QMenu::item:selected {{ background: {th['tbtn_prim']}; color: {th['tbtn_prim_text']}; }}
        """)

        self.toolbar_widget.setStyleSheet(f"background: {th['toolbar']}; border-bottom: 1px solid {th['toolbar_border']};")

        self.run_btn.setStyleSheet(f"""
            QPushButton {{ background: {th['tbtn_prim']}; color: {th['tbtn_prim_text']}; border: none; border-radius: 6px; padding: 0 20px; letter-spacing: 2px; }}
            QPushButton:hover {{ opacity: 0.8; }}
        """)

        for btn in [self.stop_btn, self.new_btn, self.clear_btn]:
            btn.setStyleSheet(f"""
                QPushButton {{ background: {th['tbtn']}; color: {th['tbtn_text']}; border: 1px solid {th['tbtn_border']}; border-radius: 6px; padding: 0 16px; letter-spacing: 1px; }}
                QPushButton:hover {{ border-color: {th['tbtn_prim']}; }}
            """)

        self.badge.setStyleSheet(f"background: {th['badge']}; color: {th['badge_text']}; border: 1px solid {th['badge_border']}; border-radius: 4px; padding: 3px 12px; letter-spacing: 1px;")

        self.editor_label.setStyleSheet(f"color: {th['panel_dot']};")
        self.output_label.setStyleSheet(f"color: {th['panel_dot']};")

        self.editor.setStyleSheet(f"""
            QTextEdit {{ background: {th['code_bg']}; color: {th['code_text']}; border: 1px solid {th['tbtn_border']}; border-radius: 8px; padding: 12px; selection-background-color: {th['tbtn_prim']}; }}
        """)

        self.output.setStyleSheet(f"""
            QTextEdit {{ background: {th['output_bg']}; color: {th['output_text']}; border: 1px solid {th['tbtn_border']}; border-radius: 8px; padding: 12px; }}
        """)

        self.status.setStyleSheet(f"background: {th['status']}; border-top: 1px solid {th['status_border']};")
        self.status_label.setStyleSheet(f"color: {th['status_text']};")

        # Rehighlight
        self.highlighter = BasicHighlighter(self.editor.document(), th)
    def switch_language(self, lang):
        self.current_language = lang
        self.editor.setText(EXAMPLES[lang])
        self.badge.setText(f"{lang} v1.0")
        self.output.clear()
        self.status_label.setText(f"● READY  ·  {lang}  ·  in memory of Ada Lovelace, 1815  ·  ADA v1.0")

    def switch_theme(self, name):
        self.current_theme = name
        self.apply_theme()

    def run_code(self):
        from languages import INTERPRETERS
        code = self.editor.toPlainText()
        if not code.strip():
            self.output.setText("No code to run.")
            return
        self.status_label.setText("● RUNNING...")
        QApplication.processEvents()
        try:
            lang = getattr(self, 'current_language', 'BASIC')
            interp = INTERPRETERS[lang]()
            if lang == 'BASIC':
                interp.load(code)
            result = interp.run(code) if lang != 'BASIC' else interp.run()
            self.output.setText(result if result else "(no output)")
            self.status_label.setText(f"● DONE  ·  {lang}  ·  ADA v1.0")
        except Exception as e:
            self.output.setText(f"ERROR: {str(e)}")
            self.status_label.setText("● ERROR")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = ADAWindow()
    window.show()
    sys.exit(app.exec())