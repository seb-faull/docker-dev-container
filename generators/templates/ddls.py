RAW_TEMP_DDL = """
CREATE TRANSIENT TABLE IF NOT EXISTS {raw_database}.{raw_schema}.TEMP_{table_name}
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
);"""

RAW_DDL = """
CREATE TABLE IF NOT EXISTS {raw_database}.{raw_schema}.{table_name}
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
) ;"""

CURATED_DDL = """
CREATE TABLE IF NOT EXISTS {curated_database}.{curated_schema}.{table_name}
(
    ADT_INSERTED_AT TIMESTAMP_NTZ(9),
    ADT_UPDATED_AT TIMESTAMP_NTZ(9),
    ADT_BATCH_DATE DATE,
    ADT_STAGE_FILE_NAME VARCHAR(1024),
    ADT_STAGE_FILE_ROW NUMBER(38,0),
    ADT_METADATA VARIANT,
    ROW_START_AT TIMESTAMP_NTZ,
    ROW_END_AT TIMESTAMP_NTZ,
    ROW_IS_CURRENT CHAR(1),
    TRACKING_HASH VARCHAR,{multi_key}{multi_updated_date}
{columns}
) ;"""
