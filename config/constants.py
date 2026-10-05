import os

TOOL_GEOCODE = "geocode"
TOOL_ALTITUDE = "altitude"
TOOL_ADMINEXPRESS = "adminexpress"
TOOL_CADASTRE = "cadastre"
TOOL_URBANISME = "urbanisme"
TOOL_ASSIETTE_SUP = "assiette_sup"

# Allows to test the futur version (main)
GEOCONTEXT_DEV=os.getenv("GEOCONTEXT_DEV","0") == "1"

TOOL_GPF_SEARCH_TYPES      = "gpf_search_types" if GEOCONTEXT_DEV else "gpf_wfs_search_types"
TOOL_GPF_DESCRIBE_TYPE     = "gpf_describe_type" if GEOCONTEXT_DEV else "gpf_wfs_describe_type"
TOOL_GPF_GET_FEATURES      = "gpf_get_features" if GEOCONTEXT_DEV else "gpf_wfs_get_features"
TOOL_GPF_GET_FEATURE_BY_ID = "gpf_get_feature_by_id" if GEOCONTEXT_DEV else "gpf_wfs_get_feature_by_id"

# GEOCONTEXT_DEV (0.10.x) only
TOOL_GPF_COUNT_FEATURES          = "gpf_count_features"
TOOL_GPF_GET_FEATURES_LAYER      = "gpf_get_features_layer"
TOOL_GPF_GET_FEATURE_BY_ID_LAYER = "gpf_get_feature_by_id_layer"
TOOL_DISTANCE                    = "distance"


EXPECTED_TOOLS = [
    TOOL_GEOCODE,
    TOOL_ALTITUDE,
    TOOL_ADMINEXPRESS,
    TOOL_CADASTRE,
    TOOL_URBANISME,
    TOOL_ASSIETTE_SUP,
    TOOL_GPF_SEARCH_TYPES,
    TOOL_GPF_DESCRIBE_TYPE,
    TOOL_GPF_GET_FEATURES,
    TOOL_GPF_GET_FEATURE_BY_ID,
]

# GEOCONTEXT_DEV (0.10.x) only
if GEOCONTEXT_DEV:
    EXPECTED_TOOLS.append(TOOL_GPF_COUNT_FEATURES)
    EXPECTED_TOOLS.append(TOOL_GPF_GET_FEATURES_LAYER)
    EXPECTED_TOOLS.append(TOOL_GPF_GET_FEATURE_BY_ID_LAYER)
    EXPECTED_TOOLS.append(TOOL_DISTANCE)
