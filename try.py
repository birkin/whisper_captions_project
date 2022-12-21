import datetime, logging, os, pprint, sys

import whisper
from config import settings

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)
log.debug( 'logging ready' )

## load model -------------------------------------------------------
model = whisper.load_model( 'base' )

## transcribe quicktime .mov file -----------------------------------
audio_file_path = settings.AUDIO_FILE_PATH
log.debug( f'audio_file_path, ``{audio_file_path}``' )
result = model.transcribe( audio_file_path )
transcription: str = result.get( 'text', '' )

## ouput transcription-text -----------------------------------------
output_file_path = f'{settings.TRANSCRIPTION_OUTPUT_DIR_PATH}/transcription_{str(datetime.datetime.now())}.txt'
log.debug( f'output_file_path, ``{output_file_path}``' )
with open( output_file_path, 'w+' ) as f:
    f.write( transcription )
