from flask import Flask
from operations import Operation
from exception import *

app=Flask(__name__)

@app.route('/<method>/<int:a>/<int:b>')
def adding(method,a,b):
    obj_1=Operation(a,b)
    if method == 'add':
        try:
            if a<10 and b<10:
                resp=obj_1.add()
                return str(resp)

            else:
                raise AddError("values are large")

        except AddError as v:
           return str(v)


    if method == 'sub':
        try:
            if a>b:
                resp=obj_1.sub()
                return str(resp)

            else:
                raise SubError("value of b is always lesser than a ")

        except SubError as v:
           return str(v)
        

    if method == 'mul':
        try:
            if a< 10 and b<10:
                resp=obj_1.mul()
                return str(resp)

            else:
                raise MulError("values are large")

        except MulError as v:
           return str(v)
        

    if method == 'div':
        try:
            if b!=0 :
                resp=obj_1.div()
                return str(resp)

            else:
                raise DivError("the value of b is non zero value")

        except DivError as v:
            return str(v)
    

if __name__ == '__main__':
    app.run(debug=True , port=5019)  