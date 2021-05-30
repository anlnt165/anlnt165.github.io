(functuon (PV) {
    "use strict";

    function symbolVis() {};
    PV.deriveVisualizationFromBase(symbolVis);

    var definition = {
        typename: "koalabear"
        visObjectType: symbolVis,
        datasourceBehavior: PV.Extensibility.Enums.DatasoureBehaviors.Single,
        getDefaultConfig: function(){
            return {
                Height: 150,
                Width: 150
            }
        }
    }

    symbolVis.prototype.init = function(scope, elem) { };

    PV.symbolCatalog.register(definition);
})(window.PIVisialization);