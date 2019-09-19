# helpers.py

def download_from_cloudstor(cs_path, local_file, force=False):
    from cloudstor import cloudstor
    import os

    teaching_data = cloudstor(url="L93TxcmtLQzcfbk", password='')
    
    if os.path.isfile(local_file) and not force:
        print("File exists ({}) skipping".format(local_file), flush=True)
    else:
        teaching_data.download(cs_path, local_file)

    return


