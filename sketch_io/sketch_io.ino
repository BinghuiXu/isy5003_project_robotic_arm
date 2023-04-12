void setup() {
  Serial.begin(9600); // 初始化串口通信，波特率为9600
}

void loop() {
  if (Serial.available() > 0) { // 如果有数据可读
    String inputString = Serial.readStringUntil('\n'); // 读取串口数据直到遇到换行符
    inputString.trim(); // 去掉前后空格

    // 将字符串分割成多个子字符串，并转换为数字类型
    int values[3];
    int i = 0;
    while (inputString.length() > 0 && i < 3) {
      int pos = inputString.indexOf(',');
      if (pos >= 0) {
        values[i] = inputString.substring(0, pos).toInt();
        inputString = inputString.substring(pos + 1);
      } else {
        values[i] = inputString.toInt();
        inputString = "";
      }
      i++;
    }

    // 输出结果
    Serial.print("Values: ");
    Serial.print(values[0]);
    Serial.print(", ");
    Serial.print(values[1]);
    Serial.print(", ");
    Serial.println(values[2]);
  }
}
