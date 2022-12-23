import datetime, json, logging, os, pprint, sys
from collections import OrderedDict

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
# model = whisper.load_model( 'base' )      # averages about 2 minutes on this file
# model = whisper.load_model( 'medium' )    # averages about 14 minute on this file
model = whisper.load_model( 'large' )

## transcribe quicktime .mov file -----------------------------------
audio_file_path = settings.AUDIO_FILE_PATH
log.debug( f'audio_file_path, ``{audio_file_path}``' )
result = model.transcribe( audio_file_path )

## extract segment data ---------------------------------------------
segments = []
for segment in result.get( 'segments', [] ):
    d = OrderedDict()
    d['start'] = segment.get( 'start', '' )    # type: ignore
    d['end'] = segment.get( 'end', '' )        # type: ignore
    d['text'] = segment.get( 'text', '' )      # type: ignore
    segments.append( d )
log.debug( f'segments, ``{pprint.pformat(segments)}``' )

## ouput data -------------------------------------------------------
datestamp = datetime.datetime.now().isoformat().replace( ':', '-' ).replace( '.', '-' )
segments_jsn = json.dumps( segments, indent=2 )
segments_jsn_path = f'{settings.TRANSCRIPTION_OUTPUT_DIR_PATH}/segments_{datestamp}.json'
log.debug( f'segments_jsn_path, ``{segments_jsn_path}``' )
with open( segments_jsn_path, 'w+' ) as f:
    f.write( segments_jsn )
full_result_jsn: str = json.dumps( result, indent=2 )
full_result_jsn_path = f'{settings.TRANSCRIPTION_OUTPUT_DIR_PATH}/full_result_{datestamp}.json'
log.debug( f'full_result_jsn_path, ``{full_result_jsn_path}``' )
with open( full_result_jsn_path, 'w+' ) as f:
    f.write( full_result_jsn )
transcription: str = result.get( 'text', '' )  # type: ignore # type: ignore
output_file_path = f'{settings.TRANSCRIPTION_OUTPUT_DIR_PATH}/transcription_{datestamp}.txt'
log.debug( f'output_file_path, ``{output_file_path}``' )
with open( output_file_path, 'w+' ) as f:
    f.write( transcription )
