import logging
import logging.config
import logging_tree

# load my module
import my_module

print("--------------------------------------------------------")
print("Step1: 標準のroot logger")
logging_tree.printout()
print("--------------------------------------------------------")

print("--------------------------------------------------------")
print("Step2: なにも設定せずgetLogger()を呼ぶ")
my_module.foo()
bar = my_module.Bar()
bar.bar()
print("")
print("getLogger()によってmy_moduleというloggerが生成されている")
logging_tree.printout()
print("--------------------------------------------------------")

print("--------------------------------------------------------")
print("Step3: logging.ini / disable_existing_loggers=True")
logging.config.fileConfig('logging.ini', disable_existing_loggers=True)
my_module.foo()
bar = my_module.Bar()
bar.bar()
print("")
print("すでにStep1でmy_module loggerは作成済だったので、無効化されている")
logging_tree.printout()
print("--------------------------------------------------------")

print("--------------------------------------------------------")
print("Step4: logging.ini / disable_existing_loggers=False")
logging.config.fileConfig('logging.ini', disable_existing_loggers=False)
my_module.foo()
bar = my_module.Bar()
bar.bar()
print("")
print("disable_existing_loggers=Falseで有効化されている")
logging_tree.printout()
print("--------------------------------------------------------")