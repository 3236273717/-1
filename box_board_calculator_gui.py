import tkinter as tk
from tkinter import ttk

class BoxBoardCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("框板计算器")
        # 设置为手机界面大小
        self.root.geometry("360x640")
        self.root.resizable(False, False)
        
        # 设置样式
        self.style = ttk.Style()
        self.style.configure('TLabel', font=('SimHei', 14))
        self.style.configure('TButton', font=('SimHei', 14))
        self.style.configure('TEntry', font=('SimHei', 14))
        
        # 创建主框架
        self.main_frame = ttk.Frame(self.root, padding="20")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        ttk.Label(self.main_frame, text="框板计算器", font=('SimHei', 18, 'bold')).pack(pady=20)
        
        # 输入区域
        input_frame = ttk.Frame(self.main_frame)
        input_frame.pack(fill=tk.X, pady=10)
        
        ttk.Label(input_frame, text="输入表达式:", width=10).pack(side=tk.TOP, padx=5, pady=5)
        # 使用Text组件替代Entry，实现自动换行
        # 使用CHAR模式确保数字和运算符不会被分割
        self.expression_text = tk.Text(input_frame, height=3, font=('SimHei', 14), wrap=tk.CHAR)
        self.expression_text.pack(fill=tk.X, expand=True, padx=5)
        # 设置Text组件的宽度，确保有足够空间显示较长的表达式
        self.expression_text.config(width=25)
        # 设置初始值
        self.expression_text.insert(tk.END, "40*4+12+48+16+40*5+48+36")
        # 添加输入事件监听器，实现实时计算和自动调整字体大小
        self.expression_text.bind('<KeyRelease>', lambda event: self.on_text_change())
        
        # 按钮区域
        button_frame = ttk.Frame(self.main_frame)
        button_frame.pack(fill=tk.X, pady=10)
        
        # 计算按钮
        ttk.Button(button_frame, text="计算", command=self.on_calculate_click, width=10).pack(side=tk.LEFT, padx=5)
        
        # 历史记录按钮
        ttk.Button(button_frame, text="历史记录", command=self.show_history, width=10).pack(side=tk.RIGHT, padx=5)
        
        # 结果显示区域
        result_frame = ttk.LabelFrame(self.main_frame, text="计算结果", padding="15")
        result_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # 总框数和总板数
        self.total_boxes_var = tk.StringVar()
        self.total_boards_var = tk.StringVar()
        
        ttk.Label(result_frame, text="总框数:").grid(row=0, column=0, sticky=tk.W, pady=15)
        ttk.Label(result_frame, textvariable=self.total_boxes_var, width=10, font=('SimHei', 20, 'bold')).grid(row=0, column=1, sticky=tk.W, pady=15)
        
        ttk.Label(result_frame, text="总板数:").grid(row=1, column=0, sticky=tk.W, pady=15)
        ttk.Label(result_frame, textvariable=self.total_boards_var, width=10, font=('SimHei', 20, 'bold')).grid(row=1, column=1, sticky=tk.W, pady=15)
        
        # 配置网格权重
        result_frame.grid_columnconfigure(1, weight=1)
        
        # 初始化历史记录列表
        self.history = []
        # 初始计算
        self.calculate(should_save=False)
    
    def on_text_change(self):
        # 自动调整字体大小
        self.adjust_font_size()
        # 实时计算但不保存历史记录
        self.calculate(should_save=False)
    
    def on_calculate_click(self):
        # 点击计算按钮时，计算并保存历史记录
        self.calculate(should_save=True)
    
    def adjust_font_size(self):
        # 获取文本内容
        text = self.expression_text.get(1.0, tk.END).strip()
        if not text:
            return
        
        # 根据文本长度调整字体大小
        # 基础字体大小
        base_font_size = 14
        # 最大文本长度
        max_length = 30
        
        # 计算当前文本长度
        text_length = len(text)
        
        # 计算新的字体大小
        if text_length > max_length:
            # 字体大小随文本长度增加而减小
            new_font_size = max(8, base_font_size - (text_length - max_length) // 5)
        else:
            new_font_size = base_font_size
        
        # 更新字体大小
        self.expression_text.config(font=('SimHei', new_font_size))
    
    def show_history(self):
        # 创建历史记录窗口
        history_window = tk.Toplevel(self.root)
        history_window.title("计算历史")
        history_window.geometry("320x400")
        history_window.resizable(False, False)
        
        # 创建历史记录框架
        history_frame = ttk.Frame(history_window, padding="20")
        history_frame.pack(fill=tk.BOTH, expand=True)
        
        # 标题
        ttk.Label(history_frame, text="计算历史", font=('SimHei', 16, 'bold')).pack(pady=15)
        
        # 历史记录列表
        if not self.history:
            ttk.Label(history_frame, text="暂无历史记录", font=('SimHei', 12)).pack(pady=20)
        else:
            # 创建历史记录表格
            for i, item in enumerate(self.history):
                # 创建条目框架
                item_frame = ttk.Frame(history_frame, padding="10")
                item_frame.pack(fill=tk.X, pady=5, ipady=5)
                item_frame.config(relief=tk.RAISED)
                
                # 表达式
                ttk.Label(item_frame, text=f"表达式: {item['expression']}", font=('SimHei', 10)).pack(anchor=tk.W, pady=2)
                # 结果
                ttk.Label(item_frame, text=f"框数: {item['boxes']}, 板数: {item['boards']}", font=('SimHei', 10, 'bold')).pack(anchor=tk.W, pady=2)
                
                # 添加分隔线
                if i < len(self.history) - 1:
                    ttk.Separator(history_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=5)
        
        # 关闭按钮
        ttk.Button(history_frame, text="关闭", command=history_window.destroy, width=10).pack(pady=20)
    
    def calculate(self, should_save=False):
        # 从Text组件获取表达式
        expression = self.expression_text.get(1.0, tk.END).strip()
        if not expression:
            self.total_boxes_var.set("0")
            self.total_boards_var.set("0")
            return
        
        try:
            # 移除表达式末尾的特殊字符（+或*）
            while expression and expression[-1] in ['+', '*']:
                expression = expression[:-1].strip()
            
            if not expression:
                self.total_boxes_var.set("0")
                self.total_boards_var.set("0")
                return
            
            # 分割表达式为各个项
            items = expression.split('+')
            total_boxes = 0
            total_boards = 0
            
            for i, item in enumerate(items):
                item = item.strip()
                if not item:
                    continue
                
                if '*' in item:
                    # 处理乘法项，如 40*4
                    a, b = item.split('*')
                    a = int(a.strip())
                    b = int(b.strip())
                    box_count = a * b
                    # 板数为第二个因子
                    board_count = b
                else:
                    # 处理单独数字项
                    box_count = int(item.strip())
                    # 所有非乘法项的板数为1
                    board_count = 1
                
                total_boxes += box_count
                total_boards += board_count
            
            # 更新结果
            self.total_boxes_var.set(str(total_boxes))
            self.total_boards_var.set(str(total_boards))
            
            # 只有在should_save为True时才保存历史记录
            if should_save:
                # 保存到历史记录
                current_expr = self.expression_text.get(1.0, tk.END).strip()
                # 移除末尾的特殊字符
                temp_expr = current_expr
                while temp_expr and temp_expr[-1] in ['+', '*']:
                    temp_expr = temp_expr[:-1].strip()
                
                if temp_expr:
                    # 构建历史记录条目
                    history_item = {
                        'expression': temp_expr,
                        'boxes': str(total_boxes),
                        'boards': str(total_boards)
                    }
                    
                    # 添加到历史记录开头
                    self.history.insert(0, history_item)
                    
                    # 保持历史记录不超过5个
                    if len(self.history) > 5:
                        self.history = self.history[:5]
                
        except Exception as e:
            # 当表达式末尾有+或*时，尝试移除后重新计算
            try:
                temp_expr = expression
                while temp_expr and temp_expr[-1] in ['+', '*']:
                    temp_expr = temp_expr[:-1].strip()
                
                if temp_expr:
                    items = temp_expr.split('+')
                    total_boxes = 0
                    total_boards = 0
                    
                    for i, item in enumerate(items):
                        item = item.strip()
                        if not item:
                            continue
                        
                        if '*' in item:
                            a, b = item.split('*')
                            a = int(a.strip())
                            b = int(b.strip())
                            box_count = a * b
                            board_count = b
                        else:
                            box_count = int(item.strip())
                            board_count = 1
                        
                        total_boxes += box_count
                        total_boards += board_count
                    
                    self.total_boxes_var.set(str(total_boxes))
                    self.total_boards_var.set(str(total_boards))
                    
                    # 只有在should_save为True时才保存历史记录
                    if should_save:
                        # 构建历史记录条目
                        history_item = {
                            'expression': temp_expr,
                            'boxes': str(total_boxes),
                            'boards': str(total_boards)
                        }
                        
                        # 添加到历史记录开头
                        self.history.insert(0, history_item)
                        
                        # 保持历史记录不超过5个
                        if len(self.history) > 5:
                            self.history = self.history[:5]
                else:
                    self.total_boxes_var.set("0")
                    self.total_boards_var.set("0")
            except:
                self.total_boxes_var.set("错误")
                self.total_boards_var.set("错误")

if __name__ == "__main__":
    root = tk.Tk()
    app = BoxBoardCalculator(root)
    root.mainloop()