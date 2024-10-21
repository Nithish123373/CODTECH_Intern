const express = require('express');
const http = require('http');
const path = require('path');
const socketIo = require('socket.io');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);
const port = 5000;

// Serve static files (HTML, CSS)
app.use(express.static(path.join(__dirname)));

// Handle socket connection
io.on('connection', (socket) => {
    console.log('A user connected');

    // Listen for 'chat message' event from any client
    socket.on('chat message', (data) => {
        // Emit the message data to all connected clients
        io.emit('chat message', data);
    });

    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

// Start the server
server.listen(port, () => {
    console.log(`Server is listening at http://localhost:${port}`);
});
