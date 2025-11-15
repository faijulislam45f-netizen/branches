def rohit_profile(**info):
    must_keys= ["Name", "Email"]
    for key in must_keys:
        if key not in info:
            print(f" missing: {key}")
            return
    print("    ---Profile---")
    for k, v in info.items():
         print(f" {k.title():<10}: {v}")
rohit_profile( 
                    Name="Rohit Singh", 
                    Email="rohit@abc.com", 
                    Gender="Male", 
                    Age="25", 
                    State="UP", 
                    City="Lucknow", 
                    Phone="9876543210")