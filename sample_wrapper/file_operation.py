import pathlib
from typing import List

# from typing import List


def read_input_file_paths(
        input_root_path: pathlib.PosixPath,
        extension: str) -> List:
    """最下層に存在する指定した拡張子のファイルを全て取得する
    Args:
        input_root_path (pathlib.PosixPath): ディレクトリのパス
        extension (str): 拡張子

    Returns:
        all_path_list (List[pathlib.PosixPath]): 取得したファイルパスのリスト
    """
    all_path_list = list(input_root_path.glob(f'**/*.{extension}'))
    return all_path_list
