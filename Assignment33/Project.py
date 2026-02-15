import psutil
import sys
import os
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime

# ---------------------------------------------------------
# Utility : Create Log Directory
# ---------------------------------------------------------
def CreateLogDirectory(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

# ---------------------------------------------------------
# Utility : Write Log
# ---------------------------------------------------------
def WriteLog(folder_name, data):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder_name, "MarvellousLog_%s.log" % timestamp)
    
    with open(filename, "w") as f:
        f.write(data)

# ---------------------------------------------------------
# 1. Thread Monitoring Feature
# ---------------------------------------------------------
def ThreadMonitoring():
    result = ""
    
    for proc in psutil.process_iter(['pid','name','num_threads']):
        try:
            result += f"Process Name : {proc.info['name']}\n"
            result += f"PID : {proc.info['pid']}\n"
            result += f"Thread Count : {proc.info['num_threads']}\n"
            result += "-"*50 + "\n"
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    return result

# ---------------------------------------------------------
# 2. Open Files Monitoring Feature
# ---------------------------------------------------------
def OpenFilesMonitoring():
    result = ""
    
    for proc in psutil.process_iter(['pid','name']):
        try:
            files = proc.open_files()
            count = len(files)
            
            result += f"Process Name : {proc.info['name']}\n"
            result += f"PID : {proc.info['pid']}\n"
            result += f"Open Files Count : {count}\n"
            result += "-"*50 + "\n"
            
        except psutil.AccessDenied:
            result += f"Process Name : {proc.info['name']} - Access Denied\n"
            result += "-"*50 + "\n"
        except psutil.NoSuchProcess:
            continue

    return result

# ---------------------------------------------------------
# 3. Memory Allocation Feature
# ---------------------------------------------------------
def MemoryMonitoring():
    result = ""
    
    process_list = []
    
    for proc in psutil.process_iter(['pid','name','memory_info','cpu_percent','num_threads']):
        try:
            memory = proc.info['memory_info'].rss
            process_list.append((proc.info['name'], proc.info['pid'], memory))
        except:
            continue
    
    process_list.sort(key=lambda x: x[2], reverse=True)
    
    result += "Top 10 Memory Consuming Processes\n"
    result += "="*50 + "\n"
    
    for proc in process_list[:10]:
        result += f"Process Name : {proc[0]}\n"
        result += f"PID : {proc[1]}\n"
        result += f"Memory (RSS) : {proc[2]}\n"
        result += "-"*50 + "\n"
        
    return result

# ---------------------------------------------------------
# 4. Send Email
# ---------------------------------------------------------
def SendEmail(receiver, logfile):
    try:
        msg = EmailMessage()
        msg['Subject'] = "Platform Surveillance Report"
        msg['From'] = "your_email@gmail.com"
        msg['To'] = receiver
        
        msg.set_content("Please find attached log report.")
        
        with open(logfile, 'rb') as f:
            file_data = f.read()
            msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=os.path.basename(logfile))
        
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login("your_email@gmail.com", "your_app_password")
        server.send_message(msg)
        server.quit()
        
    except Exception as e:
        print("Email sending failed:", e)

# ---------------------------------------------------------
# Main Surveillance Logic
# ---------------------------------------------------------
def Surveillance(interval, receiver):
    
    folder = "MarvellousLogs"
    CreateLogDirectory(folder)
    
    while True:
        log_data = ""
        log_data += "Timestamp : " + str(datetime.now()) + "\n"
        log_data += "="*60 + "\n\n"
        
        log_data += ThreadMonitoring()
        log_data += OpenFilesMonitoring()
        log_data += MemoryMonitoring()
        
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        logfile = os.path.join(folder, "MarvellousLog_%s.log" % timestamp)
        
        with open(logfile, "w") as f:
            f.write(log_data)
        
        SendEmail(receiver, logfile)
        
        time.sleep(interval)

# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------
def main():
    
    if len(sys.argv) != 4:
        print("Usage : PlatformSurveillance.py <LogFolder> <ReceiverEmail> <IntervalInMinutes>")
        sys.exit()
    
    folder = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3]) * 60
    
    Surveillance(interval, receiver)

# ---------------------------------------------------------
if __name__ == "__main__":
    main()