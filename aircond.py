#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import smbus
import subprocess

i2c = smbus.SMBus(1)
address = 0x5c
trigger = 0
 
if __name__ == '__main__':
    try:
            while 1:
                # センサsleep解除
                try:
                    i2c.write_i2c_block_data(address,0x00,[])
                except:
                    pass

                # 読み取り命令
                time.sleep(0.003)
                i2c.write_i2c_block_data(address,0x03,[0x00,0x04])

                # データ受取
                time.sleep(0.015)
                block = i2c.read_i2c_block_data(address,0,6)
                humidity = float(block[2] << 8 | block[3])/10
                temperature = float(block[4] << 8 | block[5])/10

                print('温度={0:0.1f}℃ 湿度={1:0.1f}%'.format(temperature, humidity))

                #スイッチ判断
                if trigger == 0:
                    if temperature >=28:
                        print('./cgirtool.py send air_enable')
                        cp = subprocess.run(['./cgirtool.py', 'send', 'air_enable'])
                        trigger = 1
                        if cp.returncode != 0:
                            print('ls failed.', file=sys.stderr)
                            sys.exit(1)
                if trigger == 1:
                    if temperature <=27:
                        print('./cgirtool.py send air_disable')
                        cp = subprocess.run(['./cgirtool.py', 'send', 'air_disable'])
                        trigger = 0
                        if cp.returncode != 0:
                            print('ls failed.', file=sys.stderr)
                            sys.exit(1)

                time.sleep(2)

    except KeyboardInterrupt:
        sys.exit(0)