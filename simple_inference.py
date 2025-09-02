import torch
import cv2
import numpy as np

model = torch.hub.load("ultralytics/yolov5", "yolov5s")
img_path = "test1.jpg"

results = model(img_path)
df = results.pandas().xyxy[0]

img = results.render()[0]
img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

img_cv = cv2.imread(cv2.samples.findFile("test1.jpg"))
for _, row in df.iterrows():
    xmin, ymin, xmax, ymax = int(row["xmin"]), int(row["ymin"]), int(row["xmax"]), int(row["ymax"])
    label = f"{row['name']} {row['confidence']:.2f}"
    cv2.rectangle(img_cv, (xmin, ymin), (xmax, ymax), (0, 255, 0), 2)
    cv2.putText(img_cv, label, (xmin, ymin - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

cv2.imshow("YOLOv5 Detection", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
