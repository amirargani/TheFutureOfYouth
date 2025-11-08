### 🛠️ `config.toml` unter Windows finden oder erstellen

#### 🔍 Pfad zur Datei
- **Windows:**  
  `C:\Users\<Benutzername>\.streamlit\config.toml`  
- **macOS/Linux:**  
  `~/.streamlit/config.toml`

#### 📍 Schnellzugriff im Explorer
```plaintext
%userprofile%\.streamlit
```
Falls vorhanden, liegt dort bereits `config.toml`.

---

### 📄 Datei oder Ordner fehlt?

#### 🧱 Manuell erstellen
1. Im Explorer zu  
   `C:\Users\<Benutzername>\`  
   navigieren.

2. Neuen Ordner erstellen:  
   `.streamlit`  
   *(Punkt am Anfang ist erlaubt.)*

3. Editor öffnen (z. B. Notepad) und einfügen:
   ```toml
   [theme]
   base = "light"
   ```

4. Speichern als:  
   `config.toml`  
   im `.streamlit`-Ordner.

---

### ✅ Funktionstest

Streamlit-App starten:
```bash
streamlit run app.py
```