# 🛠️ Streamlit Configuration Guide

This guide explains how to set up the `config.toml` for this project to ensure the correct theme and UI settings.

---

### 🔍 Locate the File

The configuration file is typically located in your operating system's profile directory:

| OS | Default Path |
| :--- | :--- |
| **Windows** | `C:\Users\<Name>\.streamlit\config.toml` |
| **macOS / Linux** | `~/.streamlit/config.toml` |

> [!TIP]
> On Windows, you can enter `%userprofile%\.streamlit` directly into the Explorer address bar to jump to the folder.

---

### 📄 Create File (if missing)

If the folder or file is missing, follow these steps:

1. **Create Folder:** Navigate to your user directory and create a new folder named `.streamlit`.
2. **Create File:** Inside the `.streamlit` folder, create a new text file named `config.toml`.
3. **Insert Content:** Copy the following block into the file:

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

### ✅ Test the Configuration

Restart the app to verify that the settings have been applied:

```bash
streamlit run streamlit_app.py
```

> [!NOTE]
> The `config.toml` controls the primary appearance of the app. If the visualizations are optimized for Light Mode, the `base = "light"` setting is mandatory.