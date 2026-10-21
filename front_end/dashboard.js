async function updateServices() {
    // gets services responce from api
    const response = await fetch("http://10.0.0.252:8000/services");
    // turns responce to json format
    const data = await response.json();

    //
    document.getElementById("jellyfin").textContent =
        data.message.jellyfin ? "Online" : "Offline";
    document.getElementById("pihole").textContent =
        data.message.jellyfin ? "Online" : "Offline";
    document.getElementById("qbittorrent").textContent =
        data.message.jellyfin ? "Online" : "Offline";
    document.getElementById("nginx").textContent =
        data.message.jellyfin ? "Online" : "Offline";
}

async function updatemonitoring() {
    // gets services responce from api
    const response = await fetch("http://10.0.0.252:8000/monitor");
    // turns responce to json format
    const data = await response.json();

    //gets element from html and changes it to the jsons cpu key value value
    document.getElementById("cpu").textContent = data.cpu + "%";
    document.getElementById("ram").textContent = data.ram + "%";
    document.getElementById("storage").textContent = data.storage + "%";
    document.getElementById("temp").textContent = data.temp + "C";

}

updateServices();
updatemonitoring();

setInterval(updateServices, 1000);
setInterval(updatemonitoring, 1000);