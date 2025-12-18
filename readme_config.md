# 🛠️ Streamlit Konfigurations-Guide

In diesem Guide erfährst du, wie du die `config.toml` für dieses Projekt einrichtest, um das korrekte Theme (Design) zu gewährleisten.

---

### 🔍 Datei finden

Die Konfigurationsdatei befindet sich standardmäßig im Profilverzeichnis deines Betriebssystems:

| OS | Standard-Pfad |
| :--- | :--- |
| **Windows** | `C:\Users\<Name>\.streamlit\config.toml` |
| **macOS / Linux** | `~/.streamlit/config.toml` |

> [!TIP]
> Unter Windows kannst du `%userprofile%\.streamlit` direkt in die Adresszeile des Explorers eingeben, um zum Ordner zu springen.

---

### 📄 Datei erstellen (falls nicht vorhanden)

Sollte der Ordner oder die Datei fehlen, befolge diese Schritte:

1. **Ordner erstellen:** Navigiere zu deinem Benutzerordner und erstelle einen neuen Ordner namens `.streamlit`.
2. **Datei erstellen:** Erstelle im Ordner `.streamlit` eine neue Textdatei mit dem Namen `config.toml`.
3. **Inhalt einfügen:** Kopiere den folgenden Block in die Datei:

```toml
[theme]
base = "light"
primaryColor = "#FF4B4B"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F0F2F6"
textColor = "#31333F"
font = "sans serif"
```

---

### ✅ Testen der Konfiguration

Starte die App erneut, um zu prüfen, ob die Änderungen übernommen wurden:

```bash
streamlit run streamlit_app.py
```

> [!NOTE]
> Die `config.toml` steuert das primäre Erscheinungsbild der App. Falls die Grafiken im Light-Mode besser lesbar sind, ist die Einstellung `base = "light"` zwingend erforderlich.