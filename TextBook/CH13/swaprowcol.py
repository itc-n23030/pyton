import pandas as pd


def read_excel_file(file_path):
    """
    Excelファイルからデータフレームとしてデータを読み込みます。

    :param file_path: Excelファイルのパス
    :return: データフレーム
    """
    df = pd.read_excel(file_path, sheet_name='Sheet1')
    return df


def transpose_data(df):
    """
    データフレームのデータを転置します。
    :param df: データフレーム
    :return: 転置されたデータフレーム
    """
    transposed_df = df.transpose()  # 転置したデータフレームを新しい変数に割り当てる
    return transposed_df


def write_excel_file(df, file_path):
    """
    データフレームをExcelファイルに書き込みます。
    :param df: データフレーム
    :param file_path: Excelファイルのパス
    :return:
    """
    df.to_excel(file_path, index=True, header=False)


if __name__ == '__main__':
    excel_file_path = 'base.xlsx'
    df = read_excel_file(excel_file_path)
    transposed_df = transpose_data(df)  # 転置したデータフレームを新しい変数に割り当てる
    write_excel_file(transposed_df, 'transpose.xlsx')

    print('完了')
    