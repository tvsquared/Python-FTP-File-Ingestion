# paramiko parameters
SSH_CLIENT = None
SFTP_CLIENT = None
SSH_OK = False
SFTP_OK = False

# ftp credentials
FTP_HOST = "192.168.15.123"
FTP_PORT = "21"
FTP_USERNAME = "<ftp username>"
FTP_PASSWORD = "<ftp password>"

# s3 parameters
S3_BUCKET = "<s3 bucket name>"

# sftp directory paths
PARENT_DIR_PATH = "<path of directory on FTP server where all the files are present>"
PROCESSED_DIR_PATH = "<path to directory named 'processed' on FTP server>"

# multipart parameters
MB = 1024 ** 2
GB = 1024 ** 3

MULTIPART_THRESHOLD = 100 * MB
MULTIPART_CHUNKSIZE=20 * MB
MAX_CONCURRENCY=10
USER_THREADS=True

LOGGING_CONFIG = { 
    'version': 1,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s]: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',  # Default is stderr
        },
    },
    'loggers': { 
        'python_glue_ingestion_job': {
            'handlers': ['default'],
            'level': 'DEBUG',
        }
    }
}