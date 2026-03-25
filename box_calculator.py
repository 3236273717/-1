def calculate_boxes_and_boards():
    # 表达式中的各个部分及其对应的板数
    items = [
        (40 * 4, 4),    # 40*4 对应 4板
        (12, 1),        # 12 对应 1板
        (48, 1),        # 48 对应 1板
        (16, 1),        # 16 对应 1板
        (40 * 5, 5),    # 40*5 对应 5板
        (48, 1),        # 48 对应 1板
        (36, 36)        # 36 对应 36板
    ]
    
    # 计算总框数
    total_boxes = sum(item[0] for item in items)
    
    # 计算总板数
    total_boards = sum(item[1] for item in items)
    
    # 输出结果
    print("=== 框数和板数计算 ===")
    print(f"总框数: {total_boxes}")
    print(f"总板数: {total_boards}")
    print("\n详细计算:")
    
    for i, (boxes, boards) in enumerate(items):
        print(f"项 {i+1}: {boxes} 框, {boards} 板")
    
    return total_boxes, total_boards

if __name__ == "__main__":
    calculate_boxes_and_boards()