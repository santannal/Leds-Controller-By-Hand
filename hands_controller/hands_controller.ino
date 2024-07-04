const int led1 = 2;
const int led2 = 3;
const int led3 = 6;
const int led4 = 10;
const int led5 = 12;

char currentCommand = '0';

void setup() {
    Serial.begin(9600); 
    pinMode(led1, OUTPUT);
    pinMode(led2, OUTPUT);
    pinMode(led3, OUTPUT);
    pinMode(led4, OUTPUT);
    pinMode(led5, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        char serialCommand = Serial.read();   
        currentCommand = serialCommand;
    }
    controlarLeds(currentCommand);
}

void controlarLeds(char command) {
    // Liga ou desliga LEDs conforme o comando recebido
    switch (command) {
        case '1':
            digitalWrite(led1, HIGH);
            digitalWrite(led2, LOW);
            digitalWrite(led3, LOW);
            digitalWrite(led4, LOW);
            digitalWrite(led5, LOW);
            break;
        case '2':
            digitalWrite(led1, HIGH);
            digitalWrite(led2, HIGH);
            digitalWrite(led3, LOW);
            digitalWrite(led4, LOW);
            digitalWrite(led5, LOW);
            break;
        case '3':
            digitalWrite(led1, HIGH);
            digitalWrite(led2, HIGH);
            digitalWrite(led3, HIGH);
            digitalWrite(led4, LOW);
            digitalWrite(led5, LOW);
            break;
        case '4':
            digitalWrite(led1, HIGH);
            digitalWrite(led2, HIGH);
            digitalWrite(led3, HIGH);
            digitalWrite(led4, HIGH);
            digitalWrite(led5, LOW);
            break;
        case '5':
            digitalWrite(led1, HIGH);
            digitalWrite(led2, HIGH);
            digitalWrite(led3, HIGH);
            digitalWrite(led4, HIGH);
            digitalWrite(led5, HIGH);
            break;
        case '0':
            digitalWrite(led1, LOW);
            digitalWrite(led2, LOW);
            digitalWrite(led3, LOW);
            digitalWrite(led4, LOW);
            digitalWrite(led5, LOW);
            break;
        default:
            break;
    }
}
