# Windows_RE-Install_Optimize 

## 簡介 / Introduction  
`Windows_RE-Install_Optimize` 是一個基於 Python 和 Batch 腳本開發的工具，旨在為新安裝的 Windows 11 24H2 系統進行 UI/UX 優化，並自動安裝常用軟體。特別針對台灣使用者本地化設計，適合個人使用或協助他人重灌系統。
  
`Windows_RE-Install_Optimize` is a tool developed with Python and Batch scripts to optimize UI/UX for a freshly installed Windows 11 24H2 system and automate the installation of essential software. Tailored for Taiwanese users, it’s ideal for personal use or helping others with system reinstallation.

## 系統優化詳情 / System Optimization Details  
以下是 `Windows_RE-Install_Optimize` 對系統進行的具體優化及其效果：  
Below are the specific optimizations performed by `Windows_RE-Install_Optimize` on the system and their effects:  
- **服務與任務管理 / Service and Task Management**  
  - **停用 Windows Defender 排程任務**：移除掃描、清理、驗證等排程任務（例如 `Windows Defender Scheduled Scan`），減少背景活動，提升系統效能。  
    - **Disables Windows Defender scheduled tasks**: Removes scanning, cleanup, and verification tasks (e.g., `Windows Defender Scheduled Scan`), reducing background activity and improving system performance.  
  - **停用客戶體驗改進計劃（CEIP）任務**：關閉 `Consolidator` 和 `UsbCeip` 等任務，防止系統收集並上傳使用資料，降低資源佔用並提升隱私。  
    - **Disables Customer Experience Improvement Program (CEIP) tasks**: Disables tasks like `Consolidator` and `UsbCeip`, preventing data collection and upload, reducing resource usage and enhancing privacy.  
  - **停用磁碟重組排程與系統還原**：關閉 `ScheduledDefrag` 任務並禁用系統還原功能（`SystemRestore`），減少不必要的磁碟操作，節省空間與效能（但失去還原點保護）。  
    - **Disables disk defragmentation scheduling and System Restore**: Disables `ScheduledDefrag` task and System Restore (`SystemRestore`), reducing unnecessary disk operations, saving space and performance (but losing restore point protection).  
  - **停用非必要服務**：關閉 `SysMain`（超級預載，減少記憶體預載負擔）、`Spooler`（列印服務，無印表機時無用）、`CryptSvc`（加密服務，減少背景加密負載）、`stisvc`（掃描儀服務）、`WerSvc`（錯誤報告）、`ShellHWDetection`（硬體偵測）、`iphlpsvc`（IP 輔助服務）、`TrkWks`（分散式連結追蹤）、`WdiServiceHost` 和 `WdiSystemHost`（診斷服務），大幅降低系統資源佔用，提升運行速度。  
    - **Disables non-essential services**: Turns off `SysMain` (Superfetch, reduces memory preload overhead), `Spooler` (Print Spooler, useless without a printer), `CryptSvc` (Cryptographic Services, reduces background encryption load), `stisvc` (Scanner Service), `WerSvc` (Error Reporting), `ShellHWDetection` (Hardware Detection), `iphlpsvc` (IP Helper), `TrkWks` (Distributed Link Tracking), `WdiServiceHost`, and `WdiSystemHost` (Diagnostic Services), significantly lowering resource usage and boosting speed.  
  - **啟用 WMIC 功能**：透過 `DISM` 添加 WMIC（Windows Management Instrumentation Command-line），確保系統管理工具可用。  
    - **Enables WMIC capability**: Adds WMIC (Windows Management Instrumentation Command-line) via `DISM`, ensuring system management tools remain accessible.  

- **啟動與電源設定 / Boot and Power Settings**  
  - **開機選單延遲設為 0 秒**：使用 `bcdedit /set {bootmgr} timeout 0`，移除開機選單等待時間，直接進入系統，加快啟動速度。  
    - **Sets boot menu timeout to 0 seconds**: Uses `bcdedit /set {bootmgr} timeout 0` to eliminate boot menu delay, speeding up startup.  
  - **調整電源設定**：螢幕 15 分鐘無操作後關閉（`powercfg /x monitor-timeout-ac 15`），硬碟與待機永不休眠（`powercfg /x -disk-timeout-ac 0` 和 `/x -standby-timeout-ac 0`），確保使用時不中斷，適合常開機用戶。  
    - **Adjusts power settings**: Monitor turns off after 15 minutes of inactivity (`powercfg /x monitor-timeout-ac 15`), disk and standby never sleep (`powercfg /x -disk-timeout-ac 0` and `/x -standby-timeout-ac 0`), ensuring uninterrupted use, ideal for always-on users.  
  - **電源選單調整**：停用休眠（`ShowHibernateOption 0`）並啟用睡眠（`ShowSleepOption 1`），簡化選單並保留快速喚醒功能。  
    - **Power menu adjustments**: Disables hibernate (`ShowHibernateOption 0`) and enables sleep (`ShowSleepOption 1`), simplifying the menu while retaining quick wake functionality.  
  - **禁用分頁檔案執行**：設定 `DisablePagingExecutive` 為 1，強制系統核心常駐記憶體，減少硬碟存取，提升效能（需足夠 RAM）。  
    - **Disables paging executive**: Sets `DisablePagingExecutive` to 1, keeping the system kernel in memory, reducing disk access and boosting performance (requires sufficient RAM).  

- **桌面與介面優化 / Desktop and Interface Optimization**  
  - **任務欄調整**：移除搜尋框（`SearchboxTaskbarMode 0`）與任務檢視按鈕（`ShowTaskViewButton 0`），顯示時鐘秒數（`ShowSecondsInSystemClock 1`），圖示永不合併（`TaskbarGlomLevel 2`），簡化介面並提升操作效率。  
    - **Taskbar adjustments**: Removes search box (`SearchboxTaskbarMode 0`) and Task View button (`ShowTaskViewButton 0`), shows seconds in clock (`ShowSecondsInSystemClock 1`), sets icons to never combine (`TaskbarGlomLevel 2`), simplifying the interface and improving efficiency.  
  - **關閉防火牆**：使用 `NetSh advfirewall set allprofiles state off`，停用所有防火牆設定，減少網路延遲與資源佔用（但降低安全性，適合受控環境）。  
    - **Disables firewall**: Uses `NetSh advfirewall set allprofiles state off` to turn off all firewall profiles, reducing network latency and resource usage (but lowers security, suitable for controlled environments).  
  - **自訂檔案總管圖示與快取**：將圖示設為 `imageres.dll,197`（簡化視覺），清除圖示快取（`iconcache.db`），確保圖示更新即時顯示。  
    - **Customizes File Explorer icons and cache**: Sets icons to `imageres.dll,197` (simplified visuals), clears icon cache (`iconcache.db`), ensuring immediate icon updates.  
  - **主題與配色**：啟用色彩優先（`ColorPrevalence 1`），若非 `Zack_Normal_Install` 模式，複製並啟用自訂主題（`Anime.theme`），提升視覺個人化。  
    - **Themes and colors**: Enables color prevalence (`ColorPrevalence 1`), copies and applies custom theme (`Anime.theme`) unless in `Zack_Normal_Install` mode, enhancing visual personalization.  
  - **照片檢視器背景**：設定為深色（`BackgroundColor 4278190080`），改善圖片瀏覽體驗。  
    - **Photo viewer background**: Sets to dark (`BackgroundColor 4278190080`), improving image viewing experience.
  - **最佳視覺效果**：自動開啟「效能選項」並選擇「調整為最佳外觀」，啟用所有視覺效果（如視窗動畫、陰影、平滑字體），增強桌面美觀度（可能略增加資源使用）。
    - **Best visual effects**:open "Performance Options" and select "Adjust for best appearance," enabling all visual effects (e.g., window animations, shadows, smooth fonts), enhancing desktop aesthetics (may slightly increase resource usage).  

- **其他調整 / Miscellaneous Tweaks**  
  - **停用 Office 保護檢視**：對 Excel、Word、PowerPoint 停用附件、網路檔案、不安全位置的限制（`DisableAttachmentsInPV` 等設為 1），加快文件開啟速度（但增加安全性風險）。  
    - **Disables Office Protected View**: Disables restrictions for attachments, internet files, and unsafe locations in Excel, Word, PowerPoint (`DisableAttachmentsInPV` etc. set to 1), speeding up file opening (but increasing security risks).  
  - **移除 OneDrive**：執行 `OneDriveSetup.exe /uninstall`，完全移除預裝 OneDrive，釋放空間並避免背景同步。  
    - **Removes OneDrive**: Runs `OneDriveSetup.exe /uninstall` to fully remove preinstalled OneDrive, freeing space and preventing background sync.   
  - **傳統右鍵選單**：新增登錄項（`CLSID\{86ca1aa0-...}`），恢復 Windows 10 風格右鍵選單，提升操作熟悉度。  
    - **Classic context menu**: Adds registry key (`CLSID\{86ca1aa0-...}`), restoring Windows 10-style right-click menu for improved familiarity.  

## 安裝與使用 / Installation and Usage  
### 環境需求 / Requirements  
- Windows 11 24H2，管理員權限，至少 2GB 可用空間。  
- Windows 11 24H2, administrator privileges, at least 2GB free space.

### 下載與準備 / Download and Setup  
- GitHub 專案頁面：點擊「Code」按鈕，選擇「Download ZIP」以下載程式碼壓縮檔。解壓後將必要安裝檔案放入指定資料夾。  
- GitHub project page: click the “Code” button, and select “Download ZIP” to download the code archive. Extract it and place necessary installation files into the designated folders.

### 使用方法 / How to Use  
1. 雙擊 `Optimize.exe` 啟動。  
   Double-click `Optimize.exe` to launch.  
2. 選擇功能（輸入 1-6）：  
   Select an option (enter 1-6):  
   - `1. RE-Install_Optimize`：優化與安裝 / Optimize and install  
     - **選項說明 / Option Details**（建議全選 N 使用）：  
       - `Zack_Install_Mode`：一般選 N，Y 表示我自己個人使用模式，N 表示正常安裝模式（適用一般用戶）。  
         - `Zack_Install_Mode`: Normally select N, Y for my personal use mode, N for standard install mode (for general users).  
       - `CrackActivation`：一般選 N，Y 表示啟用破解激活（如 Windows、Office），N 表示不破解（合法使用）。  
         - `CrackActivation`: Normally select N, Y for enabling activation (e.g., Windows, Office), N for no activation (legal use).  
       - `DATARestore`：一般選 N，Y 表示還原使用者資料（從 D:\Backup），N 表示不還原。  
         - `DATARestore`: Normally select N, Y to restore user data (from D:\Backup), N to skip.  
       - `AnyDeskRestore`：一般選 N，Y 表示還原 AnyDesk 設定（從 D:\Backup），N 表示不還原。  
         - `AnyDeskRestore`: Normally select N, Y to restore AnyDesk settings (from D:\Backup), N to skip.  
   - `2. mpv.net-DW_Update`：更新 mpv.net / Update mpv.net  
   - `3. mpv.net-DW_Backup`：備份 mpv.net / Backup mpv.net  
   - `4. DATABackup`：備份資料 / Backup data  
   - `5. Zack_DATABackup`：我自己個人使用模式 / for my personal use mode
   - `6. Exit`：退出 / Exit  
3. 按提示輸入選項或電腦名稱，確認後執行。  
   Follow prompts to input options or computer name, then confirm to execute.

### 注意事項 / Notes  
- 需管理員權限，破解功能請合法使用。備份前確認 D:\Backup 路徑，部分功能需網路連線。  
- Requires admin rights; use activation features legally. Ensure D:\Backup exists for backups; some features need internet.

## 範例 / Examples  
- **重灌與優化 / Reinstall and Optimize**：選擇 1，輸入電腦名稱，確認後完成。  
  Select 1, enter computer name, confirm to complete.  
- **備份資料 / Backup Data**：選擇 4，等待完成。  
  Select 4, wait for completion.

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