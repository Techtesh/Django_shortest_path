
window.onload =init()
let geodataurl ="./map_project/data.geojson"
console.log(geodataurl) 

function init()
{
    let map = new ol.Map({
        view :new ol.View({
            center:[8113479.934717107,2160693.2659119847],
            zoom :10,maxZoom:20,minZoom:5,
            //projection:"ESPG:4326"
        }),

    /*
        layers :[
            new ol.layer.Tile({
                source: new ol.source.OSM()
        })
        ],
    */

        target : "jsmap"
})

    const openStreetMapStandard=new ol.layer.Tile({ 
        source: new ol.source.OSM(),
        visible:false,
        title:"OSM_Standard"
    })


    const openStreetMapHumanitarian=new ol.layer.Tile({ 
        source:new ol.source.OSM({url: "https://{a-c}.tile.openstreetmap.fr/hot/{z}/{x}/{y}.png"}),
        visible:true,
        title:"OSM_Humanitarian"
    })

    const StamenTerrain=new ol.layer.Tile({ 
        source:new ol.source.XYZ({url:"http://tile.stamen.com/terrain/{z}/{x}/{y}.jpg"}),
        visible:true,
        title:"Stamen_Terrain"
    })
    

    //one layer allowed
    //map.addLayer(openStreetMapHumanitarian);
    //using layer group
    const baseLayerGroup =new ol.layer.Group({
        layers:[openStreetMapHumanitarian,openStreetMapStandard,StamenTerrain]
    })
    map.addLayer(baseLayerGroup)

    //base layer switcher
    let baseLayer=document.querySelectorAll(".sidebar >input[type=radio]")
    
    for(let base of baseLayer)
    {
        console.log(base);
        base.addEventListener("change",() => {let select=(base.value);
            baseLayerGroup.getLayers().forEach(function(element,index,array){
                let bltitle=(element.get("title"))
                element.setVisible(bltitle===select);
            })
        })
    }
    const FillStyle = new ol.style.Fill({color :[84,118,255,1 ]})
    const StrokeStyle= new ol.style.Stroke({
        color:[46,45,45,1],
        width:2
    })
    const CircleStyle =new ol.style.Circle({
        fill : new ol.style.Fill({color:[249,49,5,1]}),
        radius :7,
        stroke :StrokeStyle
    })
    

    //Adding Vector Layers
    
    
    const RouteGeoJson = new ol.layer.VectorImage({
        source : new ol.source.Vector({
            url://geodataurl,
            "./map_project/data.geojson", 
            //"./Geodata/map.geojson",
            format : new ol.format.GeoJSON()
        }), 
        visible:true,
        title:"route",
        style: new ol.style.Style({
            fill:FillStyle,       //polygon
            stroke:StrokeStyle,   //lines
            image :CircleStyle,   //points
            

        })
              

    })
    map.addLayer(RouteGeoJson)
    map.on("click",function(e){
        console.log(e.coordinate)
    })
}

