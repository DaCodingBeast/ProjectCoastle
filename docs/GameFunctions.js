async function request(apiEndpoint) {
    try {
        const response = await fetch(`/api/${apiEndpoint}`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
        });

        const data = await response.json();

    } catch (error) {
        console.error('Error starting game:', error);
    }
    return data;

}


async function startGame() {

    data = await request('meteo');
    console.log(data);
    return data['api/meteo/'];

}



async function getLocation() {

    data = await request('location');
    console.log(data);
    return data;

}

async function getPerceptronPrediction() {

    data = await request('perceptronGuess');
    console.log(data);
    return data;

}



let userGuess = null;

let cityData = {
    population: 1000000,
    elevation: 15,
    region: "West Coast"
};

let cityCoords = [34.0522, -118.2437];

function setGuessAndRun(guess) {
    userGuess = guess;
    document.getElementById('guess-display').innerText = guess;
    runModel();
}

async function runModel() {
    try {
        const response = await fetch('/test', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ userGuess, cityData, cityCoords })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();

        document.getElementById('modelResult').innerText = 'COASTLE says: ' + data.modelGuess;

        if (data.coords && data.coords.length === 2) {
            document.getElementById('map').innerHTML = `
            <iframe
              src="https://maps.google.com/maps?q=${data.coords[0]},${data.coords[1]}&z=10&output=embed"
              allowfullscreen>
            </iframe>
          `;
        }
    } catch (error) {
        console.error('Error running model:', error);
        document.getElementById('modelResult').innerText = 'Error getting prediction.';
    }
}

window.onload = () => {
    const list = document.getElementById('cityDataList');
    for (const [key, value] of Object.entries(cityData)) {
        const li = document.createElement('li');
        li.textContent = `${key}: ${value}`;
        list.appendChild(li);
    }
};

function openMap() {
    if (cityCoords && cityCoords.length === 2) {
        const [lat, lng] = cityCoords;
        document.getElementById('map').innerHTML = `
          <iframe
            src="https://maps.google.com/maps?q=${lat},${lng}&z=10&output=embed"
            allowfullscreen>
          </iframe>
        `;
    }
}