import logging, os, pprint, sys

log = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] %(levelname)s [%(module)s-%(funcName)s()::%(lineno)d] %(message)s',
    datefmt='%d/%b/%Y %H:%M:%S' )
log = logging.getLogger(__name__)

log.debug( f'sys.path initially, ``{pprint.pformat(sys.path)}``' )

PROJECT_CODE_DIR = os.environ['WHSPR__PROJECT_CODE_DIR_PATH']
## add project-code parent dir to sys.path
sys.path.append( os.path.dirname(PROJECT_CODE_DIR) )
log.debug( f'sys.path now, ``{pprint.pformat(sys.path)}``' )

import whisper
from whisper_captions_project.config import settings

model = whisper.load_model( "base" )

## transcribe quicktime .mov file -----------------------------------
result = model.transcribe( settings.AUDIO_FILE_PATH, format='mov' )

print(result["text"])