import cv2
import mediapipe as mp

# import dodukuri
import utiokoshi
# import yugamae

def poseDetection( ):

    mp_pose = mp.solutions.pose
    mp_drawing = mp.solutions.drawing_utils

    flag = 0

    flags = []

    flags = [ 0 ] * 7

    cap = cv2.VideoCapture( 'target_video.mp4' )

    output_filename = 'detected_video.mp4'

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    #VideoWriter オブジェクトを初期化
    output_file = cv2.VideoWriter(output_filename,cv2.VideoWriter_fourcc(*'H264'),fps,(width,height))


    # 骨格検出器の初期化
    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                print("すべてのフレームの骨格検出が終了しました")
                break

            # BGR画像をRGBに変換
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # 骨格検出の実行
            results = pose.process(frame_rgb)

            # 検出結果に基づいて骨格を描画し、キーポイントの座標をプリント
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

                #各キーポイントの情報を表示するif文、一度コメントアウトしてある
                if( flag == 0 ):
                    for idx, landmark in enumerate(results.pose_landmarks.landmark):

                        #ここに関数で使いたいそれぞれの最初の座標を変数に代入する

                        print(f"Landmark {idx}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")

                    flag = 1
                
                ldk = results.pose_landmarks.landmark
                

                if( utiokoshi.utiokoshi( ldk[15].x, ldk[15].y, ldk[16].x, ldk[16].y, ldk[23].x, ldk[23].y, ldk[24].x, ldk[24].y ) == True and flags[ 2 ] != 1 ):
                    flags[ 2 ] = 1
                

            

            #動画ファイルに書き込み
            output_file.write( frame )

            # フレームを表示
            # cv2.imshow('MediaPipe Pose Detection', frame)
            

            # # 'q'キーで終了
            if cv2.waitKey(5) & 0xFF == ord('q'):
                break

        



    

    # リソースの解放
    cap.release()
    output_file.release()
    cv2.destroyAllWindows()

    return flags