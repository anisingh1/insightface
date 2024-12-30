
import os
import os.path as osp
import zipfile
from .download import download_file

BASE_REPO_URL = 'https://github.com/deepinsight/insightface/releases/download/v0.7'

def download(name, force=False, root='~/.insightface'):
    _root = os.path.expanduser(root)
    dir_path = os.path.join(_root, name)
    if osp.exists(dir_path) and not force:
        return dir_path
    print('download_path:', dir_path)
    zip_file_path = os.path.join(_root, name + '.zip')
    model_url = "%s/%s.zip"%(BASE_REPO_URL, name)
    download_file(model_url,
             path=zip_file_path,
             overwrite=True)
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    with zipfile.ZipFile(zip_file_path) as zf:
        zf.extractall(dir_path)
    #os.remove(zip_file_path)
    return dir_path

def ensure_available(name, root='~/.insightface'):
    return download(name, force=False, root=root)

def download_onnx(model_file, force=False, root='~/.insightface', download_zip=False):
    _root = os.path.expanduser(root)
    new_model_file = osp.join(_root, model_file)
    if osp.exists(new_model_file) and not force:
        return new_model_file
    if not osp.exists(_root):
        os.makedirs(_root)
    print('download_path:', new_model_file)
    if not download_zip:
        model_url = "%s/%s"%(BASE_REPO_URL, model_file)
        download_file(model_url,
                 path=new_model_file,
                 overwrite=True)
    else:
        model_url = "%s/%s.zip"%(BASE_REPO_URL, model_file)
        zip_file_path = new_model_file+".zip"
        download_file(model_url,
                 path=zip_file_path,
                 overwrite=True)
        with zipfile.ZipFile(zip_file_path) as zf:
            zf.extractall(_root)
        return new_model_file
