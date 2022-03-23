import pathlib
from typing import List

# from typing import List


def read_input_file_paths(
        input_root_path: pathlib.PosixPath,
        extension: str):
    """最下層に存在する指定した拡張子のファイルを全て取得する
    Args:
        input_root_path (pathlib.PosixPath): ディレクトリのパス
        extension (str): 拡張子

    Returns:
        all_path_list (List[pathlib.PosixPath]): 取得したファイルパスのリスト
    """
    all_path_list = list(input_root_path.glob(f'**/*.{extension}'))
    return all_path_list


def generate_output_name_with_work_id(
        work_id: int,
        file_stem: str,
        extension: str = ''):
    """IDを付与したファイル名(or ディレクトリ名) を生成する
       ディレクトリ名は生成するときはextensionは指定しない
    Args:
        work_id (int): ワークID
        file_stem (str): 拡張子なしのファイル名
        extension (str, optional): ファイルに付与したい拡張子. Defaults to ''. (pdf, json, xlsx ...)

    Returns:
        output_name (str): IDを付与したファイル名(or ディレクトリ名)
    """
    work_id = str(work_id)
    if extension:
        output_name = f"[#{work_id}]_{file_stem}.{extension}"
    else:
        output_name = f"[#{work_id}]_{file_stem}"
    return output_name


def extract_original_file_name(file_name: str):
    """ワークIDを除いた元のファイル名を抽出する（ワークIDがある場合）

    Args:
        file_name (str): ファイル名

    Returns:
        original_file_name(str): 元のファイル名
    """
    original_file_name = re.sub(r'^[#[0-9]+]_', "", file_name)
    return original_file_name
