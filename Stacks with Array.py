class Stack:
    def __init__(self):
        self.items = []  # ใช้ list เก็บข้อมูล

    def push(self, item):
        """เพิ่มข้อมูลเข้าไปใน stack"""
        self.items.append(item)

    def pop(self):
        """ลบและคืนค่าข้อมูลที่อยู่บนสุด"""
        if not self.is_empty():
            return self.items.pop()
        else:
            return "Stack is empty!"  # ถ้าว่าง แสดงข้อความตามตัวอย่าง

    def peek(self):
        """คืนค่าข้อมูลบนสุดโดยไม่ลบออก"""
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        """ตรวจสอบว่า stack ว่างหรือไม่"""
        return len(self.items) == 0

    def size(self):
        """คืนค่าจำนวนสมาชิกใน stack"""
        return len(self.items)


if __name__ == "__main__":
    s = Stack()

    print("Is empty?", s.is_empty())

    for i in range(1, 6):
        s.push(i)

    print("Size after push:", s.size())
    print("Top element:", s.peek())

    # pop ค่าออกทีละตัว
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())

    print("Is empty?", s.is_empty())
    print("Pop from empty:", s.pop())
