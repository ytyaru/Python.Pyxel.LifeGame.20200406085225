[ja](./README.ja.md)

# Pyxel.LifeGame

Life game with Pyxel.

# DEMO

![demo](doc/demo.gif)

# Requirement

* <time datetime="2020-04-06T08:52:10+0900">2020-04-06</time>
* [Raspbierry Pi](https://ja.wikipedia.org/wiki/Raspberry_Pi) 4 Model B Rev 1.2
* [Raspbian](https://ja.wikipedia.org/wiki/Raspbian) buster 10.0 2019-09-26 <small>[setup](http://ytyaru.hatenablog.com/entry/2019/12/25/222222)</small>
* bash 5.0.3(1)-release
* Python 3.7.3
* [pyxel][] 1.3.1

[pyxel]:https://github.com/kitao/pyxel

```sh
$ uname -a
Linux raspberrypi 4.19.97-v7l+ #1294 SMP Thu Jan 30 13:21:14 GMT 2020 armv7l GNU/Linux
```

# Installation

Install Python 3.7 or higher.

Next, install [pyxel][] as follows.

* [pyxel/README](https://github.com/kitao/pyxel/blob/master/README.md#how-to-install)

```sh
sudo apt install python3 python3-pip libsdl2-dev libsdl2-image-dev
git clone https://github.com/kitao/pyxel.git
cd pyxel
make -C pyxel/core clean all
pip3 install .
```

# Usage

```sh
git clone https://github.com/ytyaru/Python.Pyxel.LifeGame.20200406085225
cd Python.Pyxel.LifeGame.20200406085225/src
./run.sh
```

# Note

* Exit with `ESC` key
    * May need to be pressed many times
        * Because FPS is too slow to be accepted

# Author

ytyaru

* [![github](http://www.google.com/s2/favicons?domain=github.com)](https://github.com/ytyaru "github")
* [![hatena](http://www.google.com/s2/favicons?domain=www.hatena.ne.jp)](http://ytyaru.hatenablog.com/ytyaru "hatena")
* [![mastodon](http://www.google.com/s2/favicons?domain=mstdn.jp)](https://mstdn.jp/web/accounts/233143 "mastdon")

# License

This software is CC0 licensed.

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.en)

