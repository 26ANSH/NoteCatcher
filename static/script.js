function number_of_notes(change) {
    document.getElementById('note-num').innerHTML = parseInt(document.getElementById('note-num').innerHTML) + change

    if (parseInt(document.getElementById('note-num').innerHTML) < 0) {
        document.getElementById('note-num').innerHTML = 0
    }

}

function note_update(color, text){
    document.getElementById('note-updates').innerHTML = `<div class="alert alert-${color} alert-dismissible fade show" role="alert">
    ${text}
    <button type="button" class="btn-close" data-bs-dismiss="alert" style="font-size:2vh;" aria-label="Close"></button>
  </div>`
}

function deletenote(noteid) {
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({ noteid: noteid }),
    }).then((_res) => {
        number_of_notes(-1)
        note_update('danger', 'Note Deleted Successfully')
    });
}

function logout() {
    fetch("/logout", {
        method: "POST",
    }).then((_res) => {
        window.location.href = '/';
    });
}

function newnote() {
    var note = document.getElementById("new_note").value;
    if (note != '') {
        document.getElementById("new_note").value = '';
        fetch("/add-note", {
            method: "POST",
            body: JSON.stringify({ note_data: note }),
        }).then((_res) => {
            number_of_notes(1)
            note_update('success', 'Note Successfully Added')
            _res.json().then(data => {
                notes = `<div class='alert alert-secondary alert-dismissible fade show text-dark' role='alert'>
                ` + note + `
                <button type='button' onclick="deletenote('${data.noteid}')" class='btn-close' data-bs-dismiss='alert'
                  aria-label='Close'></button>
                </div>`
                document.getElementById('notes_section').innerHTML += notes
            });
        });
    }
}