// # Plotly covid 

// Populate dropdown menu
// Populate dropdown menu
d3.json("merged_state_data.json").then(data => {
        
    var data = data;
    console.log(data);
    
    // Isolate patient IDs to add to dropdown
    var stateIDs = data.map(x => x.state);
    console.log(stateIDs);

    // Append options to the dropdownmenu with patientIDs
    for (var i = 0; i < stateIDs.length; i++) {
        dropdownMenu = d3.select("#selState");
        dropdownMenu.append("option").text(stateIDs[i]);
    };
});


// // Event handler
function optionChanged (stateSel) {
    console.log(stateSel);
    plot(stateSel)
}


function plot (stateSel) {

    // Tracking when the function changes
    console.log(`Selection:${stateSel}`);


    // Read data in json and create variables for data and patientIDs
    // Creating a promise to work with data - so all other manipulation must be within this function
    d3.json("states.json").then(data => {

        var recentData = data.filter(x => x.date === "2020-04-06")

        var recentSelectionData = recentData.filter(x => x.state === stateSel);
        console.log(recentSelectionData);


        // Select HTML element
        var demographicData = d3.select('#sample-metadata');

        // Clear demographic data
        demographicData.html('');
  
        // Fill demographic data for metadata section
        demographicData.append('p').text(`State: ${recentSelectionData[0].state}`);
        demographicData.append('p').text(`Total Cases: ${recentSelectionData[0].cases}`);
        demographicData.append('p').text(`Total Deaths: ${recentSelectionData[0].deaths}`);


        // Line graph section

        var selData = data.filter(x => x.state === stateSel);

        var selDates = selData.map(x => x.date);
        console.log(selDates);

        var selCases = selData.map(x => x.cases);
        console.log(selCases);

        var selDeaths = selData.map(x => x.deaths);

        var lineData = [{
            x: selDates,
            y: selCases,
            type: "scatter",
            mode: "lines",
            line: {
              color: "#FE6625"
            }
        },
        {
            x: selDates,
            y: selDeaths,
            type: "scatter",
            mode: "lines",
            line: {
              color: "red"
            }
        }]

        var lineLayout = {
            title: `${stateSel}`, 
            yaxis: {title: "Total Cases"},
            height: 300,
            width: 1000
        };

        Plotly.newPlot("bar", lineData, lineLayout);

    }) 
}


function plotMap() {
    d3.json("merged_state_data.json").then(data => {

        var allStateLat = data.map(x => x.lat);
        var allStateLon = data.map(x => x.lon);
        var allStateCases = data.map(x => x.cases);
        var allStateNames = data.map(x => x.state);

        var data = [{
            type: 'cloropleth',
            locationmode: 'USA-states',
            lat: allStateLat,
            lon: allStateLon,
            z: allStateCases,
            text: allStateNames,
            autocolorscale: true    
        }];

        var layout = {
            title: '2014 US Popultaion by State',
                geo:{
                    scope: 'usa',
                    countrycolor: 'rgb(255, 255, 255)',
                    showland: true,
                    landcolor: 'rgb(217, 217, 217)',
                    showlakes: true,
                    lakecolor: 'rgb(255, 255, 255)',
                    subunitcolor: 'rgb(255, 255, 255)',
                    lonaxis: {},
                    lataxis: {}
                }
            };
            Plotly.newPlot("map", data, layout, {showLink: false});
    })
}

// Default plot: Colorado
plot ('Alabama')
plotMap ()

// Create a map object


