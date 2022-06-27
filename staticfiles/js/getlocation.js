// JS function to get user's actual location
const findMyLocation = () => {
    const status = document.querySelector('.find-state');

    const success = (position) => {
        console.log(position)

        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        const geoApiUrl = 'https://api.bigdatacloud.net/data/reverse-geocode-client?latitude=${latitude}&longitude=${longitude}&localityLanguage=en';

        // const geoApiUrl = `https://api.mapbox.com/geocoding/v5/mapbox.places/${longitude},${latitude}.json?access_token=pk.eyJ1Ijoiam9lbGZhaCIsImEiOiJjbDRieXl1MTAwYWJsM2NxdndpamNldW5jIn0.L7f9La3LlUbeiZSyHIuZ_Q`

        fetch(geoApiUrl)
        .then(res => res.json())
        .then(data => {
            console.log(data)
            status.innerHTML = 'You are at <b>' + data.principalSubdivision + '</b>'
        })

        // console.log(geoApiUrl)

        // fetch(geoApiUrl)
        // .then(res => res.json())
        // .then(type => {
        //     console.log(type)
        //     status.innerHTML = data.principalSubdivision
        // })

        // Position Stack
        // $.ajax({
        //     url: 'https://api.positionstack.com/v1/reverse',
        //     data: {
        //       access_key: '6ab7b4a71d1c7b6ca12ee0c5330d01a6',
        //       query: '${latitude},${longitude}',
        //       output: 'xml',
        //       limit: 1
        //     }
        //   }).done(function(data) {
        //     console.log(data);
        //   });

        // Mapbox solution

    }

    const error = () => {
        status.innerHTML = "Allow location first";
    }

    navigator.geolocation.getCurrentPosition(success, error);
}

document.querySelector('.find-state').addEventListener('click', findMyLocation);