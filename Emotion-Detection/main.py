import cv2
from fer import FER

cap = cv2.VideoCapture(0)

detector = FER(mtcnn=True)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = detector.detect_emotions(frame)

    for result in results:
        (x, y, w, h) = result["box"]
        emotion, score = max(result["emotions"].items(), key=lambda item: item[1])
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, f"{emotion} ({score:.2f})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)

        cv2.imshow("Emotion Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()