import mlflow

import warnings

def calculate(x,y):
    return x*y

if __name__ == "__main__":

    with mlflow.start_run():
        x,y = 100,200

        result = calculate(x,y)
        print(f"here is my result {result}")
        mlflow.log_param("X",x)
        mlflow.log_param("Y",y)
        mlflow.log_param("Result",result)

    

