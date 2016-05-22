const electron = require('electron');
const {app, BrowserWindow} = electron;

let win;
function createWindow() {
  win = new BrowserWindow({width: 800, height: 640});
  win.loadURL(`file://${__dirname}/index.html`);
}

app.on('ready', createWindow);

app.on('window-all-closed', () => {
  if (process.platform !== 'darwin') {
    app.quit();
  }
});

app.on('activate', () => {
  if (win === null) {
    createWindow();
  }
});
