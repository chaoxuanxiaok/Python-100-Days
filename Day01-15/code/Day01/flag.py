"""
用Python的turtle模块绘制国旗
"""
import turtle


def draw_rectangle(x, y, width, height):
    """绘制矩形"""
    # 画笔跳转到指定坐标
    turtle.goto(x, y)
    # 画笔笔尖变成红色
    turtle.pencolor('red')
    # 画笔填充色变成红色
    turtle.fillcolor('red')
    # 画笔开始填充图形
    turtle.begin_fill()
    for i in range(2):  # 宽和高需要画两次
        turtle.forward(width)   # 画笔直行画宽度
        turtle.left(90) # 画笔左转90度
        turtle.forward(height)  # 画笔直行画高度
        turtle.left(90)
    # 画笔结束填充图形
    turtle.end_fill()


def draw_star(x, y, radius):
    """绘制五角星"""
    turtle.setpos(x, y)
    # 通过五个点，绘制一个圆形
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    # 将画笔的颜色变为黄色
    turtle.color('yellow', 'yellow')
    # 开始填充大五角星------------begin
    turtle.begin_fill()
    # 画笔移到右下角
    turtle.goto(pos3)
    # 画笔移到顶角
    turtle.goto(pos1)
    # 画笔移到左下角
    turtle.goto(pos4)
    # 画笔移到右平角
    turtle.goto(pos2)
    # 画笔移到左平角
    turtle.goto(pos5)
    # 结束填充大五角星---end，将中途画笔所经过线条的闭合区间填充满
    turtle.end_fill()


def main():
    """主程序"""
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180
    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)
    # 画大星星
    pice = 22
    # 画笔移到大星星的起始位，五角星正中心（-270+110，-180+360-110）=（-160,70）
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]
    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)
    # 隐藏海龟
    turtle.ht()
    # 显示绘图窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()