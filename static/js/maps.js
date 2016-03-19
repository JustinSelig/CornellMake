function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 42.4467, lng: -76.4848},
    zoom: 16,
    streetViewControl: false
  });
  var locations = [
    ['Carpenter Hall', 42.444844, -76.484081, '<div id="content"><h1>Carpenter Hall</h1><img src="../images/carpenter.png" alt="Carpenter" height="150" width="204"><p>This is a marker for the Carpenter makerspace.</p></div>'],
    ['Philips Hall', 42.444577, -76.48205, '<div id="content"><h1>Philips Hall</h1><img src="../images/philips.jpg" alt="Philips" height="150" width="204"><p>This is a marker for the Kennedy makerspace.</p></div>'],
    ['Kennedy Hall', 42.44826, -76.479387, '<div id="content"><h1>Kennedy Hall (Popshop)</h1><img src="../images/kennedy.jpg" alt="Kennedy" height="150" width="204"><p>This is a marker for the Philips makerspace.</p></div>'],
    ['Williard Straight Hall', 42.44674, -76.485558, '<div id="content"><h1>Williard Straight Hall (Slope Studio)</h1><img src="../images/kennedy.jpg" alt="WSH" height="150" width="204"><p>This is a marker for Slope Studio.</p></div>'],
    ['Carl Becker House', 42.448114, -76.489546, '<div id="content"><h1>Carl Becker House</h1><img src="../images/kennedy.jpg" alt="Becker" height="150" width="204"><p>This is a marker for the Becker makerspace.</p></div>']
  ];
  var infowindow = new google.maps.InfoWindow();

  var marker, i;

  for (i = 0; i < locations.length; i++) {
    marker = new google.maps.Marker({
      position: new google.maps.LatLng(locations[i][1], locations[i][2]),
      map: map
    });

    google.maps.event.addListener(marker, 'click', (function(marker, i) {
      return function() {
        infowindow.setContent(locations[i][3]);
        infowindow.open(map, marker);
      }
    })(marker, i));
  }
}   