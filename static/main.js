const usernameInput = document.getElementById('username');
const joinBroadcasterButton = document.getElementById('join-broadcaster');
const joinViewerButton = document.getElementById('join-viewer');

joinBroadcasterButton.addEventListener('click', () => {
    const username = usernameInput.value || 'Anonymous';
    window.location.href = `/broadcast?username=${encodeURIComponent(username)}`;
});

joinViewerButton.addEventListener('click', () => {
    const username = usernameInput.value || 'Anonymous';
    window.location.href = `/viewer?username=${encodeURIComponent(username)}`;
});
