import random
import time

class FlyVisualizer:
    def __init__(self, width=1080, height=1920):
        self.x, self.y = width // 2, height // 2
        self.width, self.height = width, height

    def update_position(self):
        # Sinek, etrafta küçük, öngörülemez "sıçramalar" yapacak
        # 1 Hz modunda olduğumuz için çok yavaş ve minimal hareketler
        self.x += random.randint(-5, 5)
        self.y += random.randint(-5, 5)
        
        # Ekrandan çıkarsa sınırlara geri döndür
        self.x = max(0, min(self.width, self.x))
        self.y = max(0, min(self.height, self.y))
        
        return (self.x, self.y)

# Test modülü: Sinek ekranda nasıl süzülüyor?
visualizer = FlyVisualizer()
for _ in range(5):
    pos = visualizer.update_position()
    print(f"🪰 [SYSTEM]: Sinek koordinatları güncellendi: {pos}")
    time.sleep(1) # 1Hz yani saniyede 1 güncelleme
