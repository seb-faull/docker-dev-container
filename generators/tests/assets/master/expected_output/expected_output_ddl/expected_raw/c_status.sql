
CREATE TABLE IF NOT EXISTS RAW_ALLIANT_PPL_PROD_LAKE.DBO.C_STATUS
(
    ADT_INSERT_AUDIT_ID     NUMBER(38,0),
    ADT_INSERT_TIME         TIMESTAMP_NTZ(9),
    ADT_UPDATE_AUDIT_ID     NUMBER(38,0),
    ADT_UPDATE_TIME         TIMESTAMP_NTZ(9),
    ADT_BATCH_DATE          DATE,
    ADT_STAGE_FILE_NAME     VARCHAR(1024),
    ADT_STAGE_FILE_ROW      NUMBER(38,0),
    ADT_METADATA            VARIANT,
    ADT_BOOKMARK_COLUMN     VARCHAR(255),
    ADT_BOOKMARK_TYPE       VARCHAR(20),
    ADT_BOOKMARK_VALUE      VARCHAR(100),
    FILECONTENTS            VARIANT
) ;
