async function updateServices() {
    // gets services responce from api
    const response = await fetch("http://127.0.0.1:8000/services");
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
    // Gets services responce from api
    // Raspberrypi http://10.0.0.252:8000/monitor
    // Mac http://127.0.0.1:8000/monitor
    const response = await fetch("http://127.0.0.1:8000/monitor");
    // turns responce to json format
    const data = await response.json();

    //gets element from html and changes it to the jsons cpu key value value
    document.getElementById("cpu").textContent = data.cpu + "%";
    document.getElementById("cpu-bar").style.width = data.cpu + "%";
    document.getElementById("ram").textContent = data.ram + "%";
    document.getElementById("ram-bar").style.width = data.ram + "%";
    document.getElementById("storage").textContent = data.storage.percent + "%";
    document.getElementById("storage-bar").style.width = data.cpu + "%";
    document.getElementById("temp").textContent = data.temp === null ? "N/A" : data.temp + "°C";
    document.getElementById("upload").textContent = data.network.upload + " MB/s";
    document.getElementById("download").textContent = data.network.download + " MB/s";
    
    

}

updateServices();
updatemonitoring();

setInterval(updateServices, 1000);
setInterval(updatemonitoring, 1000);