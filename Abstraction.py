class A:
    def  __init__(self,call,camera):
        self.call=call       #----> Hiding these implementation details
        self.camera=camera       #----> Hiding these implementation details
        print(f"Accessing camera {camera}")
        print("Picking up call")


s1=A(True,"Camera1")
