# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['present.py'],
             pathex=['C:\\present_v2'],
             binaries=[],
             datas=[
(r'sprites\beggar_1.png', 'sprites'),
(r'sprites\beggar_1_hurt.png', 'sprites'),
(r'sprites\beggar_2.png', 'sprites'),
(r'sprites\beggar_2_hurt.png', 'sprites'),
(r'sprites\dad.png', 'sprites'),
(r'sprites\dad_hurt.png', 'sprites'),
(r'sprites\dad_run.png', 'sprites'),
(r'sprites\explosion_1.png', 'sprites'),
(r'sprites\explosion_2.png', 'sprites'),
(r'sprites\explosion_3.png', 'sprites'),
(r'sprites\explosion_4.png', 'sprites'),
(r'sprites\explosion_5.png', 'sprites'),
(r'sprites\explosion_6.png', 'sprites'),
(r'sprites\explosion_7.png', 'sprites'),
(r'sprites\explosion_8.png', 'sprites'),
(r'sprites\explosion_9.png', 'sprites'),
(r'sprites\explosion_10.png', 'sprites'),
(r'sprites\explosion_11.png', 'sprites'),
(r'sprites\explosion_12.png', 'sprites'),
(r'sprites\f_apple.png', 'sprites'),
(r'sprites\f_applepart.png', 'sprites'),
(r'sprites\f_cola.png', 'sprites'),
(r'sprites\f_dumplings.png', 'sprites'),
(r'sprites\f_schnizel.png', 'sprites'),
(r'sprites\fh_bigmac.png', 'sprites'),
(r'sprites\game_over.png', 'sprites'),
(r'sprites\h_book.png', 'sprites'),
(r'sprites\homeless_1.png', 'sprites'),
(r'sprites\homeless_1_hurt.png', 'sprites'),
(r'sprites\homeless_2.png', 'sprites'),
(r'sprites\homeless_2_hurt.png', 'sprites'),
(r'sprites\homeless_super.png', 'sprites'),
(r'sprites\homeless_super_hurt.png', 'sprites'),
(r'sprites\level1_fone.png', 'sprites'),
(r'sprites\menu_dad.png', 'sprites'),
(r'sprites\menu_dad_waving.png', 'sprites'),
(r'sprites\menu_fone.png', 'sprites'),
(r'sprites\menu_start_button.png', 'sprites'),
(r'sprites\menu_start_button_clicked.png', 'sprites'),
(r'sprites\menu_start_button_pushed.png', 'sprites'),
(r'sprites\road_repair.png', 'sprites'),
(r'sprites\road_repair_sign.png', 'sprites'),
(r'sprites\road_worker_1.png', 'sprites'),
(r'sprites\road_worker_1_hurt.png', 'sprites'),
(r'sprites\road_worker_2.png', 'sprites'),
(r'sprites\road_worker_2_hurt.png', 'sprites'),
(r'sprites\road_worker_3.png', 'sprites'),
(r'sprites\road_worker_3_hurt.png', 'sprites'),
(r'sprites\road_worker_4.png', 'sprites'),
(r'sprites\road_worker_4_hurt.png', 'sprites'),
(r'sprites\road_worker_talking.png', 'sprites'),
(r'sprites\spikes.png', 'sprites'),
(r'sprites\state_lines.png', 'sprites'),
(r'sprites\story_fone.png', 'sprites'),
(r'sprites\story_start_button.png', 'sprites'),
(r'sprites\story_start_button_clicked.png', 'sprites'),
(r'sprites\story_start_button_pushed.png', 'sprites'),
(r'sprites\trash.png', 'sprites'),
(r'sprites\trashcan.png', 'sprites'),
(r'sprites\trashcan_open.png', 'sprites'),
(r'sprites\w_bat.png', 'sprites'),
(r'sprites\w_bottle.png', 'sprites'),
(r'sprites\w_brassknuckles.png', 'sprites'),
(r'sprites\w_cup.png', 'sprites'),
(r'sprites\w_fryingpan.png', 'sprites'),
(r'sprites\w_hammer.png', 'sprites'),
(r'sprites\w_pencil.png', 'sprites'),
(r'sprites\w_pocketknife.png', 'sprites'),
(r'sprites\w_russianflag.png', 'sprites'),
(r'sprites\w_superhammer.png', 'sprites')
		],
             hiddenimports=['sys', 'os', 'random', 'pygame'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='present',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False , icon='icon.ico')
