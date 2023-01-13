import sys
import time
from pathlib import Path

VERSION = "1.0"
AUTHOR = "Kotaro Yamashita (yamashita.ko@mitsuimiike.co.jp)"

dwg_versions = {
    "AC1015": "DWG AutoCAD 2000",
    "AC1018": "DWG AutoCAD 2004",
    "AC1021": "DWG AutoCAD 2007",
    "AC1024": "DWG AutoCAD 2010",
    "AC1027": "DWG AutoCAD 2013",
    "AC1032": "DWG AutoCAD 2018",
}

if len(sys.argv) == 2:
    if sys.argv[1] == "--version":
        print(f"\ncheck_dwg_version {VERSION}\nAuthor: {AUTHOR}\n")
        sys.exit()

while True:
    raw_target_folder_path = input("チェック対象のDWGファイルを保管しているフォルダのパスを入力してください。")

    match raw_target_folder_path:
        case "":
            continue
        case "exit":
            sys.exit()
        case _:
            break

if raw_target_folder_path[0] == '"' and raw_target_folder_path[-1] == '"':
    target_folder_path = Path(raw_target_folder_path[1:-1])
else:
    target_folder_path = Path(raw_target_folder_path)

if not target_folder_path.exists():
    print("指定されたフォルダが存在しません。プログラムを終了します。")
    time.sleep(3)
    sys.exit()

for p in target_folder_path.iterdir():
    if p.match("*.dwg"):
        with p.open(mode="r", encoding="cp932", errors="ignore") as f:
            t = f.readline()
            version_code = t[:6]
            if version_code in dwg_versions.keys():
                version = dwg_versions[version_code]
            else:
                version = "unkown"

        print(f"{p} \t{version}")


input("何かキーを押してください。")
