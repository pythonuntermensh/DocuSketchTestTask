# MemoryAlarmTestTask
Simple script to check if memory is full and alarm server for DocuSketch test task.

You need firstly to run test_server.py and then run memory_checker.py.

test_server.py has 1 controller on "/alarm"-url.
memory_checker.py checks memory every n-seconds (by default - 3 seconds).

By default, if the memory is more than 90 percent full, an alarm request will be sent to the server and the script will stop working.
