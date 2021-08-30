const { app, BrowserWindow } = require("electron");
const { autoUpdater } = require("electron-updater");
const log = require("electron-log");
const dev = require("electron-is-dev");
const path = require("path");

let mainWindows;

const createWindow = () => {
  mainWindows = new BrowserWindow({
    maxWidth: 960,
    maxHeight: 540,
    minWidth: 960,
    minHeight: 540,
    width: 960,
    height: 540,
    center: true,
    fullscreen: false,
    webPreferences: {
      nodeIntegration: true,
      enableRemoteModule: true,
      devTools: dev,
    },
  });

  const startURL = dev
    ? process.env.ELECTRON_START_URL
    : `file://${path.join(__dirname, "../build/index.html")}`;

  mainWindows.loadURL(startURL);
  mainWindows.on("closed", () => {
    mainWindows = null;
  });
  mainWindows.focus();
};

app.on("ready", () => {
  createWindow();
  dev ?? autoUpdater.checkForUpdates();
});

app.on("window-all-closed", () => {
  if (process.platform !== "darwin") app.quit();
});

app.on("activate", () => {
  if (mainWindows === null) {
    createWindow();
  }
});

// --- Update ---
autoUpdater.on("checking-for-update", () => {
  log("업데이트 확인 중...");
});

autoUpdater.on("update-available", (info) => {
  log("업데이트가 가능합니다.");
});

autoUpdater.on("update-not-available", (info) => {
  log("현재 최신 버전입니다.");
});

autoUpdater.on("error", (err) => {
  log(`에러가 발생하였습니다. 에러내용: ${err}`);
});

autoUpdater.on("download-progress", (progress) => {
  let logMessage = `다운로드 속도: ${progress.bytesPerSecond}`;
  logMessage = `${logMessage} - 현재 ${progress.percent}%`;
  logMessage = `${logMessage} (${progress.transferred}/${progress.total})`;
  log(logMessage);
});

autoUpdater.on("update-downloaded", (info) => {
  log("업데이트가 완료되었습니다.");
});
