#-------------------------------------------------------------------
#Traceback (most recent call last):
#   File "D:\codeTheDream\python_class\python-intro-homework\week-6\assignment-6\warmup3.py", line 6, in <module>
#     print(f"Validity of this pass is until : {Validity_month} ")
#                                               ^^^^^^^^^^^^^^
# NameError: name 'Validity_month' is not defined
""" def variable_scope():
    Validity_month="November"
    

variable_scope()
print(f"Validity of this pass is until : {Validity_month} ") """
#------------------------------------------------------------------------

def variable_scope():
    Validity_month="November"
    return Validity_month
    
print(f"Validity of this pass is until : {variable_scope()} ")