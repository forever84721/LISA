import torch, time

x = torch.rand((8192, 8192), device="cuda")
torch.cuda.synchronize()

t0 = time.time()
y = x @ x
torch.cuda.synchronize()

print("矩陣乘法耗時(ms):", (time.time()-t0)*1000)
print("最大顯存使用(MB):", torch.cuda.max_memory_allocated()//(1024**2))
