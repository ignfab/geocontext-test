import os

TOOL_GEOCODE = "geocode"
TOOL_ALTITUDE = "altitude"
TOOL_ADMINEXPRESS = "adminexpress"
TOOL_CADASTRE = "cadastre"
TOOL_URBANISME = "urbanisme"
TOOL_ASSIETTE_SUP = "assiette_sup"

# TODO : handle GEOCONTEXT_DEV=1 to switch 
# to the next version naming

GEOCONTEXT_DEV=os.getenv("GEOCONTEXT_DEV","0") == "1"

TOOL_GPF_SEARCH_TYPES      = "gpf_search_types" if GEOCONTEXT_DEV else "gpf_wfs_search_types"
TOOL_GPF_DESCRIBE_TYPE     = "gpf_describe_type" if GEOCONTEXT_DEV else "gpf_wfs_describe_type"
TOOL_GPF_GET_FEATURES      = "gpf_get_features" if GEOCONTEXT_DEV else "gpf_wfs_get_features"
TOOL_GPF_GET_FEATURE_BY_ID = "gpf_get_feature_by_id" if GEOCONTEXT_DEV else "gpf_wfs_get_feature_by_id"
TOOL_GPF_COUNT_FEATURES    = "gpf_count_features" # GEOCONTEXT_DEV only

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

if GEOCONTEXT_DEV:
    EXPECTED_TOOLS.append(TOOL_GPF_COUNT_FEATURES)
