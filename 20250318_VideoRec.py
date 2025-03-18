import cv2 as cv

vd = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'MJPG')
save = cv.VideoWriter('webcam_rec.avi', fourcc, 60, (1280, 960))

is_recording = False
is_flipped = False  

if vd.isOpened() :
  fps = vd.get(cv.CAP_PROP_FPS)
  if fps == 0:
    fps = 60
  wait_msec = int(1/fps*1000)
 
  while True :
    valid, img = vd.read()
    if not valid :
      print("프레임 읽기 실패")
      break
   
    if is_flipped:
        img = cv.flip(img, 1)  # 좌우 반전 적용
    if is_recording:
      original_img = img.copy()  # 원본 프레임을 저장
      save.write(original_img)   # 원본 프레임을 녹화 파일에 저장
      img = cv.rectangle(img, (0, 0), (img.shape[1], img.shape[0]), (0, 0, 255), 10) 
      
    font = cv.FONT_HERSHEY_SIMPLEX  # 폰트 설정
    cv.putText(img, "R: rec", (30, 30), font, 0.6, (0, 0, 0), 2, cv.LINE_AA)  # 녹화 텍스트
    cv.putText(img, 'R: rec', (30, 30), font, 0.6, (0, 255, 0), 1, cv.LINE_AA)  
    cv.putText(img, 'SPACE: flip', (30, 60), font, 0.6, (0, 0, 0), 2, cv.LINE_AA)  # 반전 텍스트
    cv.putText(img, 'SPACE: flip', (30, 60), font, 0.6, (0, 255, 0), 1, cv.LINE_AA)  
    cv.putText(img, 'ESC: exit', (30, 90), font, 0.6, (0, 0, 0), 2, cv.LINE_AA)  # 종료 텍스트  
    cv.putText(img, 'ESC: exit', (30, 90), font, 0.6, (0, 255, 0), 1, cv.LINE_AA)  

    cv.imshow('video player', img)
    key = cv.waitKey(wait_msec)
    if key == 27 : # ESC키를 누르면 종료
      break
    elif key == ord('r'): # R키를 누르면 녹화 시작/종료
        is_recording = not is_recording

    elif key == ord(' '):  # space키를 누르면 좌우 반전
        is_flipped = not is_flipped
else :
  print('rtsp 스트림 연결 실패')

cv.destroyAllWindows()















