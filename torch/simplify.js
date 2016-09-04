var fs = require('fs'),
    rawLayers = require('./nn-extended.json'),
    layerNames,
    layers;

// layer attributes
layers = rawLayers.map(layer => {
    return {
        name: layer.name,
        attrs: layer.params.concat(Object.keys(layer.setters))
    };
});

fs.writeFileSync('layers.json', JSON.stringify(layers, null, 4));

// layer names
layerNames = rawLayers.map(layer => layer.name);
fs.writeFileSync('layer-names.json', JSON.stringify(layerNames, null, 4));
