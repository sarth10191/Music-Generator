# vadi_samvadi = dict()
vadi_samvadi = {   
    "vadi":[["psamvadi","ssamvadi","optional ssamvadi"]],
    "sa":[["pa","ma"],["pa","mat"],["ma","mat"],["ma"," "]],
    "pa":[["sa","re"],["sa","kre"]],
    "ma":[["sa","kni"],["sa","ni"]],
    "ga":[["ni","dha"],["dha","kni"],["dha"," "]],
    "re":[["dha","mat"],["pa","dha"],["pa","kdha"],["dha"," "]],
    "kga":[["kni","kdha"],["kdha","kni"],["kni","dha"],["kdha"," "]],
    "kre":[["kdha","mat"],["kdha"," "]],
    "dha":[["ga","re"],["re"," "],["re","kga"],["ga","kga"]],
    "kdha":[["kga","kre"],["kga","ga"],["kre"," ",],["kre","ga"]]
}

# vadi_anuvadi = dict()
vadi_anuvadi = {
    "sa":[["ga","dha"],["ga","kdha"],["kga","dha"],["kga","kdha"]],
    "pa":[["ga","ni"],["ga","kni"],["kga","kni"],["kga","kni"]],
    "ma":[["re","dha"],["re","kdha"],["kre","dha"],["kre","kdha"]],
    "ga":[["pa","sa"]],
    "re":[["ma","ni"],["ma","kni"],["ni","mat"],["kni","mat"]],
    "kga":[["pa","sa"]],
    "kre":[["ma","ni"],["ma","kkni"]],
    "dha":[["ma","sa"],["sa","mat"]],
    "kdha":[["ma","sa"],["sa","mat"]]
}
vadi_anuanuvadi = dict()
vadi_anuanuvadi = {
    "sa":[["re","ni"],["re","kni"],["kre","ni"],["kre","kni"]],
    "pa":[["ma","dha"],["ma","kdha"],["dha","mat"],["kdha","mat"]],
    "ma":[["pa","ga"],["pa","kga"]],
    "ga":[["ma","re"],["ma","kre"],["re","mat"],["kre","mat"]],
    "kga":[["ma","re"],["ma","kre"],["re","mat"],["kre","mat"]],
    "re":[["sa","ga"],["sa","kga"]],
    "kre":[["ma","ga"],["ma","kga"]],
    # "sa":[["ga","dha"],["ga","kdha"],["kga","dha"],["kga","kdha"]],
    "dha":[["pa","ni"],["pa","kni"],["ni","mat"],["kni","mat"]],
    "kdha":[["pa","ni"],["pa","kni"],["ni","mat"],["kni","mat"]]
}


