from cobot_python import context

ctx = context.Context("192.168.1.253", 9000)

ctx.login("Admin", "333333")

print ctx.tran.token

print "check health: " + str(ctx.check_health())

state = param.get_robot_state(ctx)
print type(state)

print "robot state: " + str(state)

print "power on: " + str(servo.power(ctx))

print "get input status: " + str(io_service.get_input(ctx, 0))

ctx.logout()