function deletenote(noteid){
    fetch("/delete-note", {
        method: "POST",
        body: JSON.stringify({noteid: noteid}),
    }).then((_res) => {
        var num = document.getElementById('note-num')
        current = num.innerHTML
        num.innerHTML = current  - 1
});
}

function logout(){
    fetch("/logout", {
        method: "POST",
    }).then((_res) => {
        window.location.href = '/';
    });
}