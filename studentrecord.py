r_list=[]

def get_student_data():
    
    r_num =""
    s_name =""
    n_sub = 0
    sub_count = 0
    g_result = ""
    
    print("\n" + "--- STARTING DATA ENTRY FOR ONE STUDENT ---")
    
    r_num = input("Enter the Student's Roll Number (eg 101): ")
    s_name = input("Enter the student's Full Name: ")
    
    n_sub=int(input("Enter the total number of subjects for this student: "))

    s_record = {}
    s_record['R_N'] = r_num
    s_record['Name'] = s_name
    s_record['SubList'] = []
    
    while sub_count < n_sub:
      sub_count = sub_count+1
      print("  > Subject Number " + str(sub_count) +" of "+ str(n_sub) + ":")
      sub_name = input('    Enter the name of the subject: ')
      
      m_obtain= float(input('    Enter the marks obtained (e.g. 85.50): '))
      
      if m_obtain < 0.0 or m_obtain > 100.0:
          print("    [Warning!]: Marks are outside the 0-100 range. Check input.")

      if m_obtain >= 90.0:
          g_result ="A"
      elif m_obtain >= 80.0:
          g_result ="B"
      elif m_obtain >= 70.0:
          g_result ="C"
      elif m_obtain >= 60.0:
          g_result ="D"
      elif m_obtain >= 35.0:
          g_result ="E"
      else:
          g_result ="F" 
      
      s_record['SubList'].append({
          'N': sub_name,
          'M': m_obtain,
          'G': g_result
      })

    return s_record 

def display_table_data(s_name, r_num, sub_data):
    
    if not sub_data:
        print("\n!ERROR!: No subject data found to display.")
        return

    b_line ="================================================================================="
    print("\n" + b_line)
    
    print("RECORD FOUND FOR: "+s_name + "\t\t\t\t" + "ROLL NUMBER: "+r_num)
    print(b_line)
    
    print("SUBJECT NAME           MARKS OBTAINED      FINAL GRADE")
    print("--------------------   ------------------  ------------")

    for d in sub_data:
        
        m_str = "{:.2f}".format(d['M'])
        sub_col = d['N'].ljust(22)
        marks_col = m_str.ljust(20) 
        
        print(sub_col + marks_col + d['G']) 
        
    print(b_line)

def main_app_loop():
    
    global r_list 
    r_list = []

    print("\n" + "*****************************************************************")
    print("* WELCOME TO THE STUDENT RECORD MANAGEMENT SYSTEM V1.0 ALPHA *")
    print("*****************************************************************" + "\n")

    while True:
        choice = ""
        print("\n--- Primary Menu Options ---")
        print("1. Enter New Student Records (Start New Session)")
        print("2. Search/Display Record by Roll Number (Find Student)")
        print("3. Exit Program (Terminate Application)")

        choice= input("Please enter your selection (1, 2, or 3): ")

        if choice == "1":
            
            a_count_in = input("How many NEW students will you add right now?: ")
            
            a_count_in = int(a_count_in) 
            added_count_local= 0
            
            while added_count_local < a_count_in:
              new_data = get_student_data()

              r_list.insert(len(r_list), new_data) 
              added_count_local = added_count_local +1
              
              print(">>> Record number " + str(added_count_local) + " was successfully added.")
            
            print("\n[Status Report]: Finished adding " + str(added_count_local) + " record(s). Returning to menu.")
        
        elif choice == "2":
            
            f_record = None
            s_roll = ""
            found_flag= 0 
            
            if len(r_list) == 0:
                print("\n[Notice]: The student list is empty. Pls enter data (Option 1) first.")
                continue
            
            print("\n--- Start Record Search ---")
            s_roll= input("Enter the Roll Number to search for: ")

            i= 0
            while i < len(r_list):
                s= r_list[i]
                if s['R_N']== s_roll:
                    f_record = s
                    found_flag = 1
                    break
                i = i+1
            
            if found_flag == 1:
                display_table_data(f_record['Name'], f_record['R_N'], f_record['SubList'])
            else:
                print("\n[Search Fail]: Roll Number " + s_roll + " was not found. Try again.")
        
        elif choice == "3":
            print("\nApplication shutting down. Goodbye!")
            break
            
        else:
            print("\n!Input Error!: Invalid selection. Only 1, 2, or 3 is acceptable.")

if __name__ == "__main__":
    main_app_loop()