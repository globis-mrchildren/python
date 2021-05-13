{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# 課題2-1: 一元分散分析\n",
    "\n",
    "A社は、エタノールを製造・販売しています。5本の製造ラインがありますが、これらのラインにより製品の濃度に差がないかどうかを確認したく思います。5本のライン(A, B, C, D, E)から10回ずつサンプリングを行い測定を行った結果が *dataset/data1.csv* です（データ数の合計：50件）。このデータを一元分散分析にて解析し、結論を出してみましょう。\n",
    "\n",
    "レッスン7までで学んだ内容を踏まえ、各セルに入っているコメントを実行するコードを記入してください。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 1. 必要なモジュールの読み込み"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import scipy as sp\n",
    "from scipy import stats\n",
    "\n",
    "from matplotlib import pyplot as plt\n",
    "import seaborn as sns\n",
    "sns.set()\n",
    "\n",
    "import statsmodels.formula.api as smf\n",
    "import statsmodels.api as sm\n",
    "\n",
    "%matplotlib inline\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 2. データの読み込み"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# データを読み込んで変数 data に格納\n",
    "data1 = pd.read_csv('data1.csv')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Density</th>\n",
       "      <th>Line</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>71.624345</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>69.388244</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69.471828</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>68.927031</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>70.865408</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Density Line\n",
       "0  71.624345    A\n",
       "1  69.388244    A\n",
       "2  69.471828    A\n",
       "3  68.927031    A\n",
       "4  70.865408    A"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# データの最初の5行だけ表示\n",
    "data1.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Density</th>\n",
       "      <th>Line</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>71.624345</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>69.388244</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>69.471828</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>68.927031</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>70.865408</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>67.698461</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>71.744812</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>69.238793</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>70.319039</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>69.750630</td>\n",
       "      <td>A</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>69.583242</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>69.943733</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>67.863804</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>71.640271</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>68.206564</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>69.158253</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>70.502881</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>68.754712</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>68.942048</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>69.090992</td>\n",
       "      <td>B</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>20</th>\n",
       "      <td>72.077257</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>21</th>\n",
       "      <td>69.373020</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>22</th>\n",
       "      <td>68.692995</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>23</th>\n",
       "      <td>65.273015</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>24</th>\n",
       "      <td>67.945224</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25</th>\n",
       "      <td>67.790482</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>26</th>\n",
       "      <td>68.934517</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>27</th>\n",
       "      <td>67.745999</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>28</th>\n",
       "      <td>68.912364</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>29</th>\n",
       "      <td>67.545564</td>\n",
       "      <td>C</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>30</th>\n",
       "      <td>69.050562</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>31</th>\n",
       "      <td>69.499951</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>32</th>\n",
       "      <td>68.004091</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>33</th>\n",
       "      <td>69.693599</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>34</th>\n",
       "      <td>68.581698</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>35</th>\n",
       "      <td>67.415423</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>36</th>\n",
       "      <td>68.352293</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>37</th>\n",
       "      <td>69.598575</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>38</th>\n",
       "      <td>69.332250</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>39</th>\n",
       "      <td>67.852523</td>\n",
       "      <td>D</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>40</th>\n",
       "      <td>69.441227</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>41</th>\n",
       "      <td>68.669130</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>42</th>\n",
       "      <td>71.430771</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>43</th>\n",
       "      <td>68.747908</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>44</th>\n",
       "      <td>69.109610</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>45</th>\n",
       "      <td>70.582481</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>46</th>\n",
       "      <td>68.090768</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>47</th>\n",
       "      <td>68.408363</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>48</th>\n",
       "      <td>69.187603</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>49</th>\n",
       "      <td>68.670130</td>\n",
       "      <td>E</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Density Line\n",
       "0   71.624345    A\n",
       "1   69.388244    A\n",
       "2   69.471828    A\n",
       "3   68.927031    A\n",
       "4   70.865408    A\n",
       "5   67.698461    A\n",
       "6   71.744812    A\n",
       "7   69.238793    A\n",
       "8   70.319039    A\n",
       "9   69.750630    A\n",
       "10  69.583242    B\n",
       "11  69.943733    B\n",
       "12  67.863804    B\n",
       "13  71.640271    B\n",
       "14  68.206564    B\n",
       "15  69.158253    B\n",
       "16  70.502881    B\n",
       "17  68.754712    B\n",
       "18  68.942048    B\n",
       "19  69.090992    B\n",
       "20  72.077257    C\n",
       "21  69.373020    C\n",
       "22  68.692995    C\n",
       "23  65.273015    C\n",
       "24  67.945224    C\n",
       "25  67.790482    C\n",
       "26  68.934517    C\n",
       "27  67.745999    C\n",
       "28  68.912364    C\n",
       "29  67.545564    C\n",
       "30  69.050562    D\n",
       "31  69.499951    D\n",
       "32  68.004091    D\n",
       "33  69.693599    D\n",
       "34  68.581698    D\n",
       "35  67.415423    D\n",
       "36  68.352293    D\n",
       "37  69.598575    D\n",
       "38  69.332250    D\n",
       "39  67.852523    D\n",
       "40  69.441227    E\n",
       "41  68.669130    E\n",
       "42  71.430771    E\n",
       "43  68.747908    E\n",
       "44  69.109610    E\n",
       "45  70.582481    E\n",
       "46  68.090768    E\n",
       "47  68.408363    E\n",
       "48  69.187603    E\n",
       "49  68.670130    E"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Density</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>50.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>69.134490</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.281785</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>65.273015</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>68.366311</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>69.070777</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>69.594742</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>72.077257</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Density\n",
       "count  50.000000\n",
       "mean   69.134490\n",
       "std     1.281785\n",
       "min    65.273015\n",
       "25%    68.366311\n",
       "50%    69.070777\n",
       "75%    69.594742\n",
       "max    72.077257"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "data1.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 50 entries, 0 to 49\n",
      "Data columns (total 2 columns):\n",
      " #   Column   Non-Null Count  Dtype  \n",
      "---  ------   --------------  -----  \n",
      " 0   Density  50 non-null     float64\n",
      " 1   Line     50 non-null     object \n",
      "dtypes: float64(1), object(1)\n",
      "memory usage: 928.0+ bytes\n"
     ]
    }
   ],
   "source": [
    "data1.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 3. データ内容の把握"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Line', ylabel='Density'>"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# （データ数が多くはないので）箱髭図にて製造ラインごとの濃度を表示\n",
    "sns.boxplot(x='Line', y='Density',data=data1)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 4. 分散分析\n",
    "\n",
    "ここでは理解を深めるために手動で計算して理解を深めましょう。"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4-1. 群間・群内平方和の計算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "69.9028591091939\n",
      "69.36865005840153\n",
      "68.42904350984494\n",
      "68.73809656689362\n",
      "69.23379915563065\n",
      "69.13448967999292\n"
     ]
    }
   ],
   "source": [
    "#各ラインでの濃度平均\n",
    "me_L_A = np.mean(data1.query('Line ==\"A\"')['Density'])\n",
    "me_L_B = np.mean(data1.query('Line ==\"B\"')['Density'])\n",
    "me_L_C = np.mean(data1.query('Line ==\"C\"')['Density'])\n",
    "me_L_D = np.mean(data1.query('Line ==\"D\"')['Density'])\n",
    "me_L_E = np.mean(data1.query('Line ==\"E\"')['Density'])\n",
    "me_all = np.mean(data1['Density'])\n",
    "\n",
    "print(me_L_A)\n",
    "print(me_L_B)\n",
    "print(me_L_C)\n",
    "print(me_L_D)\n",
    "print(me_L_E)\n",
    "print(me_all)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array([69.90285911, 69.90285911, 69.90285911, 69.90285911, 69.90285911,\n",
       "       69.90285911, 69.90285911, 69.90285911, 69.90285911, 69.90285911,\n",
       "       69.36865006, 69.36865006, 69.36865006, 69.36865006, 69.36865006,\n",
       "       69.36865006, 69.36865006, 69.36865006, 69.36865006, 69.36865006,\n",
       "       68.42904351, 68.42904351, 68.42904351, 68.42904351, 68.42904351,\n",
       "       68.42904351, 68.42904351, 68.42904351, 68.42904351, 68.42904351,\n",
       "       68.73809657, 68.73809657, 68.73809657, 68.73809657, 68.73809657,\n",
       "       68.73809657, 68.73809657, 68.73809657, 68.73809657, 68.73809657,\n",
       "       69.23379916, 69.23379916, 69.23379916, 69.23379916, 69.23379916,\n",
       "       69.23379916, 69.23379916, 69.23379916, 69.23379916, 69.23379916])"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#効果の平方和\n",
    "effect = [me_L_A]*len(data1.query('Line == \"A\"'))+[me_L_B]*len(data1.query('Line == \"B\"'))+[me_L_C]*len(data1.query('Line == \"C\"'))+[me_L_D]*len(data1.query('Line == \"D\"'))+[me_L_E]*len(data1.query('Line == \"E\"'))\n",
    "effect = np.array(effect)\n",
    "effect"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(69.13448968)"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "me_all = np.array(me_all)\n",
    "me_all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13.098668335875422"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#　群間の平方和を求める（効果の平方和）\n",
    "squares_line = np.sum((effect-me_all)**2)\n",
    "squares_line"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "67.4069531127806"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#　群間の誤差を求める（誤差の平方和）\n",
    "resid = data1['Density']-effect\n",
    "\n",
    "squares_resid = np.sum(resid**2)\n",
    "squares_resid"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "2.1861249021602567"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#　群内の平方和を求める\n",
    "df_line = 5-1\n",
    "df_resid = 50-1-4\n",
    "\n",
    "variance_line = squares_line/df_line\n",
    "variance_resid = squares_resid/df_resid\n",
    "\n",
    "f_ratio = variance_line/variance_resid\n",
    "f_ratio"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.0857496485120679"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "1-sp.stats.f.cdf(x=f_ratio,dfn=df_line,dfd=df_resid)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4-2. 群間・群内分散の計算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    " # 群間変動の自由度を変数 df_model に格納し、群内変動の自由度を変数 df_resid に格納する\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 群間の平均平方（分散）を求める\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [],
   "source": [
    "# 群内の平均平方（分散）を求める\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### 4-3. p値の計算"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "# F比を求める\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "# p値を求めて、表示する\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 5. Statsmodelsによる分散分析\n",
    "\n",
    "実務ではStatsmodelsを使って実行していくことになります。次に、Statsmodelsのパッケージを用いて計算してみましょう。"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>sum_sq</th>\n",
       "      <th>df</th>\n",
       "      <th>F</th>\n",
       "      <th>PR(&gt;F)</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>Line</th>\n",
       "      <td>13.098668</td>\n",
       "      <td>4.0</td>\n",
       "      <td>2.186125</td>\n",
       "      <td>0.08575</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Residual</th>\n",
       "      <td>67.406953</td>\n",
       "      <td>45.0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "             sum_sq    df         F   PR(>F)\n",
       "Line      13.098668   4.0  2.186125  0.08575\n",
       "Residual  67.406953  45.0       NaN      NaN"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# 最小二乗法を使ってモデルを作成\n",
    "anova_model_1 = smf.ols('Density ~ Line',data=data1).fit()\n",
    "sm.stats.anova_lm(anova_model_1, typ=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "# Statsmodelsの関数で分散分析を実行し、結果を表示\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "手動で計算した場合と結果は一致しましたか？"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## 6. 結果の解釈"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "ラインによって、製品の濃度は「  」と判断できる（ここをダブルクリックして編集状態にし、カギカッコの中に文言を埋めてください）"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "*補足：有意差がみられた場合、これは化学メーカーとしては問題ですので製造ラインの詳細を確認する必要があります。*"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
