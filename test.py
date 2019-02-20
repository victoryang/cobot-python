from cobot_python import context

ctx = context.Context("192.168.1.253", 9000)

ctx.login("Admin", "333333")

ctx.logout()