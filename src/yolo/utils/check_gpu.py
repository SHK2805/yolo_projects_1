import torch

def check_gpu():
    if torch.cuda.is_available():
        print("GPU is available")
    else:
        print("GPU is NOT available")


if __name__ == "__main__":
    check_gpu()