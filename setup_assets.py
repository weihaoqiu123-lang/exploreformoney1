from pathlib import Path
from urllib.request import urlopen
import io, tarfile
root = Path(__file__).resolve().parent / 'dist'
root.mkdir(exist_ok=True)
print('正在下载 MediaPipe 识别组件…')
with urlopen('https://registry.npmjs.org/@mediapipe/tasks-vision/-/tasks-vision-0.10.21.tgz', timeout=120) as response:
    archive = response.read()
with tarfile.open(fileobj=io.BytesIO(archive), mode='r:gz') as bundle:
    for name in ['vision_bundle.mjs', 'wasm/vision_wasm_internal.js', 'wasm/vision_wasm_internal.wasm', 'wasm/vision_wasm_nosimd_internal.js', 'wasm/vision_wasm_nosimd_internal.wasm']:
        member = bundle.extractfile('package/' + name)
        target = root / name
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(member.read())
print('正在下载人脸识别模型…')
with urlopen('https://storage.googleapis.com/mediapipe-models/face_landmarker/face_landmarker/float16/1/face_landmarker.task', timeout=120) as response:
    (root / 'face_landmarker.task').write_bytes(response.read())
print('完成。运行 python -m http.server 8000 --directory dist')

