var fs = require('fs'),
    rawLayers = require('./nn-extended.json'),
    layerNames,
    layers;

// layer attributes
layers = rawLayers
    .filter(layer => layer.type === 'Transfer')
    .map(layer => layer.name);

fs.writeFileSync('layers.json', JSON.stringify(layers, null, 4));

// layer names
layerNames = rawLayers.map(layer => layer.name);
fs.writeFileSync('transfer.json', JSON.stringify(layerNames, null, 4));
