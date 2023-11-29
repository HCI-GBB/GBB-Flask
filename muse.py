import pandas as pd


def get_result():
    df1 = pd.read_csv('게임-세라.csv', encoding='utf-8')
    df2 = pd.read_csv('음악감상-세라.csv', encoding='utf-8')
    df3 = pd.read_csv('수다-세라.csv', encoding='utf-8')
    df4 = pd.read_csv('쇼핑-세라.csv', encoding='utf-8')

    extraction1 = df1[['Theta_AF8', 'Name']]
    extraction2 = df2[['Theta_AF8', 'Name']]
    extraction3 = df3[['Theta_AF8', 'Name']]
    extraction4 = df4[['Theta_AF8', 'Name']]

    preprocessing1 = extraction1.dropna(how='all')
    preprocessing2 = extraction2.dropna(how='all')
    preprocessing3 = extraction3.dropna(how='all')
    preprocessing4 = extraction4.dropna(how='all')

    result1 = preprocessing1['Theta_AF8'].mean()
    result2 = preprocessing2['Theta_AF8'].mean()
    result3 = preprocessing3['Theta_AF8'].mean()
    result4 = preprocessing4['Theta_AF8'].mean()

    name1 = df1['Name'].iloc[0]
    name2 = df2['Name'].iloc[0]
    name3 = df3['Name'].iloc[0]
    name4 = df4['Name'].iloc[0]

    data = {'Value': [result1, result2, result3, result4], 'Name': [name1, name2, name3, name4]}
    sum1 = pd.DataFrame(data)

    new_result = sum1.sort_values(by=['Value'], ascending=False)
    new_result = new_result.reset_index(drop=True)

    return new_result['Name'][0], new_result['Name'].values.tolist()
