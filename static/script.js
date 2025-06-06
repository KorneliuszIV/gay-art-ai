function updateRatingValue(val, num) {
    document.getElementById(`ratingValue${num}`).textContent = val;
}

// Initialize with the default value
document.addEventListener('DOMContentLoaded', init);

const API_HOSTNAME = 'https://gay-art-ai.onrender.com';
async function getData() {
    const data = await fetch(API_HOSTNAME + `/level_data`)
    const j = await data.text()
    return j
}


async function init(){
    const sliders = document.getElementsByClassName('slider');
    for (let slider of sliders){
        document.getElementById('ratingValue').textContent = slider.value;
    }
    data = await getData();
    x_values = [1,2,3,4,5,6,7,8,9,10]
    y_values = []
    for (let value of data.slice(0, -1)){
        y_values.push(value)
    }
    console.log(y_values)
    const myChart = new Chart("canvas", {
        type: "line",
        data: {
            labels: x_values,
            datasets: [{
                backgroundColor:"rgba(0,0,255,1.0)",
                borderColor: "rgba(0,0,255,0.1)",
                fill: false,
                data: y_values
            }]
        },
        options: {
            legend: {display: false},
            scales: {
              yAxes: [{ticks: {min: 0, max:10}}],
            }
          }
      });   
};

