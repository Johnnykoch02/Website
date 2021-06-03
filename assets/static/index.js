let timers = []
function timerHandler(id) {
    timers.push(new Timer(id));
}
function deleteNote(noteId) {

    fetch( '/delete-note', {
        method: 'POST',
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        window.location.href = "/";
    });
}
function unqeueGroup(groupId) {
    console.log("in function")
    fetch( '/unactivate-group', {
        method: 'POST',
        body: JSON.stringify({ groupId: groupId }),
    }).then((_res) => {
        window.location.href = "/rentals";
    });
}