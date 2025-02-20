Communication Contract  

How to request data from the microservice:
1. Write to the "needed_nums.txt" file.
    Example call: with open("needed_nums.txt", 'w') as file:
                      file.write(str(num_cards))
2. Execute the microservice, I recommend using subprocess.run()

How to receive data from the microservice:
1. After executing the microservice, allow the process to finish.
2. Read from the needed_nums.txt file.
   Example call: with open("needed_nums.txt", 'r') as file:
                     result = file.read().strip()

![A UML sequence diagram showing requesting and receiving data from the
Tarot PRNG Microservice](UML_Sequence_Diagram.jpeg "Microservice UML Diagram")