#!/usr/bin/env python3

# used to generate model: unsqueeze.onnx

import torch
import torch.nn as nn


class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.axis = 3

    def forward(self, x):
        x = torch.unsqueeze(x, self.axis)
        return x


def main():
    # Set seed for reproducibility
    torch.manual_seed(42)

    torch.set_printoptions(precision=8)

    # Export to onnx
    model = Model()
    model.eval()
    device = torch.device("cpu")

    file_name = "unsqueeze_torch.onnx"
    test_input = torch.randn(3, 4, 5, device=device)
    model = Model()

    output = model.forward(test_input)

    torch.onnx.export(model, (test_input), file_name, verbose=False, opset_version=16)

    print(f"Finished exporting model to {file_name}")

    # Output some test data for use in the test
    print(f"Test input data of ones: {test_input}")
    print(f"Test input data shape of ones: {test_input.shape}")
    # output = model.forward(test_input)
    print(f"Test output data shape: {output.shape}")

    print(f"Test output: {output}")


if __name__ == "__main__":
    main()