async function updateServices() {
    // gets services responce from api
    const response = await fetch("http://127.0.0.1:8000/services");
    // turns responce to json format
    const data = await response.json();

    //
    document.getElementById("jellyfin").textContent =
        data.message.jellyfin ? "Online" : "Offline";
}

async function updatemonitoring() {
    // gets services responce from api
    const response = await fetch("http://127.0.0.1:8000/monitor");
    // turns responce to json format
    const data = await response.json();

    //gets element from html and changes it to the jsons cpu key value value
    document.getElementById("cpu").textContent = data.cpu + "%";
    document.getElementById("ram").textContent = data.ram + "%";
    document.getElementById("storage").textContent = data.storage + "%";

}

updateServices();
updatemonitoring();