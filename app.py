# 豆包购物智能助手 - 真正可交互聊天版
# 双击运行 → 自动打开浏览器 → 实时聊天！

import http.server
import socketserver
import webbrowser
import threading
import time

HTML = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>🛒 豆包购物智能助手（可聊天版）</title>
<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
    font-family: "Microsoft YaHei", Arial;
}
body {
    background: #f2f2f2;
    max-width: 900px;
    margin: 20px auto;
    padding: 0 15px;
}
.container {
    background: white;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    overflow: hidden;
}
.header {
    background: #ff4d00;
    color: white;
    padding: 18px;
    text-align: center;
    font-size: 20px;
    font-weight: bold;
}
.chat-box {
    height: 550px;
    padding: 20px;
    overflow-y: auto;
    background: #fafafa;
}
.bot-message, .user-message {
    margin-bottom: 15px;
    max-width: 80%;
    padding: 12px 15px;
    border-radius: 12px;
    line-height: 1.5;
}
.bot-message {
    background: #e3f2fd;
    float: left;
    clear: both;
}
.user-message {
    background: #ffe0b2;
    float: right;
    clear: both;
    text-align: right;
}
.btns {
    display: flex;
    gap: 10px;
    padding: 15px;
    background: white;
    flex-wrap: wrap;
}
.btn {
    flex: 1;
    min-width: 120px;
    padding: 12px;
    border: none;
    border-radius: 8px;
    background: #ff4d00;
    color: white;
    font-size: 15px;
    cursor: pointer;
}
.btn:hover {
    background: #e44600;
}
.input-area {
    display: flex;
    padding: 15px;
    background: white;
    border-top: 1px solid #eee;
}
#inputText {
    flex: 1;
    padding: 12px 15px;
    border: 1px solid #ddd;
    border-radius: 8px;
    font-size: 15px;
}
#sendBtn {
    margin-left: 10px;
    padding: 12px 20px;
    background: #ff4d00;
    color: white;
    border: none;
    border-radius: 8px;
    cursor: pointer;
}
</style>
</head>

<body>
<div class="container">
    <div class="header">🛒 豆包购物智能助手（可交互版）</div>
    <div class="chat-box" id="chatBox">
        <div class="bot-message">你好！我是你的购物小助手 😊
<br>我可以帮你：
<br>🔍 搜索商品
<br>📊 全网比价
<br>🎯 个性化推荐</div>
    </div>

    <div class="btns">
        <button class="btn" onclick="sendMsg('帮我找200元内蓝牙耳机')">🔍 搜商品</button>
        <button class="btn" onclick="sendMsg('帮我比价这款耳机')">📊 比价</button>
        <button class="btn" onclick="sendMsg('推荐适合我的商品')">🎯 推荐</button>
    </div>

    <div class="input-area">
        <input type="text" id="inputText" placeholder="输入你想买的东西...">
        <button id="sendBtn" onclick="sendMsg()">发送</button>
    </div>
</div>

<script>
function addMessage(text, isUser = false) {
    const chatBox = document.getElementById('chatBox');
    const div = document.createElement('div');
    div.className = isUser ? 'user-message' : 'bot-message';
    div.innerText = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function sendMsg(defaultText = null) {
    const input = document.getElementById('inputText');
    const text = defaultText || input.value.trim();
    if (!text) return;

    addMessage(text, true);
    input.value = '';

    setTimeout(() => {
        let reply = '';
        if (text.includes('搜') || text.includes('耳机') || text.includes('找')) {
            reply = `🔍 为你找到：
1. 无线蓝牙耳机 Pro版 ¥199（淘宝）
2. 小米Air2 SE ¥169（京东）
3. 华为FreeBuds 4i ¥399（拼多多）`;
        } 
        else if (text.includes('比价') || text.includes('便宜')) {
            reply = `📊 全网比价结果：
抖音：¥274 ✅最优
淘宝：¥279
京东：¥279
拼多多：¥284`;
        } 
        else if (text.includes('推荐')) {
            reply = `🎯 为你推荐：
1. 小米手环8 ¥249
2. 倍思蓝牙耳机 ¥198
3. 飞利浦电动牙刷 ¥179`;
        } 
        else {
            reply = "😊 你可以点击下方按钮：搜商品、比价、推荐~";
        }
        addMessage(reply);
    }, 600);
}
</script>
</body>
</html>
"""

# 启动本地服务器
PORT = 1213

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(HTML.encode('utf-8'))

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        httpd.serve_forever()

def open_browser():
    time.sleep(1)
    webbrowser.open(f'http://localhost:{PORT}')

if __name__ == "__main__":
    print("✅ 豆包购物智能助手 启动中...")
    print("🌐 自动打开浏览器，请稍等...")
    print("💡 支持：聊天、按钮点击、搜索、比价、推荐")
    
    threading.Thread(target=start_server, daemon=True).start()
    open_browser()
    
    input("\n按回车键退出...")