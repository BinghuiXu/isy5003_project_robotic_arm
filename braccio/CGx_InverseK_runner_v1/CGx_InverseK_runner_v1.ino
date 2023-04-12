// Include the library InverseK.h
#include <InverseK.h>
#include <Braccio.h>
#include <Servo.h>


Servo base;
Servo shoulder;
Servo elbow;
Servo wrist_rot;
Servo wrist_ver;
Servo gripper;

// Quick conversion from the Braccio angle system to radians
float b2a(float b){
  return b / 180.0 * PI - HALF_PI;
}

// Quick conversion from radians to the Braccio angle system
float a2b(float a) {
  return (a + HALF_PI) * 180 / PI;
}

void setup() {
  Serial.begin(9600);
  Serial.println("running setup");
  Braccio.begin();
  Braccio.ServoMovement(20,90, 90+5, 90-5, 90, 90,  10);
  // Setup the lengths and rotation limits for each link
  Link base2, upperarm, forearm, hand;

  base2.init(0, b2a(0.0), b2a(180.0));
  upperarm.init(200, b2a(15.0), b2a(165.0));
  forearm.init(200, b2a(0.0), b2a(180.0));
  hand.init(270, b2a(0.0), b2a(180.0));

  // Attach the links to the inverse kinematic model
  InverseK.attach(base2, upperarm, forearm, hand);

  float a0, a1, a2, a3;

  /*
  // InverseK.solve() return true if it could find a solution and false if not.

  
  // Calculates the angles without considering a specific approach angle
  // InverseK.solve(x, y, z, a0, a1, a2, a3)
  
  if(InverseK.solve(550, 100, 100, a0, a1, a2, a3)) {
    Serial.print(a2b(a0)); Serial.print(',');
    Serial.print(a2b(a1)); Serial.print(',');
    Serial.print(a2b(a2)); Serial.print(',');
    Serial.println(a2b(a3));
  } else {
    Serial.println("No solution found!");
  }

  // Calculates the angles considering a specific approach angle
  // InverseK.solve(x, y, z, a0, a1, a2, a3, phi)
  
  if(InverseK.solve(550, 100, 100, a0, a1, a2, a3, b2a(90.0))) {
    Serial.print(a2b(a0)); Serial.print(',');
    Serial.print(a2b(a1)); Serial.print(',');
    Serial.print(a2b(a2)); Serial.print(',');
    Serial.println(a2b(a3));
  } else {
    Serial.println("No solution found!");
  }
  */
  Serial.println("initial done");
}

//  Main Loop

void loop() {
  if (Serial.available() > 0) {
    String armpos = Serial.readStringUntil('\n');
    Serial.println(armpos);
    armpos.trim();

    // change var
    float values[6];
    int i = 0;
    while (armpos.length() > 0 && i < 6) {
      int pos = armpos.indexOf(',');
      if (pos >= 0) {
        values[i] = armpos.substring(0, pos).toFloat();
        armpos = armpos.substring(pos + 1);
      } else {
        values[i] = armpos.toFloat();
        armpos = "";
      }
      i++;
    }
    Serial.print("Values: ");
    Serial.print(values[0]);
    Serial.print(", ");
    Serial.print(values[1]);
    Serial.print(", ");
    Serial.print(values[2]);
    Serial.print(", ");
    Serial.print(values[3]);
    Serial.print(", ");
    Serial.print(values[4]);
    Serial.print(", ");
    Serial.println(values[5]);
    //move arm
    move(values[0],values[1],values[2],values[3],values[4],values[5]);
  } 
  
}

// braccio arm move with x,y,z input

void move(float x,float y,float z,float wrist, float grip, float phi){
  float a0, a1, a2, a3;
  if(phi==1000){
    Serial.println("run xyz without considering approaching positon");

    if(InverseK.solve(x, y, z, a0, a1, a2, a3)) {
      Serial.print(a2b(a0)); Serial.print(',');
      Serial.print(a2b(a1)); Serial.print(',');
      Serial.print(a2b(a2)); Serial.print(',');
      Serial.println(a2b(a3));
    } else {
      Serial.println("No solution found!");
    }
  } else if (phi<=180) {
    Serial.println("run xyz considering approaching positon");
    
    if(InverseK.solve(x, y, z, a0, a1, a2, a3, b2a(phi))) {
      Serial.print(a2b(a0)); Serial.print(',');
      Serial.print(a2b(a1)); Serial.print(',');
      Serial.print(a2b(a2)); Serial.print(',');
      Serial.println(a2b(a3));
    } else {
      Serial.println("No solution found!");
    } 
  } else if (phi>180 && phi<=500) {
    Serial.println("run servo angle directly");
    a0=b2a(x);
    a1=b2a(y);
    a2=b2a(z);
    a3=b2a(phi-300); // phi= wrist degrees-300, aka a3:0->phi:300
    Serial.print("a0,a1,a2,a3: ");
    Serial.print(a2b(a0));
    Serial.print(", ");
    Serial.print(a2b(a1));
    Serial.print(", ");
    Serial.print(a2b(a2));
    Serial.print(", ");
    Serial.println(a2b(a3));
    
  }
  Braccio.ServoMovement(20,a2b(a0), a2b(a1)+5, a2b(a2)-5, a2b(a3), wrist,grip);
  delay(3000);
}
