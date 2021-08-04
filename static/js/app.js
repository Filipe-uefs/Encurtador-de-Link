
const bnt = document.getElementById("send")
bnt.addEventListener("click", function (e) {
    e.preventDefault();
    var link = document.getElementById("link").value;
    link = link.trim()
    if (link == "") {
        alert("Link requerido")
        return
    }
    async function registerLink() {
        try {
            const response = await fetch("http://127.0.0.1:5000/registerLink", {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ link: link })
            })
            const data = await response.json()
            document.getElementById("display-link").innerHTML = `Link http://127.0.0.1:5000/${data["index"]}`; 
        } catch (error) {
            console.error("erro")
        }
    }
    registerLink()
})


