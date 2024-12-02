import streamlit as st
import vpd_test as vt
import cv2
from moviepy.editor import VideoFileClip
import os

pose_index = { 0 : "胴造り", 1 : "弓構え", 2 : "打起し", 3 : "引分け", 4 : "会", 5: "離れ", 6 : "残身" }

st.title( "弓道の姿勢評価" )

st.header( "姿勢を評価する動画をiPhoneで撮影してアップロードしてください" )

uploaded_file = st.file_uploader( "", type=[ "mov" ] )




if uploaded_file is not None:

    file_name = "target_video.MOV"
    content = uploaded_file.read()
    
    with st.spinner('processing...'):
    # 拡張子のチェック
        if not file_name.endswith(( ".mov", ".MOV" )):

            st.error("サポートされていないファイル形式です。")

        with open( "target_video.MOV", "wb" ) as f:
            f.write( content )

        video_clip = VideoFileClip( file_name )

        output_file = "target_video.mp4"

        width = video_clip.size[0]
        height = video_clip.size[1]

        video_clip.write_videofile(output_file, codec='libx264', ffmpeg_params=["-vf", f"scale={width}:{height}"])
        
        result = vt.poseDetection()

        if os.path.exists( "detected_video.mp4" ):
            st.video( "detected_video.mp4" )
    
        else:
            st.error( "処理された動画ファイルが見つかりません。" )

        for i in range( 7 ):
            if( result[ i ] == 0 ):
                st.text( pose_index[ i ] + " = 失敗" )
            else:
                st.text( pose_index[ i ] + " = 成功")