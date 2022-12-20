import pandas as pd

test_df1 = pd.DataFrame(
    {
        'name':[
            'ShunDev',
            'fuga',
            'hoge',
            'joe',
        ],
        'point':[
            20,
            30,
            40,
            50,
        ]
    }
)
test_df1.to_csv('csv/test_csv1.csv')

test_df2 = pd.DataFrame(
    {
        'name':[
            'toro',
            'tarako',
            'ikura',
            'iwashi',
        ],
        'point':[
            60,
            30,
            80,
            10,
        ]
    }
)
test_df2.to_csv('csv/test_csv2.csv')

test_df3 = pd.DataFrame(
    {
        'name':[
            'toro',
            'tarako',
            'ikura',
            'iwashi',
        ],
        'POINT':[
            60,
            30,
            80,
            10,
        ]
    }
)
test_df3.to_csv('csv/test_csv3.csv')