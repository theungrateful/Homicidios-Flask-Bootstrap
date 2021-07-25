	    var map = L.map('map').setView([-26.8198, -65.2169], 13);

        // Capas base
        var osmLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
        attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap<\/a> contributors'
        }).addTo(map);
        
        // GeoJSON from API Rest
      
       let miSelect=2020; 
        
     
      

        async function fetchHomicidiosJSON() {
        const response = await fetch('https://python-api-homicidios.herokuapp.com/');
        const homicidios = await response.json();
        return homicidios;
        }

        fetchHomicidiosJSON().then(homicidios => {
            let layer1 = L.geoJson(homicidios, {filter: function(feature, layer) {								
								 if(miSelect != 0)		
									return (feature.properties.ANIO_NUM == miSelect );
								else
									return true;
							    }
                    });
        layer1.addTo(map);
            });