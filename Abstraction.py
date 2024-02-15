class A:
    def  __init__(self,call,camera):
        self.call=call
        self.camera=camera
        print(f"Accessing camera {camera}")
        print("Picking up call")


s1=A(True,"Camera1")
