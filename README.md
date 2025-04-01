# Windows_RE-Install_Optimize 
# Windows 11 24H2 優化與安裝工具  
# Windows 11 24H2 Optimization and Installation Tool

## 簡介 / Introduction  
`Windows_RE-Install_Optimize` 是一個基於 Python 和 Batch 腳本開發的工具，旨在為新安裝的 Windows 11 24H2 系統進行 UI/UX 優化，並自動安裝常用軟體。特別針對台灣使用者本地化設計，適合個人使用或協助他人重灌系統。
  
`Windows_RE-Install_Optimize` is a tool developed with Python and Batch scripts to optimize UI/UX for a freshly installed Windows 11 24H2 system and automate the installation of essential software. Tailored for Taiwanese users, it’s ideal for personal use or helping others with system reinstallation.

## 功能 / Features  
1. **UI/UX 優化 / UI/UX Optimization**  
   - 關閉不必要服務、調整系統設定、優化桌面體驗。  
   - Disables unnecessary services, adjusts system settings, and enhances desktop experience.  
2. **軟體安裝 / Software Installation**  
   - 安裝常用軟體（Visual C++、Chrome 等），支援破解激活及個人化模式。  
   - Installs common software (Visual C++, Chrome, etc.), supports activation and personalized modes.  
3. **資料備份與還原 / Data Backup and Restore**  
   - 備份桌面、文件等至 D:\Backup，支援 AnyDesk 設定管理。  
   - Backs up Desktop, Documents, etc., to D:\Backup, with AnyDesk configuration support.  
4. **系統重灌與設定 / System Reinstallation and Setup**  
   - 提供標準及個人化模式，可自訂電腦名稱。  
   - Offers standard and personalized modes with custom computer name setup.

## 安裝與使用 / Installation and Usage  
### 環境需求 / Requirements  
- Windows 11 24H2，管理員權限，至少 2GB 可用空間。  
- Windows 11 24H2, administrator privileges, at least 2GB free space.

### 下載與準備 / Download and Setup  
- GitHub 專案頁面：點擊「Code」按鈕，選擇「Download ZIP」以下載程式碼壓縮檔。解壓後將必要安裝檔案放入指定資料夾。  
- GitHub project page:click the “Code” button, and select “Download ZIP” to download the code archive. Extract it and place necessary installation files into the designated folders.

### 使用方法 / How to Use  
1. 雙擊 `Optimize.exe` 啟動。  
   Double-click `Optimize.exe` to launch.  
2. 選擇功能（輸入 1-6）：  
   Select an option (enter 1-6):  
   - `1. RE-Install_Optimize`：優化與安裝 / Optimize and install  
   - `2. mpv.net-DW_Update`：更新 mpv.net / Update mpv.net  
   - `3. mpv.net-DW_Backup`：備份 mpv.net / Backup mpv.net  
   - `4. DATABackup`：備份資料 / Backup data  
   - `5. Zack_DATABackup`：個人化備份 / Personalized backup  
   - `6. Exit`：退出 / Exit  
3. 按提示輸入選項或電腦名稱，確認後執行。  
   Follow prompts to input options or computer name, then confirm to execute.

### 注意事項 / Notes  
- 需管理員權限，破解功能請合法使用。備份前確認 D:\Backup 路徑，部分功能需網路連線。  
- Requires admin rights; use activation features legally. Ensure D:\Backup exists for backups; some features need internet.

## 範例 / Examples  
- **重灌與優化 / Reinstall and Optimize**：選擇 1，輸入電腦名稱，確認後完成。  
  Select 1, enter computer name, confirm to complete.  
- **備份資料 / Backup Data**：選擇 4，確認 AnyDesk 備份，等待完成。  
  Select 4, confirm AnyDesk backup, wait for completion.

## 已知問題 / Known Issues  
- D: 磁碟不存在時備份可能失敗；網路不穩可能影響安裝；非中文系統或有亂碼。  
- Backup may fail without D: drive; unstable network may affect installation; non-Chinese systems may show garbled text.

## 貢獻 / Contribution  
此為個人專案，歡迎建議或提交 Pull Request。  
This is a personal project; suggestions or Pull Requests are welcome.

## 版權與免責聲明 / License and Disclaimer  
- 作者 / Author：Zack  
- 版本 / Version：Ver240316  
- 僅限學習與個人使用，作者不承擔使用損失責任。  
- For educational and personal use only; the author is not liable for any damages.