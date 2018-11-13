class Setting():
    def __init__(self):
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 15

        # 子弹设置
        self.bullet_speed_factor = 30
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullet_allowed = 3

        # 外星人设置
        self.alien_space_factor = 10
        self.fleet_drop_speed = 100
        # 1 代表向右 -1代表向左
        self.fleet_direction = 10
