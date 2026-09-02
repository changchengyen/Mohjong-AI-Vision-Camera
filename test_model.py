from ai_edge_litert.interpreter import Interpreter

interpreter = Interpreter(model_path="best_int8.tflite")
interpreter.allocate_tensors()

print("Model loaded successfully!")

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

print(input_details)
print(output_details)
