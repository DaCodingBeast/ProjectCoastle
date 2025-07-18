async function request(apiEndpoint) {
    let data = null;
    try {
        const response = await fetch(`https://projectcoastlebackend.onrender.com/api/${apiEndpoint}/`, {
            method: 'GET',
            headers: { 'Content-Type': 'application/json' },
        });
        data = await response.json();
    } catch (error) {
        console.error('Error starting game:', error);
    }
    return data;

}

async function startGame() {
    console.log("Starting game...");
    const list = document.getElementById('cityDataList');
    // Remove all previous list items
    list.innerHTML = '';
    document.getElementById('map').innerHTML = ``;
    document.getElementById('modelResult').innerText = "";

    const data = await request('meteo');
    console.log('API response:', data);

    if (data && data.result) {
        for (const [key, value] of Object.entries(data.result)) {
            const li = document.createElement('li');
            li.textContent = `${key}: ${value}`;
            list.appendChild(li);
        }
    } else {
        console.log('No result data received from backend.');
    }
}



async function getLocation() {
    console.log("Getting Location");

    data = await request('location');
    console.log(data);

    cityCoords = data.location;

    if (data.location && data.location.length === 2) {
        document.getElementById('map').innerHTML = `
            <iframe
              src="https://maps.google.com/maps?q=${data.location[0]},${data.location[1]}&z=10&output=embed"
              allowfullscreen>
            </iframe>
          `;
    }

}

async function getPerceptronPrediction() {
    
    console.log("Getting Prediction...");

    data = await request('perceptronGuess');
    console.log(data);

    document.getElementById('modelResult').innerText = 'COASTLE says: ' + data.perceptronPrediction;

    return data;

}
