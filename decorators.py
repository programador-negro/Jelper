from datetime import datetime
from colorama import Fore

def total_time_execution(function):
    def container(*args, **kwargs):
        start_time = datetime.now()
        function(*args, **kwargs)
        end_time = datetime.now()
        
        print(Fore.GREEN +  \
        "TIME EXECUTION\n" + \
        f"START: , {start_time}\n" + \
        f"END: , {end_time}\n" + \
        f"- - - - - - -\n" + \
        f"TOTAL TIME: {end_time - start_time}\n" + \
        Fore.RESET)

    return container
    