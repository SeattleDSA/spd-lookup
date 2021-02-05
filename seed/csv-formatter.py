import pandas as pd
in_df = pd.read_csv('name_of_file')

def split_name(df, var):
    sub_df = df[var].str.split('\\s+', expand=True)
    result = []
    for _, row in sub_df.iterrows():
        info = {'first_name': '', 'middle_name': '', 'last_name': ''}
        n = row.count()
        if n == 0:
            pass
        elif n == 1:
            info['last_name'] = row.iloc[0]
        elif n == 2:
            info['last_name'], info['first_name'] = row.iloc[:2]
        else:
            info['first_name'] = row.iloc[1].strip().strip(',')
            info['last_name'] = row.iloc[0].strip().strip(',')
            info['middle_name'] = ' '.join([(string or '') for string in row.iloc[2:-1]]).strip().strip('.')
        result.append(info)
    return pd.DataFrame(result, index=df.index)


name_split_df = split_name(in_df, 'Name')
out_df = in_df.join(name_split_df, how='outer')

column_names = {
    'Name': 'full_name',
    'Badge_Num': 'badge_number',
    'Title_Description': 'title',
    'Unit': 'unit',
    'Unit_Description': 'unit_Description'
}
out_df.rename(columns=column_names, inplace=True)
out_df.to_csv('name_of_output', index=False)