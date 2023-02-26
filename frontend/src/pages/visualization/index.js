import React,{useState,useEffect} from 'react'
import DeckGL from 'deck.gl';
import { TripsLayer } from '@deck.gl/geo-layers';
import { IconLayer } from '@deck.gl/layers';
import {Map} from 'react-map-gl';

import data from '../../data/routes.json';
import trip_data from '../../data/trips.json';


const { assign } = Object;

const MAPBOX_TOKEN = `pk.eyJ1IjoidmFpc2hha2ciLCJhIjoiY2xkdjgxYmFsMGQ5MzNxcGN3ZDQ0bDc0ZSJ9.WkFIdi_bydsc8SFnh6_bTA`; // eslint-disable-line
const ICON_MAPPING = {
    marker: {x: 0, y: 0, width: 128, height: 128, mask: true}
  };
  let newData=[]
  data.map(o=>{
      newData.push({'name':o.stop_name,'coordinates':[o.stop_lon,o.stop_lat]})
  })
  const ROUTES= newData;
const mapStyle = 'mapbox://styles/vaishakg/cldxcgmug004m01tdo0w91fym';
const initialStyle = {
    position: "relative",
    width: "100%",
    height: "550px",
    border: "1px solid black",
  };

  const initialViewState = {
    longitude: -84.51542,
    latitude: 39.173388,
    zoom: 11.9,
    minZoom: 5,
    maxZoom: 15,
    pitch: 45,
    bearing: 0,
  };


const BLUE = [23, 184, 190];
const RED = [253, 128, 93];


const Visualization = () => {
    const [style, setStyle] = useState(assign({}, initialStyle));
    const [viewState, setViewState] = useState(initialViewState);
    const step = .1;
    const intervalMS = 10;
    const loopLength = 2400;
  
  
    const intensity = 1;
    const threshold = 0.03;
    const radiusPixels = 30;
    
    const [time, setTime] = useState(0);
    
    useEffect(() => {
      const interval = setInterval(() => {
          
        setTime(t => (t + step) % loopLength);
      }, intervalMS);
    
      return () => clearInterval(interval);
    }, []);
    const layers = [
      new TripsLayer({
        id: 'trips',
        data: trip_data,
        getPath: d =>d.path,
        getTimestamps: d => d.timestamps,
        getColor: d => (d.vendor === 0 ? RED : BLUE),
        opacity: 0.5,
        widthMinPixels: 3,
        rounded: true,
        trailLength: 10,
        currentTime: time,
      }),
        new IconLayer({
          id:'icons',
          data:ROUTES,
          pickable: true,
          iconAtlas: 'https://raw.githubusercontent.com/visgl/deck.gl-data/master/website/icon-atlas.png',
          iconMapping: ICON_MAPPING,
          getIcon: d => 'marker',
          sizeScale: 6,
          getPosition: d => d.coordinates,
          getSize: d => 2,
          getColor: d => [Math.sqrt(d.exits), 140, 0]
        }),
      
        // new HeatmapLayer({
        //   heat_data,
        //   id: 'heatmp-layer',
        //   pickable: false,
        //   getPosition: d =>{ console.log(d);return [d[0], d[1]]},
        //   getWeight: d => d[2],
        //   radiusPixels,
        //   intensity,
        //   threshold
        // })
    ];
  
    return (
      <>
        <DeckGL
          controller
          viewState={viewState}
          layers={layers}
          style={style}
          getTooltip={({object}) => object && `${object.name}\n`} 
          onViewStateChange={
            (nextViewState) => {
              setViewState(nextViewState.viewState);
            }
          }
        >
  
            <Map
            reuseMaps
            mapStyle={mapStyle}
            preventStyleDiffing={true}
            mapboxAccessToken={MAPBOX_TOKEN}
            />
        </DeckGL>
        </>
    )
  }

export default Visualization