# -*- mode: python -*-

block_cipher = None


a = Analysis(['encrypt_hlbt.py'],
             pathex=['/media/atishya/New Volume/Summer project/Side work/Untitled Folder/py_img_stegano'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='encrypt_hlbt',
          debug=False,
          strip=False,
          upx=True,
          console=True )