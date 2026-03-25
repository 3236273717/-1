from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.clock import Clock

class BoxBoardCalculatorApp(App):
    def build(self):
        # 设置窗口大小
        Window.size = (360, 640)
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # 标题
        title_label = Label(text='框板计算器', font_size=24, bold=True, size_hint_y=None, height=60)
        main_layout.add_widget(title_label)
        
        # 输入区域
        input_layout = BoxLayout(orientation='vertical', size_hint_y=None, height=120)
        input_label = Label(text='输入表达式:', font_size=16, size_hint_y=None, height=30)
        input_layout.add_widget(input_label)
        
        self.expression_input = TextInput(
            text='40*4+12+48+16+40*5+48+36',
            font_size=16,
            multiline=True,
            size_hint_y=None,
            height=80
        )
        self.expression_input.bind(text=self.on_text_change)
        input_layout.add_widget(self.expression_input)
        main_layout.add_widget(input_layout)
        
        # 按钮区域
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        self.calculate_button = Button(text='计算', font_size=16, width=100)
        self.calculate_button.bind(on_press=self.on_calculate_click)
        button_layout.add_widget(self.calculate_button)
        
        history_button = Button(text='历史记录', font_size=16, width=100)
        history_button.bind(on_press=self.show_history)
        button_layout.add_widget(history_button)
        
        main_layout.add_widget(button_layout)
        
        # 结果显示区域
        result_layout = BoxLayout(orientation='vertical', padding=15, spacing=15)
        result_label = Label(text='计算结果', font_size=18, bold=True, size_hint_y=None, height=40)
        result_layout.add_widget(result_label)
        
        # 框数和板数显示
        boxes_layout = BoxLayout(size_hint_y=None, height=40)
        boxes_label = Label(text='总框数:', font_size=16)
        self.boxes_result = Label(text='0', font_size=20, bold=True)
        boxes_layout.add_widget(boxes_label)
        boxes_layout.add_widget(self.boxes_result)
        result_layout.add_widget(boxes_layout)
        
        boards_layout = BoxLayout(size_hint_y=None, height=40)
        boards_label = Label(text='总板数:', font_size=16)
        self.boards_result = Label(text='0', font_size=20, bold=True)
        boards_layout.add_widget(boards_label)
        boards_layout.add_widget(self.boards_result)
        result_layout.add_widget(boards_layout)
        
        main_layout.add_widget(result_layout)
        
        # 初始化历史记录
        self.history = []
        
        # 初始计算
        self.calculate(should_save=False)
        
        return main_layout
    
    def on_text_change(self, instance, value):
        # 实时计算但不保存历史记录
        self.calculate(should_save=False)
    
    def on_calculate_click(self, instance):
        # 点击计算按钮时，计算并保存历史记录
        self.calculate(should_save=True)
    
    def calculate(self, should_save=False):
        expression = self.expression_input.text.strip()
        if not expression:
            self.boxes_result.text = '0'
            self.boards_result.text = '0'
            return
        
        try:
            # 移除表达式末尾的特殊字符（+或*）
            while expression and expression[-1] in ['+', '*']:
                expression = expression[:-1].strip()
            
            if not expression:
                self.boxes_result.text = '0'
                self.boards_result.text = '0'
                return
            
            # 分割表达式为各个项
            items = expression.split('+')
            total_boxes = 0
            total_boards = 0
            
            for item in items:
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
            self.boxes_result.text = str(total_boxes)
            self.boards_result.text = str(total_boards)
            
            # 只有在should_save为True时才保存历史记录
            if should_save:
                # 保存到历史记录
                current_expr = self.expression_input.text.strip()
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
                    
                    for item in items:
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
                    
                    self.boxes_result.text = str(total_boxes)
                    self.boards_result.text = str(total_boards)
                    
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
                    self.boxes_result.text = '0'
                    self.boards_result.text = '0'
            except:
                self.boxes_result.text = '错误'
                self.boards_result.text = '错误'
    
    def show_history(self, instance):
        # 创建历史记录弹窗
        if not self.history:
            # 无历史记录时
            content = BoxLayout(orientation='vertical', padding=20, spacing=10)
            content.add_widget(Label(text='暂无历史记录', font_size=16))
            close_button = Button(text='关闭', size_hint_y=None, height=40)
            content.add_widget(close_button)
            
            popup = Popup(title='计算历史', content=content, size_hint=(0.9, 0.6))
            close_button.bind(on_press=popup.dismiss)
            popup.open()
        else:
            # 有历史记录时
            scroll = ScrollView()
            history_layout = GridLayout(cols=1, spacing=10, size_hint_y=None)
            history_layout.bind(minimum_height=history_layout.setter('height'))
            
            for i, item in enumerate(self.history):
                item_box = BoxLayout(orientation='vertical', padding=10, size_hint_y=None, height=80)
                item_box.add_widget(Label(text=f'表达式: {item["expression"]}', font_size=14, halign='left', valign='middle', text_size=(300, None)))
                item_box.add_widget(Label(text=f'框数: {item["boxes"]}, 板数: {item["boards"]}', font_size=14, bold=True, halign='left', valign='middle', text_size=(300, None)))
                history_layout.add_widget(item_box)
                
                if i < len(self.history) - 1:
                    history_layout.add_widget(Label(size_hint_y=None, height=1, color=(0, 0, 0, 0.3)))
            
            scroll.add_widget(history_layout)
            
            content = BoxLayout(orientation='vertical')
            content.add_widget(scroll)
            close_button = Button(text='关闭', size_hint_y=None, height=50)
            content.add_widget(close_button)
            
            popup = Popup(title='计算历史', content=content, size_hint=(0.9, 0.7))
            close_button.bind(on_press=popup.dismiss)
            popup.open()

if __name__ == '__main__':
    BoxBoardCalculatorApp().run()