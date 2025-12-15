### 🛠️ Finding or Creating `config.toml` on Windows

#### 🔍 File Path

* **Windows:**
  `C:\Users\<username>\.streamlit\config.toml`
* **macOS / Linux:**
  `~/.streamlit/config.toml`

#### 📍 Quick Access via File Explorer

```plaintext
%userprofile%\.streamlit
```

If the file already exists, you will find `config.toml` there.

---

### 📄 File or Folder Missing?

#### 🧱 Create Manually

1. In File Explorer, navigate to
   `C:\Users\<username>\`

2. Create a new folder named:
   `.streamlit`
   *(A leading dot is allowed.)*

3. Open a text editor (e.g., Notepad) and insert:

   ```toml
   [theme]
   base = "light"
   ```

4. Save the file as:
   `config.toml`
   inside the `.streamlit` folder.

---

### ✅ Test the Configuration

Start the Streamlit app:

```bash
streamlit run app.py
```