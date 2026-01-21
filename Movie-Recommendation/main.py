import subprocess

print("Starting training process...")

train_result = subprocess.run(["python", "train.py"], capture_output=True, text=True)

print(train_result.stdout)
if train_result.returncode != 0:
    print("Training failed with error:")
    print(train_result.stderr) 
    exit(1)

print("Training completed successfully.")
print("Starting recommendation process...")

recommend_result = subprocess.run(["python", "recommend.py"], capture_output=True, text=True)

print(recommend_result.stdout)
if recommend_result.returncode != 0:
    print("Recommendation failed with error:")
    print(recommend_result.stderr)
    exit(1)

print("Recommendation process completed successfully.")