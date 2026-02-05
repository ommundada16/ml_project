import sys

def error_message_detail(error,error_detail:sys):      #1st paarmeter : for our msg of error , 2n para: for the error msg from the system
    _,_,exc_tb = error_detail.exc_info()     #we get 3 parameters as output, but we are only interested in 3rd parameter which will give us the filename and the location of the error
    file_name = exc_tb.tb_frame.f_code.co_filename          #error location
    error_message = "error occured in python script name[{0}] line number[{1}] error message[{2}]".format(           #here we are using placeholders for rprinting. just basic format chnage in the syntax of print
    file_name,exc_tb.tb_lineno, str(error)

    )            



class CustomException(Exception):              #the paramter is linking this class to the inbuilt Exception class
    def __init__(self,error_message,error_detail:sys):        #constructor
        super.__init__(error_message)
        self.error_message = error_message_detail(error_message, error_detail = error_detail)
    def __str__(self):
        return self.error_message          