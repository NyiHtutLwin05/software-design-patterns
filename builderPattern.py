class Computer:
    def __init__(self, cpu, ram, storage, gpu=None, display=None):
        self.cpu = cpu
        self.ram = ram
        self.storage = storage
        self.gpu = gpu
        self.display = display

    def __str__(self):
        return f"Computer: CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}, Display={self.display}"


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer("", "", "")

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_display(self, display):
        self.computer.display = display
        return self

    def build(self):
        return self.computer


builder = ComputerBuilder()
computer = builder.set_cpu("Intel i7").set_ram("16GB").set_storage(
    "512GB SSD").set_gpu("NVIDIA RTX 3060").build()
print(computer)
