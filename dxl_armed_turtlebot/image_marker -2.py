#!/usr/bin/env python

import rospy  #rospy内のファイルの読み込み
from opencv_apps.msg import RotatedRectStamped  #opencv_apps/msg内のファイルからRotatedRectStamped.msgを読み込む
from image_view2.msg import ImageMarker2  #image_view2/msg内のファイルからImageMarker2.msgを読み込む
from geometry_msgs.msg import Point  #geometry_msgs/msg内のPint.msgを読み込む

#関数の定義
def cb(msg):
    print msg.rect  #矩形の情報を出力する
    marker = ImageMarker2()  #markerの設定
    marker.type = 0  #マーカーの形を円にする
    marker.position = Point(msg.rect.center.x, msg.rect.center.y, 0)  #マーカーの中心を矩形の中心にする（z座標は0）
    pub.publish(marker)  #markerを送信する

rospy.init_node('client')  #初期化宣言..."client"という名前のソフトウェアであると宣言する
rospy.Subscriber('/camshift/track_box', RotatedRectStamped, cb)  #SubscriberとしてRotatedRectStampedというトピックに対してSubscribeし、トピックが更新されたときにはcb関数を実行する
pub = rospy.Publisher('/image_marker', ImageMarker2)  #nodeの宣言...Subscriberのインスタンスwp作る。"/camshift/track_box"というtopicにRotatedRectStamped型のSubscriberを作成
rospy.spin()  #トピック更新の待受を行う関数

"""
gitについて、
mech-user@test1-pc:~/catkin_ws/src/robot-programming$ git remote -v
origin	https://github.com/jsk-enshu/robot-programming (fetch)
origin	https://github.com/jsk-enshu/robot-programming (push)
ryota_morimoto	http://github.com/ryota_morimoto/robot-programming (fetch)
ryota_morimoto	http://github.com/ryota_morimoto/robot-programming (push)
mech-user@test1-pc:~/catkin_ws/src/robot-programming$ git fetch --allFetching origin
Fetching ryota_morimoto
Username for 'https://github.com': ryota_morimoto
Password for 'https://ryota_morimoto@github.com':
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/ryota_morimoto/robot-programming/'
error: Could not fetch ryota_morimoto
のようになってしまい、設定したことのないパスワードを要求されてどうすればいいのか解決方法がわからなかったため、ソースコードの形で（とりあえず）提出させていただきます。
"""
