OpenCV 기반 웹캠 녹화 및 화면 반전 프로그램

이 프로그램은 OpenCV를 사용하여 웹캠 영상을 실시간으로 출력하고, 녹화 및 좌우 반전 기능을 제공
cv.VideoWriter_fourcc(*'XVID')로 XVID 포맷의 코덱을 지정
CAP_PROP_FPS를 사용하여 웹캠의 프레임 속도(FPS)를 가져옴
만약 FPS 값을 얻지 못하면 기본값 60을 사용
wait_msec = int(1 / fps * 1000)를 사용하여 cv.waitKey()의 딜레이를 조정하여 원활한 프레임 속도를 유지
해상도는 1280 X 960으로 지정

**기능 설명**
1. **웹캠 영상 실시간 출력**
   - OpenCV의 `VideoCapture(0)`를 사용하여 웹캠을 실행하고 실시간으로 화면에 출력

2. **녹화 기능 (`R` 키)**
   - waitKey를 사용하여 `R` 키를 누르면 **녹화가 시작되며**, VideoWriter에 의해 영상이 `webcam_rec.avi` 파일로 저장
   - 녹화 중일 때는 화면에 **빨간 테두리**가 표시
   - 다시 `R` 키를 누르면 **녹화가 중지**

3. **화면 좌우 반전 기능 (`SPACE` 키)**
   - waitKey를 사용하여 `SPACE` 키를 누르면 **실시간 영상이 좌우 반전**

4. **프로그램 종료 (`ESC` 키)**
   - waitKey를 사용하여 `ESC` 키를 누르면 프로그램이 종료

5. **해당 기능들을 putText를 통해 테두리가 있는 글씨로 표시**

**기본화면**

![image](https://github.com/user-attachments/assets/d48048a9-ba15-40d1-b735-d265ea59ac98)

**녹화**

![image](https://github.com/user-attachments/assets/c8d22c09-26b2-41e3-ab09-0d1bf721d495)

**반전**

![image](https://github.com/user-attachments/assets/ad855cdc-6942-4e9f-8ca2-9919499f9cf8)

**저장된 모습**

![image](https://github.com/user-attachments/assets/22cdffaf-1843-43c6-99b5-54e988b7c62f)
