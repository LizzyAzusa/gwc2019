var ourLoc
var map
var view

function init(){
  //Initialize stuff
  ourLoc = ol.proj.fromLonLat([40.7535,73.9768]);
  view = new ol.View({
    center: ourLoc,
    zoom:6
  })
  map = new ol.Map({
    target:'map',
    layers:[
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating:true,
    view:view
  });
}

window.onload = init;
