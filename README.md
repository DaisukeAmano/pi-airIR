# 概要
ASTINAのエアコン制御用プログラム
- 28度以上でエアコンを起動
- 27度以下でエアコンを終了

温度に関しては 'aircond.py' にて変更可能。

温度センサAM2320からI2C通信を用いて温度を取得。温度に応じてsubprocessからエアコンのon/offコマンドを実行。

# 使い方
I2Cのセットアップが完了していない場合は以下のサイトを参考にI2Cのセットアップを完了してください。社内ラズパイには既にインストールされています。  
https://www.fabshop.jp/denshikousaku-onshitudosensa/

プログラムは社内ラズパイの以下のディレクトリに保存されています。  
Document/cgir/cgir-master/aircond.py 

ターミナルから以下のコマンドを実行してください。  
python3 aircond.py

# 参考サイト 
I2C温度センサ関係  
https://qiita.com/kamujun/items/51f85339bfd582b27752
https://www.fabshop.jp/denshikousaku-onshitudosensa/  

赤外線受光・発光プログラム関係  
https://github.com/IndoorCorgi/cgir  
https://www.indoorcorgielec.com/resources/raspberry-pi/python-pigpio-infrared/  
https://www.indoorcorgielec.com/resources/raspberry-pi/aircond-control/ 

赤外線センサ  
https://www.indoorcorgielec.com/products/rpz-ir-sensor/  

温度センサ  
https://akizukidenshi.com/catalog/g/gM-08663/  

PythonのSubprocess  
https://qiita.com/tanabe13f/items/8d5e4e5350d217dec8f5

# 動作不良の場合
天野にchatworkで連絡を下さい。








