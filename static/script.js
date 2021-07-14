function deletenote(noteid){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteid: noteid}),
    }).then((_res) => {
        window.location.reload()
    });
}

function logout(){
    fetch("/logout", {
        method: "POST",
    }).then((_res) => {
        window.location.href = '/';
    });
}