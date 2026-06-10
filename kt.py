employee_list =[]

while True :
    print("1.them nhan vien moi ")
    print("2.danh sach nhan vien ")
    print("3.xoa nhan vien khoi danh sach ")
    print("4.thoat chuong trinh")

    choice = input("moi ban nhap lua chon cua minh(1-4) :")
    count = len(employee_list)
    if choice == "1":
        print(count)
        id = 101 + count 
        while True :
            name = input("moi ban nhap ten :").strip()
            if name == "":
                print("ten ko dc de trong! vui long nhap lai  ")
            else:
                break
        while True :
            lasary = input("moi ban nhap luong :")
            if lasary == "" :
                print("luong ko hop le ! vui long nhap lai")
            else :
                lasary = int(lasary)
                if lasary <0:
                    print("luong ko hop le ! vui long nhap lai")
                else:
                    break
        
        employee_list.append ({
            "id" :id,
            "name" : name,
            "lasary" : lasary
        })
        print("them nhan vien thanh cong ")
        
        

    elif choice=="2":
        if len(employee_list) ==0 :
            print("chua co du lieu nhan su")
        else :
            print("ID| ten| muc luong ")
            for i in range (len(employee_list)):
                employee = employee_list[i] 
                print(f"{employee['id']}|"
                f"{employee['name']}|"
                f"{employee['lasary']}")
    
    elif choice =="3":
        id = int(input("moi ban nhap id muon xoa :"))
        found =False
        for i in range (len(employee_list)):
            employee = employee_list[i] 
            if id == employee['id']:
                employee_list.pop(i)
                print("xoa thanh cong ")
                found = True 
        
        if not found :
            print("ko tim thay nhan vien de xoa ")
    
    elif choice == "4":
        print(" thoat chuong trinh")
        break

    else :
        print("lua chon ko hop le! vui long nhap lai (1-4)")