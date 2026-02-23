import sys
import os
import time

import schedule

import smtplib
from email.message import EmailMessage

class ZeroByteCleaner:
    def __init__(self, dirName):
        self.DirName = dirName
        self.TotalFileCount = 0
        self.EmptyFiles = 0
        self.DeletedFiles = 0
        self.DeleteErrors = 0
        self.Border = "-" * 80
        self.FileName = ""
    
    def DirectoryScanner(self):
        self.TotalFileCount = 0
        self.EmptyFiles = 0
        self.DeletedFiles = 0
        self.DeleteErrors = 0
        
        Ret = False
        
        Ret = os.path.exists(self.DirName)

        if(Ret == False):
            print("There is no such Path/Directory")
            return

        Ret = os.path.isdir(self.DirName)

        if(Ret == False):
            print("The given path is not a directory")
            return
        
        for Folders, SubFolders, Files in os.walk(self.DirName):
            # print("Folder : ", Folders)

            # for subf in SubFolders:
            #     print("Sub-Folder : ", subf)

            for fname in Files:
                # print("File : ", fname)
                self.TotalFileCount = self.TotalFileCount + 1
                filepath = os.path.join(Folders, fname)
                filesize = os.path.getsize(filepath)

                # print("File : ", fname)
                # print("File Size : ", filesize)

                if(filesize == 0):
                    self.EmptyFiles = self.EmptyFiles + 1
                    try:
                        os.remove(filepath)
                        self.DeletedFiles = self.DeletedFiles + 1
                    except Exception as e:
                        self.DeleteErrors = self.DeleteErrors + 1

        print("Scan Complete")
        print(f"Scanned : {self.TotalFileCount} | Deleted : {self.DeletedFiles} | Errors : {self.DeleteErrors}")      

    def LogFileWriter(self):

        timestamp = time.ctime()
        timestamp = timestamp.replace(" ", "_")
        timestamp = timestamp.replace(":", "_")

        self.FileName = ("LogReport_%s.txt" %(timestamp))

        logobj = open(self.FileName, "w")

        logobj.write(self.Border + "\n")
        logobj.write("-------------------- Zero-Byte Cleaner Automation Script -----------------------" + "\n")
        logobj.write(self.Border + "\n")

        # logobj.write(self.Border + "\n")
        logobj.write("This is a log file is created by Umesh Shivaji Bhabad\n")
        logobj.write("This is a directory Cleaner automation script\n")
        logobj.write(self.Border + "\n")
        
        # logobj.write(self.Border + "\n")
        logobj.write("Total Files : "+str(self.TotalFileCount) + "\n")
        logobj.write("Empty Files Found : "+ str(self.EmptyFiles) + "\n")
        logobj.write("Deleted Files : "+ str(self.DeletedFiles) + "\n")
        logobj.write("Error : "+ str(self.DeleteErrors) + "\n")
        logobj.write(self.Border + "\n")
        logobj.write("This log files is created at : "+ str(timestamp) + "\n")
        # logobj.write(self.Border + "\n")

        logobj.write(self.Border + "\n")
        logobj.write("----------------- Thank you for using this automation script -------------------" + "\n")
        logobj.write(self.Border + "\n")

    def send_mail(self, sender, password, receiver, subject, body, report):
    
        # Step 1 : Create Email object
        msg = EmailMessage()

        # Step 2 : Set Mail headers
        msg["From"] = sender
        msg["To"] = receiver
        msg["Subject"] = subject

        # Step 3 : Add Email Body
        msg.set_content(body)

        # Step 4 : Add attachment
        fobj = open(report, "rb")

        file_data = fobj.read()
        file_name = os.path.basename(report)

        msg.add_attachment (
                            file_data,
                            maintype = "application",
                            subtype = "octet-stream",
                            filename = file_name
                            )

        # Step 5 : Create SMTP SSL connection manually
        smtp_server = "smtp.gmail.com"
        port = 465
        smtp = smtplib.SMTP_SSL(smtp_server, port)

        # Step 6 : Login using Gmail + Password
        smtp.login(sender, password)

        # Step 7 : Send the email
        smtp.send_message(msg)

        # Step 8 : Close the connection manually
        smtp.quit()

    def __del__(self):
        print("Directory Scanned at : ", time.ctime())

def CleaningProcess(Dir):

    obj = ZeroByteCleaner(Dir)

    obj.DirectoryScanner()
    obj.LogFileWriter()

    # Sender Email
    sender_email = "umesh.example@gmail.com"

    # app password
    app_password = "Enter your app password here"

    # receiver mail
    receiver_email = "jhondoe.example@gmail.com"

    # Mail subject
    subject = f"Zero Byte Cleaner Report - {time.ctime()}"

    # Mail body
    body = """Jay Ganesh,

    This is a test email sent using Python.
    This Automation script is used to delete the empty file on directory.

    Regards,
    Umesh Bhabad
    """

    # Mail attachment
    report_path = obj.FileName

    obj.send_mail(sender_email, app_password, receiver_email, subject, body, report_path)

    print("Mail sent sucessfully with attachment")

    del obj

# Main method
def main():
    Border = "-" * 80

    print(Border)
    print("-------------------- Zero-Byte Cleaner Automation Script -----------------------")
    print(Border)

    if(len(sys.argv) == 3):
        DirectoryName = sys.argv[1]
        TimeInterval = int(sys.argv[2])

        schedule.every(TimeInterval).minutes.do(CleaningProcess, DirectoryName)

        while True:
            schedule.run_pending()
            time.sleep(1)

        # LogFileWriter()

    elif(len(sys.argv) == 2):
        if((sys.argv[1] == "--h") or (sys.argv[1] == "--H")):
            print("This application is used to delete all the empty files in the given directory/server")
            print("This is a automation script")
            return

        elif((sys.argv[1] == "--u") or (sys.argv[1] == "--U")):
            print("Use the given script as :")
            print("\tScriptName.py Argument1 Argument2")
            print()
            print("Argument1 : DirectoryName")
            print("Argument2 : TimeInterval")
            return
        
        else:
            print("Use the given flag as :")
            print("--u : used to display the usage")
            print("--h : used to display the help")
    
    else:
        print("Invalid number of command line arguments")
        print("Use the given flag as :")
        print("--u : used to display the usage")
        print("--h : used to display the help")
        return

    print(Border)
    print("----------------- Thank you for using this automation script -------------------")
    print(Border)

# Start of program
if __name__ == "__main__":
    main()