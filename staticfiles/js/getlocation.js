// JS function to get user's actual location
const findMyLocation = () => {
    const status = document.querySelector('.find-state');

    const success = (position) => {

        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        const geoApiUrl = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en';

        fetch(geoApiUrl)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            status.innerHTML = data.principalSubdivision
        })

    }

    const error = () => {
        status.innerHTML = "Allow location first";
    }

    navigator.geolocation.getCurrentPosition(success, error);
}

document.querySelector('.find-state').addEventListener('click', findMyLocation);