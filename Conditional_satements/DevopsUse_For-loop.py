#server provisioning and configuration
# List of servers
servers = ["server1", "server2", "server3"]

# Function to configure monitoring agent
def configure_monitoring_agent(server):
    print(f"Configuring monitoring agent on {server}")

# Loop through each server and configure
for server in servers:
    configure_monitoring_agent(server)


#Deploying configuration on Multiple Environments
Environments=["Dev","Staging","Prod"]
def deploying_configuring_servers(environment):
    print(f"deploying configuring agent on {environment}")

for envirinment in Environments:
    deploying_configuring_servers(envirinment)

#Backup and restore
databases=["DB1","DB2","DB3"]
def create_backup(DB):
    print(f"create backup on {DB}")
for DB in databases:
    create_backup(DB)

#Log rotation and cleanup
# List of log files
log_files = ["app.log", "access.log", "error.log"]
def rotate_and_cleanup_logs(log_file):
    print(f"Rotating and cleaning up {log_file}")
for log_file in log_files:
    rotate_and_cleanup_logs(log_file)

#Monitoring and reporting
servers=["server-1","server-2","server-3"]
def check_resource_servers(server):
    print(f"Check resource utilization on {server}")

for server in servers:
    check_resource_servers(server)

#Managing and Cloud resource
instances=["instance-1","instance-2","instance-3"]
def resize_instance(instance):
    print(f"resize instance {instance}")
for instance in instances:
    resize_instance(instance)